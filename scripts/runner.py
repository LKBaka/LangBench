# scripts/runner.py
import subprocess
import time
import statistics
import argparse
import yaml
import json
from pathlib import Path


class BenchmarkRunner:
    def __init__(self, languages_config, test_suite_config):
        self.languages = languages_config
        self.suite_config = test_suite_config

    def run_benchmark(self, test_case_path, language_name):
        lang_config = self.languages[language_name]
        results = []

        # 编译阶段（如果需要）
        output_file = None
        source_file = None
        if lang_config.get('compile_command'):
            compile_result = self.compile_test_case(test_case_path, lang_config)
            if not compile_result['success']:
                return compile_result
            output_file = compile_result['output_file']
            source_file = compile_result.get('source_file')
        else:
            # 解释型语言，查找源文件
            source_file = self.find_source_file(test_case_path, lang_config)
            if not source_file:
                return {
                    'success': False,
                    'error': f'No source file found with extension {lang_config.get("file_extension", "")}'
                }

        # 预热运行
        for _ in range(self.suite_config.get('warmup_runs', 5)):
            self.run_single_execution(test_case_path, lang_config, output_file, source_file)

        # 正式测试运行
        for _ in range(self.suite_config.get('iterations', 50)):
            result = self.run_single_execution(test_case_path, lang_config, output_file, source_file)
            results.append(result)

        return self.analyze_results(results)

    def compile_test_case(self, test_case_path, lang_config):
        """编译测试用例"""
        test_case_path = Path(test_case_path)
        file_ext = lang_config.get('file_extension', '')

        # 查找该扩展名的所有源文件
        source_files = []
        for file in test_case_path.iterdir():
            if file.is_file() and file.suffix == file_ext:
                source_files.append(str(file))

        if not source_files:
            return {'success': False, 'error': f'No source files found with extension {file_ext}'}

        # 创建临时输出目录
        output_dir = Path("/tmp/langbench")
        output_dir.mkdir(exist_ok=True)
        output_file = output_dir / f"benchmark_{test_case_path.name}"

        # 执行编译命令
        compile_cmd = lang_config['compile_command'].format(
            sources=' '.join(source_files),
            output=str(output_file)
        )

        try:
            process = subprocess.run(
                compile_cmd,
                shell=True,
                capture_output=True,
                text=True,
                timeout=120
            )

            if process.returncode != 0:
                return {
                    'success': False,
                    'error': f"Compilation failed: {process.stderr}",
                    'stdout': process.stdout,
                    'stderr': process.stderr,
                    'return_code': process.returncode
                }

            return {
                'success': True,
                'output_file': str(output_file),
                'source_file': source_files[0]  # 保存第一个源文件路径
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Compilation timeout'}

    def find_source_file(self, test_case_path, lang_config):
        """查找要运行的源文件"""
        test_case_path = Path(test_case_path)
        file_ext = lang_config.get('file_extension', '')

        for file in test_case_path.iterdir():
            if file.is_file() and file.suffix == file_ext:
                return str(file)
        return None

    def run_single_execution(self, test_case_path, lang_config, output_file=None, source_file=None):
        start_time = time.time()
        start_memory = self.get_memory_usage()

        try:
            # 确定运行命令
            if output_file and lang_config.get('compile_command'):
                # 编译型语言：运行可执行文件
                run_cmd = lang_config['run_command'].format(output=str(output_file))
            else:
                # 解释型语言：直接运行源文件
                if not source_file:
                    source_file = self.find_source_file(test_case_path, lang_config)
                if not source_file:
                    return {'success': False, 'error': f'No source file found'}
                run_cmd = lang_config['run_command'].format(file_path=source_file)

            # 使用 Popen 以便更好地控制超时
            timeout = self.suite_config.get('timeout_seconds', 60)
            process = subprocess.Popen(
                run_cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            try:
                stdout, stderr = process.communicate(timeout=timeout)
                execution_time = time.time() - start_time
                end_memory = self.get_memory_usage()

                return {
                    'success': process.returncode == 0,
                    'execution_time': execution_time,
                    'memory_used': end_memory - start_memory,
                    'stdout': stdout,
                    'stderr': stderr,
                    'return_code': process.returncode
                }
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
                return {'success': False, 'error': 'timeout'}
        except Exception as e:
            return {'success': False, 'error': f'{str(e)}'}

    def analyze_results(self, results):
        successful_runs = [r for r in results if r['success']]

        if not successful_runs:
            return {
                'success': False,
                'total_runs': len(results),
                'successful_runs': 0,
                'error': 'All runs failed',
                'failures': results[:3]  # 记录前几个失败信息
            }

        return {
            'success': True,
            'total_runs': len(results),
            'successful_runs': len(successful_runs),
            'average_time': statistics.mean([r['execution_time'] for r in successful_runs]),
            'min_time': min([r['execution_time'] for r in successful_runs]),
            'max_time': max([r['execution_time'] for r in successful_runs]),
            'std_dev_time': statistics.stdev([r['execution_time'] for r in successful_runs]) if len(successful_runs) > 1 else 0,
            'average_memory': statistics.mean([r['memory_used'] for r in successful_runs])
        }

    def get_memory_usage(self):
        # 简化版内存测量
        try:
            with open('/proc/self/status', 'r') as f:
                for line in f:
                    if line.startswith('VmRSS:'):
                        return int(line.split()[1]) * 1024  # KB to bytes
        except:
            pass
        return 0


def main():
    parser = argparse.ArgumentParser(description='Run language benchmarks')
    parser.add_argument('--language', required=True, help='Language to benchmark')
    parser.add_argument('--suite', required=True, help='Test suite name')
    args = parser.parse_args()

    # 加载语言配置
    with open(f'langs/{args.language}.yml', 'r') as f:
        lang_config = yaml.safe_load(f)

    # 加载测试套件配置
    suite_path = Path(f'benchmarks/{args.suite}')
    with open(suite_path / 'config.yaml', 'r') as f:
        suite_config = yaml.safe_load(f)

    # 运行测试
    runner = BenchmarkRunner({args.language: lang_config}, suite_config)
    result = runner.run_benchmark(suite_path, args.language)

    # 保存结果
    result['language'] = args.language
    result['suite'] = args.suite

    with open('result.json', 'w') as f:
        json.dump(result, f, indent=2)

    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

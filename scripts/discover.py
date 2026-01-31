# scripts/discover.py
import yaml
from pathlib import Path


def discover_benchmarks():
    benchmarks_dir = Path("./benchmarks")
    langs_dir = Path("./langs")

    # 读取所有语言配置
    languages = {}
    for lang_file in langs_dir.glob("*.y*"):
        if lang_file.suffix in ['.yaml', '.yml']:
            with open(lang_file, 'r') as f:
                lang_config = yaml.safe_load(f)
                lang_name = lang_file.stem
                languages[lang_name] = lang_config

    # 发现所有测试套件（每个测试套件目录本身就是一个测试）
    test_suites = {}
    for suite_dir in benchmarks_dir.iterdir():
        if suite_dir.is_dir():
            config_file = suite_dir / "config.yaml"
            if config_file.exists():
                with open(config_file, 'r') as f:
                    suite_config = yaml.safe_load(f)

                # 测试套件目录本身就是测试用例
                matched_langs = find_case_configs(suite_dir, languages)

                test_suites[suite_dir.name] = {
                    'config': suite_config,
                    'path': str(suite_dir),
                    'languages': matched_langs
                }

    return languages, test_suites


def find_case_configs(case_dir, languages):
    """为测试用例找到所有匹配的语言配置（可能有多个）"""
    matched_languages = []

    for file in case_dir.iterdir():
        if file.is_file():
            for lang_name, lang_config in languages.items():
                lang_ext = lang_config.get('file_extension', '')
                if file.suffix == lang_ext:
                    matched_languages.append(lang_name)

    # 去重
    return list(set(matched_languages))


if __name__ == '__main__':
    import json

    languages, test_suites = discover_benchmarks()

    # 生成测试矩阵
    matrix = []
    for suite_name, suite_data in test_suites.items():
        for language in suite_data['languages']:
            matrix.append({
                'language': language,
                'suite': suite_name
            })

    # 输出 JSON 矩阵
    print(json.dumps(matrix))

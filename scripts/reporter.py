# scripts/reporter.py
import json
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

def generate_report(results_dir):
    results = []
    failed_results = []
    # 递归查找所有 JSON 结果文件
    for result_file in Path(results_dir).rglob("*.json"):
        with open(result_file, 'r') as f:
            data = json.load(f)
            # 从文件名提取信息：raw-result-语言-套件/result.json
            filename = result_file.name
            parent_dir = result_file.parent.name

            # 如果文件名是 result.json，从父目录提取信息
            if filename == 'result.json':
                parts = parent_dir.split('-')
                if len(parts) >= 3:
                    # 格式: raw-result-language-suite
                    data['language'] = parts[2] if len(parts) > 2 else parts[0]
                    data['suite'] = '-'.join(parts[3:]) if len(parts) > 3 else parts[1]
                    data['test_case'] = data['suite']

                    if data.get('success', False) and data.get('successful_runs', 0) > 0:
                        results.append(data)
                    else:
                        failed_results.append(data)

    df = pd.DataFrame(results)
    failed_df = pd.DataFrame(failed_results)

    # 如果没有成功结果，跳过图表生成
    if len(df) > 0:
        generate_comparison_chart(df)
        generate_trend_chart(df)

    # 生成Markdown表格
    generate_results_table(df, failed_df)

    return df

def generate_comparison_chart(df):
    if len(df) == 0:
        return

    plt.figure(figsize=(12, 8))

    # 按测试用例分组，比较不同语言的性能
    test_cases = df['test_case'].unique()
    x = range(len(test_cases))
    width = 0.8 / len(df['language'].unique())

    for i, language in enumerate(df['language'].unique()):
        lang_data = df[df['language'] == language]
        values = [lang_data[lang_data['test_case'] == tc]['average_time'].values[0]
                  if len(lang_data[lang_data['test_case'] == tc]) > 0 else 0
                  for tc in test_cases]
        plt.bar([pos + i * width for pos in x], values, width, label=language)

    plt.xticks([pos + width for pos in x], test_cases, rotation=45, ha='right')
    plt.ylabel('执行时间(秒)')
    plt.title('各语言性能对比')
    plt.legend()
    plt.tight_layout()
    Path('report').mkdir(exist_ok=True)
    plt.savefig('report/comparison.png')
    plt.close()

def generate_trend_chart(df):
    if len(df) == 0:
        return

    plt.figure(figsize=(12, 8))

    # 按语言分组，展示在不同测试用例上的性能趋势
    for language in df['language'].unique():
        lang_data = df[df['language'] == language]
        sorted_data = lang_data.sort_values('test_case')
        plt.plot(sorted_data['test_case'], sorted_data['average_time'],
                marker='o', label=language)

    plt.xticks(rotation=45, ha='right')
    plt.ylabel('执行时间(秒)')
    plt.title('性能趋势图')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    Path('report').mkdir(exist_ok=True)
    plt.savefig('report/trend.png')
    plt.close()

def generate_results_table(df, failed_df):
    # 生成Markdown格式的结果表格
    Path('report').mkdir(exist_ok=True)

    with open('README.md', 'w') as f:
        f.write('# LangBench 测试报告\n\n')

        # 添加图表
        if len(df) > 0:
            f.write('## 性能图表\n\n')
            f.write('### 性能对比\n\n')
            f.write('![性能对比](report/comparison.png)\n\n')
            f.write('### 性能趋势\n\n')
            f.write('![性能趋势](report/trend.png)\n\n')

        # 按测试用例分组（仅成功的数据）
        if len(df) > 0:
            for test_case in df['test_case'].unique():
                f.write(f'## {test_case}\n\n')
                test_data = df[df['test_case'] == test_case]

                # 排序：按平均时间升序
                test_data = test_data.sort_values('average_time')

                f.write('| 语言 | 平均时间(s) | 最小时间(s) | 最大时间(s) | 标准差(s) | 成功率 |\n')
                f.write('|------|-------------|-------------|-------------|-----------|--------|\n')

                for _, row in test_data.iterrows():
                    success_rate = (row['successful_runs'] / row['total_runs']) * 100
                    f.write(f"| {row['language']} | {row['average_time']:.4f} | "
                           f"{row['min_time']:.4f} | {row['max_time']:.4f} | "
                           f"{row['std_dev_time']:.4f} | {success_rate:.1f}% |\n")

                f.write('\n')

            # 总结
            f.write('## 总结\n\n')
            for test_case in df['test_case'].unique():
                test_data = df[df['test_case'] == test_case]
                fastest = test_data.loc[test_data['average_time'].idxmin()]
                f.write(f"- **{test_case}**: 最快语言是 {fastest['language']} "
                       f"(平均 {fastest['average_time']:.4f}s)\n")
            f.write('\n')

        # 失败测试报告
        if len(failed_df) > 0 and 'test_case' in failed_df.columns:
            f.write('## 失败测试详情\n\n')

            # 按测试用例分组失败结果
            all_test_cases = set(df['test_case'].unique()) | set(failed_df['test_case'].unique())

            for test_case in all_test_cases:
                failed_test_data = failed_df[failed_df['test_case'] == test_case]

                if len(failed_test_data) > 0:
                    f.write(f'### {test_case} - 失败\n\n')

                    for _, row in failed_test_data.iterrows():
                        language = row.get('language', 'unknown')
                        error = row.get('error', 'unknown error')
                        f.write(f"#### {language}\n")
                        f.write(f"**错误信息**: `{error}`\n\n")

                        failures = row.get('failures')
                        if isinstance(failures, list) and failures:
                            f.write("**失败详情**:\n")
                            f.write("```\n")
                            for i, failure in enumerate(failures[:3], 1):
                                f.write(f"尝试 {i}: {failure.get('error', 'unknown')}\n")
                            f.write("```\n\n")

                        if row.get('total_runs', 0) > 0 and row.get('successful_runs', 0) == 0:
                            f.write(f"- 总运行次数: {row['total_runs']}\n")
                            f.write(f"- 成功次数: 0\n")
                            f.write(f"- 失败率: 100%\n\n")

                    f.write('---\n\n')
        else:
            f.write('## 失败测试\n\n')
            f.write('✅ 所有测试均通过！\n\n')

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Generate benchmark reports')
    parser.add_argument('--results-dir', default='.', help='Directory containing result JSON files')
    args = parser.parse_args()

    df = generate_report(args.results_dir)
    print(f"Report generated successfully. Processed {len(df)} results.")

if __name__ == '__main__':
    main()
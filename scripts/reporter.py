# scripts/reporter.py
import json
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

def format_time(seconds, decimals=4):
    """根据时间大小自动选择合适的单位"""
    if seconds >= 1:
        return f"{seconds:.{decimals}f}s"
    elif seconds >= 0.001:
        return f"{seconds * 1000:.{decimals}f}ms"
    else:
        return f"{seconds * 1000000:.{decimals}f}μs"

def generate_report(results_dir):
    results = []
    failed_results = []
    # 递归查找所有 JSON 结果文件
    for result_file in Path(results_dir).rglob("*.json"):
        with open(result_file, 'r') as f:
            data = json.load(f)

            # 尝试从数据本身获取信息（runner.py 已经添加了 language 和 suite）
            if 'language' in data and 'suite' in data:
                data['test_case'] = data['suite']

                if data.get('success', False) and data.get('successful_runs', 0) > 0:
                    results.append(data)
                else:
                    failed_results.append(data)

    df = pd.DataFrame(results)
    failed_df = pd.DataFrame(failed_results)

    print(f"Found {len(results)} successful results, {len(failed_results)} failed results")

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
        if len(df) > 0 and 'test_case' in df.columns:
            f.write('## 性能图表\n\n')
            f.write('### 性能对比\n\n')
            f.write('![性能对比](report/comparison.png)\n\n')
            f.write('### 性能趋势\n\n')
            f.write('![性能趋势](report/trend.png)\n\n')

        # 按测试用例分组（仅成功的数据）
        if len(df) > 0 and 'test_case' in df.columns:
            # 确定时间单位（根据最小值）
            min_time = df['average_time'].min()
            unit = 's'
            decimals = 4
            if min_time < 1:
                unit = 'ms'
                decimals = 3
            if min_time < 0.001:
                unit = 'μs'
                decimals = 1

            for test_case in df['test_case'].unique():
                f.write(f'## {test_case}\n\n')
                test_data = df[df['test_case'] == test_case]

                # 排序：按平均时间升序
                test_data = test_data.sort_values('average_time')

                f.write(f'| 语言 | 平均时间({unit}) | 最小时间({unit}) | 最大时间({unit}) | 标准差({unit}) | 成功率 |\n')
                f.write('|------|------------------|------------------|------------------|-----------------|--------|\n')

                for _, row in test_data.iterrows():
                    success_rate = (row['successful_runs'] / row['total_runs']) * 100
                    # 根据单位转换时间值
                    if unit == 's':
                        avg_str = f"{row['average_time']:.{decimals}f}"
                        min_str = f"{row['min_time']:.{decimals}f}"
                        max_str = f"{row['max_time']:.{decimals}f}"
                        std_str = f"{row['std_dev_time']:.{decimals}f}"
                    elif unit == 'ms':
                        avg_str = f"{row['average_time'] * 1000:.{decimals}f}"
                        min_str = f"{row['min_time'] * 1000:.{decimals}f}"
                        max_str = f"{row['max_time'] * 1000:.{decimals}f}"
                        std_str = f"{row['std_dev_time'] * 1000:.{decimals}f}"
                    else:  # μs
                        avg_str = f"{row['average_time'] * 1000000:.{decimals}f}"
                        min_str = f"{row['min_time'] * 1000000:.{decimals}f}"
                        max_str = f"{row['max_time'] * 1000000:.{decimals}f}"
                        std_str = f"{row['std_dev_time'] * 1000000:.{decimals}f}"

                    f.write(f"| {row['language']} | {avg_str} | {min_str} | {max_str} | {std_str} | {success_rate:.1f}% |\n")

                f.write('\n')

            # 总结
            f.write('## 总结\n\n')
            for test_case in df['test_case'].unique():
                test_data = df[df['test_case'] == test_case]
                fastest = test_data.loc[test_data['average_time'].idxmin()]
                f.write(f"- **{test_case}**: 最快语言是 {fastest['language']} "
                       f"(平均 {format_time(fastest['average_time'])})\n")
            f.write('\n')

        # 失败测试报告
        if len(failed_df) > 0 and 'test_case' in failed_df.columns:
            failed_test_cases = set(failed_df['test_case'].unique())
            if len(failed_test_cases) > 0:
                f.write('## 失败测试详情\n\n')

                # 按测试用例分组失败结果
                df_test_cases = set(df['test_case'].unique()) if 'test_case' in df.columns else set()
                all_test_cases = df_test_cases | failed_test_cases

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
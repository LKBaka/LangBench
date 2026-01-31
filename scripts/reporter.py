# scripts/reporter.py
import json
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

def generate_report(results_dir):
    results = []
    for result_file in Path(results_dir).glob("*.json"):
        with open(result_file, 'r') as f:
            data = json.load(f)
            # 提取文件名信息：语言-套件-用例
            parts = result_file.stem.split('-')
            if len(parts) >= 3:
                data['language'] = parts[0]
                data['suite'] = parts[1]
                data['test_case'] = '-'.join(parts[2:])
                results.append(data)
    
    df = pd.DataFrame(results)
    
    # 生成对比图表
    generate_comparison_chart(df)
    generate_trend_chart(df)
    
    # 生成Markdown表格
    generate_results_table(df)
    
    return df

def generate_comparison_chart(df):
    plt.figure(figsize=(12, 8))
    
    # 按语言和测试套件分组展示
    for language in df['language'].unique():
        lang_data = df[df['language'] == language]
        plt.bar(lang_data['test_case'], lang_data['average_time'], label=language)
    
    plt.xticks(rotation=45)
    plt.ylabel('执行时间(秒)')
    plt.title('各语言性能对比')
    plt.legend()
    plt.tight_layout()
    plt.savefig('report/comparison.png')
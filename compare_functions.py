#!/usr/bin/env python3
"""
比对 _函数汇总.md 和 functionlist.md 的函数列表
"""
import re
from pathlib import Path

def extract_functions_from_summary(filepath):
    """从 _函数汇总.md 提取函数名"""
    functions = set()
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            # 匹配类似: - [funcName](funcName/)
            match = re.search(r'- \[([^\]]+)\]\([^)]*\)', line)
            if match:
                func_name = match.group(1)
                functions.add(func_name)
    return functions

def extract_functions_from_list(filepath):
    """从 functionlist.md 提取函数名"""
    functions = set()
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                # 去掉 dip:: 前缀
                if line.startswith('dip::'):
                    line = line[5:]
                functions.add(line)
    return functions

def compare_functions():
    summary_file = Path("文档检查/functions/_函数汇总.md")
    list_file = Path("文档检查/functions/functionlist.md")
    
    summary_funcs = extract_functions_from_summary(summary_file)
    list_funcs = extract_functions_from_list(list_file)
    
    print("=" * 60)
    print("函数列表比对结果")
    print("=" * 60)
    print(f"\n_函数汇总.md 中的函数数量: {len(summary_funcs)}")
    print(f"functionlist.md 中的函数数量: {len(list_funcs)}")
    
    # 在汇总里有但 functionlist 里没有（多的）
    extra_in_summary = summary_funcs - list_funcs
    # 在 functionlist 里有但汇总里没有（缺失的）
    missing_in_summary = list_funcs - summary_funcs
    
    print("\n" + "=" * 60)
    print(f"[在 _函数汇总.md 中多出的函数] ({len(extra_in_summary)} 个)")
    print("=" * 60)
    if extra_in_summary:
        for func in sorted(extra_in_summary):
            print(f"  - {func}")
    else:
        print("  无")
    
    print("\n" + "=" * 60)
    print(f"[在 _函数汇总.md 中缺失的函数] ({len(missing_in_summary)} 个)")
    print("=" * 60)
    if missing_in_summary:
        for func in sorted(missing_in_summary):
            print(f"  - {func}")
    else:
        print("  无")
    
    # 保存结果到文件
    result_file = Path("文档检查/functions/_函数比对结果.md")
    with open(result_file, 'w', encoding='utf-8') as f:
        f.write("# 函数列表比对结果\n\n")
        f.write(f"- **_函数汇总.md** 中的函数数量: {len(summary_funcs)}\n")
        f.write(f"- **functionlist.md** 中的函数数量: {len(list_funcs)}\n\n")
        
        f.write(f"## 在 _函数汇总.md 中多出的函数 ({len(extra_in_summary)} 个)\n\n")
        if extra_in_summary:
            for func in sorted(extra_in_summary):
                f.write(f"- {func}\n")
        else:
            f.write("无\n")
        
        f.write(f"\n## 在 _函数汇总.md 中缺失的函数 ({len(missing_in_summary)} 个)\n\n")
        if missing_in_summary:
            for func in sorted(missing_in_summary):
                f.write(f"- {func}\n")
        else:
            f.write("无\n")
    
    print(f"\n[结果已保存到] {result_file}")

if __name__ == "__main__":
    compare_functions()

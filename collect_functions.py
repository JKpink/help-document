#!/usr/bin/env python3
"""
收集文档检查中的函数文件夹到 functions 文件夹
复制整个文件夹结构，而不仅仅是 .md 文件
"""
import os
import shutil
from pathlib import Path

# 源目录（文档检查）
SOURCE_DIR = Path("文档检查")
# 目标目录（functions）
TARGET_DIR = SOURCE_DIR / "functions"

def collect_functions():
    """收集所有函数文件夹到 functions 文件夹"""
    
    # 确保目标目录存在
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    
    # 跳过的目录
    skip_dirs = {'.git', 'functions', '__pycache__', '.DS_Store'}
    
    collected = []
    conflicts = []
    
    print("开始收集函数文件夹...")
    print("=" * 60)
    
    # 遍历所有子目录（作者目录）
    for author_dir in sorted(SOURCE_DIR.iterdir()):
        if not author_dir.is_dir() or author_dir.name in skip_dirs:
            continue
        
        author = author_dir.name
        print(f"\n[作者] {author}")
        
        # 查找该作者目录下的所有函数文件夹
        # 函数文件夹定义：包含 .md 文件的文件夹（不包括 mathjax 和 .git 等）
        func_dirs = []
        for item in author_dir.rglob("*"):
            if item.is_dir() and item.name not in skip_dirs and "mathjax" not in item.name.lower():
                # 检查是否包含 .md 文件（排除 README.md）
                md_files = [f for f in item.glob("*.md") 
                           if f.name != "README.md" and not f.name.startswith("~$")]
                if md_files:
                    func_dirs.append(item)
        
        if not func_dirs:
            print(f"   没有找到函数文件夹")
            continue
        
        # 去重：只保留最顶层的函数文件夹
        # 例如：如果同时有 affinetform2d/ 和 affinetform2d/mathjax/，只保留前者
        func_dirs = sorted(set(func_dirs))
        filtered_dirs = []
        for d in sorted(func_dirs, key=lambda x: len(x.parts)):
            # 检查是否已经被包含在其他文件夹中
            is_subdir = False
            for existing in filtered_dirs:
                try:
                    d.relative_to(existing)
                    is_subdir = True
                    break
                except ValueError:
                    pass
            if not is_subdir:
                filtered_dirs.append(d)
        
        func_dirs = filtered_dirs
        
        for func_dir in sorted(func_dirs):
            func_name = func_dir.name
            
            # 目标路径
            target_func_dir = TARGET_DIR / func_name
            
            # 检查是否已存在
            if target_func_dir.exists():
                # 冲突，添加作者前缀
                target_func_dir = TARGET_DIR / f"{func_name}_{author}"
                conflicts.append((func_name, author))
            
            try:
                # 复制整个文件夹
                shutil.copytree(func_dir, target_func_dir)
                collected.append({
                    'author': author,
                    'func_name': func_name,
                    'source': func_dir,
                    'target': target_func_dir
                })
                print(f"   [OK] {func_name}")
            except Exception as e:
                print(f"   [FAIL] {func_name} - 错误: {e}")
    
    print("\n" + "=" * 60)
    print(f"\n收集完成!")
    print(f"总共收集: {len(collected)} 个函数文件夹")
    print(f"目标目录: {TARGET_DIR.resolve()}")
    
    if conflicts:
        print(f"\n[警告] 发现 {len(conflicts)} 个重名函数，已添加作者后缀:")
        for func_name, author in conflicts:
            print(f"   - {func_name} ({author})")
    
    # 生成汇总文件
    generate_summary(collected)
    
    return collected

def generate_summary(collected):
    """生成汇总文件"""
    summary_file = TARGET_DIR / "_函数汇总.md"
    
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write("# 函数文档汇总\n\n")
        f.write(f"共收集 **{len(collected)}** 个函数文件夹\n\n")
        
        # 按作者分组
        by_author = {}
        for item in collected:
            author = item['author']
            if author not in by_author:
                by_author[author] = []
            by_author[author].append(item['func_name'])
        
        for author in sorted(by_author.keys()):
            f.write(f"\n## {author} ({len(by_author[author])}个)\n\n")
            for func_name in sorted(by_author[author]):
                f.write(f"- [{func_name}]({func_name}/)\n")
    
    print(f"\n[汇总] 汇总文件已生成: {summary_file}")

if __name__ == "__main__":
    collect_functions()

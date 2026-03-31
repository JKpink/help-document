import os
import markdown
import shutil
from pathlib import Path

# MathJax 源目录路径（默认使用 node_modules 中的 MathJax）
# 可以修改此路径指向你的 MathJax 安装位置
MATHJAX_SOURCE_DIR = Path("node_modules/mathjax")

# MathJax 入口文件（在源目录中的相对路径）
MATHJAX_ENTRY_FILE = "es5/tex-mml-chtml.js"

def find_mathjax_source():
    """查找 MathJax 源目录"""
    # 检查配置的源目录
    if MATHJAX_SOURCE_DIR.exists():
        return MATHJAX_SOURCE_DIR
    
    # 尝试其他常见位置
    alternative_paths = [
        Path("mathjax"),
        Path("MathJax"),
        Path("../mathjax"),
        Path("../../mathjax"),
    ]
    
    for path in alternative_paths:
        if path.exists():
            return path
    
    return None

CSS_STYLE = """
/* GitHub stylesheet for MarkdownPad (http://markdownpad.com) */
/* Author: Nicolas Hery - http://nicolashery.com */
/* Version: b13fe65ca28d2e568c6ed5d7f06581183df8f2ff */
/* Source: https://github.com/nicolahery/markdownpad-github */

/* RESET
=============================================================================*/

html, body, div, span, applet, object, iframe, h1, h2, h3, h4, h5, h6, p, blockquote, pre, a, abbr, acronym, address, big, cite, code, del, dfn, em, img, ins, kbd, q, s, samp, small, strike, strong, sub, sup, tt, var, b, u, i, center, dl, dt, dd, ol, ul, li, fieldset, form, label, legend, table, caption, tbody, tfoot, thead, tr, th, td, article, aside, canvas, details, embed, figure, figcaption, footer, header, hgroup, menu, nav, output, ruby, section, summary, time, mark, audio, video {
  margin: 0;
  padding: 0;
  border: 0;
}

/* BODY
=============================================================================*/

body {
  font-family: "Times New Roman", "宋体", arial, freesans, clean, sans-serif;
  font-size: 14px;
  line-height: 1.6;
  color: #333;
  background-color: #fff;
  padding: 20px;
  max-width: 960px;
  margin: 0 auto;
}

body>*:first-child {
  margin-top: 0 !important;
}

body>*:last-child {
  margin-bottom: 0 !important;
}

/* BLOCKS
=============================================================================*/

p, blockquote, ul, ol, dl, table, pre {
  margin: 15px 0;
}

/* HEADERS
=============================================================================*/

h1, h2, h3, h4, h5, h6 {
  margin: 20px 0 10px;
  padding: 0;
  font-weight: bold;
  -webkit-font-smoothing: antialiased;
}

h1 tt, h1 code, h2 tt, h2 code, h3 tt, h3 code, h4 tt, h4 code, h5 tt, h5 code, h6 tt, h6 code {
  font-size: inherit;
}

h1 {
  font-size: 28px;
  color: #000;
}

h2 {
  font-size: 24px;
  border-bottom: 1px solid #ccc;
  color: #000;
}

h3 {
  font-size: 18px;
}

h4 {
  font-size: 16px;
}

h5 {
  font-size: 14px;
}

h6 {
  color: #777;
  font-size: 14px;
}

body>h2:first-child, body>h1:first-child, body>h1:first-child+h2, body>h3:first-child, body>h4:first-child, body>h5:first-child, body>h6:first-child {
  margin-top: 0;
  padding-top: 0;
}

a:first-child h1, a:first-child h2, a:first-child h3, a:first-child h4, a:first-child h5, a:first-child h6 {
  margin-top: 0;
  padding-top: 0;
}

h1+p, h2+p, h3+p, h4+p, h5+p, h6+p {
  margin-top: 10px;
}

/* LINKS
=============================================================================*/

a {
  color: #4183C4;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

/* LISTS
=============================================================================*/

ul, ol {
  padding-left: 30px;
}

ul li > :first-child, 
ol li > :first-child, 
ul li ul:first-of-type, 
ol li ol:first-of-type, 
ul li ol:first-of-type, 
ol li ul:first-of-type {
  margin-top: 0px;
}

ul ul, ul ol, ol ol, ol ul {
  margin-bottom: 0;
}

dl {
  padding: 0;
}

dl dt {
  font-size: 14px;
  font-weight: bold;
  font-style: italic;
  padding: 0;
  margin: 15px 0 5px;
}

dl dt:first-child {
  padding: 0;
}

dl dt>:first-child {
  margin-top: 0px;
}

dl dt>:last-child {
  margin-bottom: 0px;
}

dl dd {
  margin: 0 0 15px;
  padding: 0 15px;
}

dl dd>:first-child {
  margin-top: 0px;
}

dl dd>:last-child {
  margin-bottom: 0px;
}

/* CODE
=============================================================================*/

pre, code, tt {
  font-size: 12px;
  font-family: Consolas, "Liberation Mono", Courier, monospace;
}

code, tt {
  margin: 0 0px;
  padding: 0px 0px;
  white-space: nowrap;
  border: 1px solid #eaeaea;
  background-color: #f8f8f8;
  border-radius: 3px;
}

pre>code {
  margin: 0;
  padding: 0;
  white-space: pre;
  border: none;
  background: transparent;
}

pre {
  background-color: #f8f8f8;
  border: 1px solid #ccc;
  font-size: 13px;
  line-height: 19px;
  overflow: auto;
  padding: 6px 10px;
  border-radius: 3px;
}

pre code, pre tt {
  background-color: transparent;
  border: none;
}

kbd {
    -moz-border-bottom-colors: none;
    -moz-border-left-colors: none;
    -moz-border-right-colors: none;
    -moz-border-top-colors: none;
    background-color: #DDDDDD;
    background-image: linear-gradient(#F1F1F1, #DDDDDD);
    background-repeat: repeat-x;
    border-color: #DDDDDD #CCCCCC #CCCCCC #DDDDDD;
    border-image: none;
    border-radius: 2px 2px 2px 2px;
    border-style: solid;
    border-width: 1px;
    font-family: "Helvetica Neue",Helvetica,Arial,sans-serif;
    line-height: 10px;
    padding: 1px 4px;
}

/* QUOTES
=============================================================================*/

blockquote {
  border-left: 4px solid #DDD;
  padding: 0 15px;
  color: #777;
}

blockquote>:first-child {
  margin-top: 0px;
}

blockquote>:last-child {
  margin-bottom: 0px;
}

/* HORIZONTAL RULES
=============================================================================*/

hr {
  clear: both;
  margin: 15px 0;
  height: 0px;
  overflow: hidden;
  border: none;
  background: transparent;
  border-bottom: 4px solid #ddd;
  padding: 0;
}

/* TABLES
=============================================================================*/

table th {
  font-weight: bold;
}

table th, table td {
  border: 1px solid #ccc;
  padding: 6px 13px;
}

table tr {
  border-top: 1px solid #ccc;
  background-color: #fff;
}

table tr:nth-child(2n) {
  background-color: #f8f8f8;
}

/* IMAGES
=============================================================================*/

img {
  max-width: 100%
}
"""


def copy_mathjax_if_needed(html_dir, has_latex):
    """
    如果需要，复制整个 MathJax 目录到 HTML 所在目录
    
    Args:
        html_dir: HTML 文件所在目录
        has_latex: 是否包含 LaTeX 公式
    
    Returns:
        bool: 是否成功复制（或不需要复制）
    """
    if not has_latex:
        return True  # 不需要复制
    
    mathjax_source = find_mathjax_source()
    if not mathjax_source:
        print(f"  警告: 找不到 MathJax 源目录，跳过复制")
        print(f"  请确保 MATHJAX_SOURCE_DIR 指向正确的 MathJax 安装目录")
        return False
    
    target_dir = Path(html_dir) / "mathjax"
    
    # 如果目标目录已存在，不需要重复复制
    if target_dir.exists():
        return True
    
    try:
        print(f"  正在复制 MathJax 目录...")
        shutil.copytree(mathjax_source, target_dir)
        print(f"  已复制 MathJax 到: {target_dir}")
        return True
    except Exception as e:
        print(f"  错误: 复制 MathJax 失败: {e}")
        return False


def contains_latex(html_content):
    """检查 HTML 内容中是否包含 LaTeX 公式"""
    return '<script type="math/tex' in html_content


def generate_mathjax_script(mathjax_path, has_latex):
    """生成 MathJax 脚本，如果没有公式则返回空字符串"""
    if not has_latex:
        return ""
    
    return f"""
<script>
MathJax = {{
    tex: {{
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
        processEscapes: true,
        processEnvironments: true
    }},
    startup: {{
        ready: () => {{
            // 先处理 python-markdown-math 生成的 script 标签
            const scripts = document.querySelectorAll('script[type^="math/tex"]');
            scripts.forEach(script => {{
                const isDisplay = script.type.includes('mode=display');
                const tex = script.textContent.trim();
                // 用 $$ 或 $ 包裹公式，让 MathJax 正常识别
                const wrappedTex = isDisplay ? '$$' + tex + '$$' : '$' + tex + '$';
                const span = document.createElement('span');
                span.textContent = wrappedTex;
                script.parentNode.replaceChild(span, script);
            }});
            // 然后运行默认的 MathJax 处理流程
            MathJax.startup.defaultReady();
        }}
    }}
}};
</script>
<script id="MathJax-script" async src="{mathjax_path}"></script>
"""


def md2html(md_file_path):
    with open(md_file_path, "r", encoding="utf-8") as md_file:
        md_content = md_file.read()
    html_content = markdown.markdown(
        md_content, extensions=["fenced_code", "tables", "mdx_math"]
    )
    
    # 检查是否包含 LaTeX 公式
    has_latex = contains_latex(html_content)
    
    # 获取 HTML 文件所在目录
    html_dir = Path(md_file_path).parent
    
    # 如果需要，复制 MathJax 目录
    copy_mathjax_if_needed(html_dir, has_latex)
    
    # MathJax 路径（相对于 HTML 文件）
    mathjax_path = "./mathjax/" + MATHJAX_ENTRY_FILE
    
    # 生成 MathJax 脚本（如果没有公式则为空）
    mathjax_script = generate_mathjax_script(mathjax_path, has_latex)
    
    html_document = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>{Path(md_file_path).stem}</title>
    <style>
        {CSS_STYLE}
    </style>
    {mathjax_script}
</head>
<body>
    {html_content}
</body>
</html>
"""

    html_file_path = md_file_path.replace(".md", ".html")
    with open(html_file_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_document)

    return html_file_path, has_latex


def batch_convert_md_to_html(root_dir):
    converted = 0
    skipped = 0
    errors = []
    latex_files = []  # 记录包含公式的文件

    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".md"):
                md_file_path = os.path.join(foldername, filename)
                html_file_path = md_file_path.replace(".md", ".html")
                if os.path.exists(html_file_path):

                    # skipped += 1
                    # continue

                    # 删掉已存在的 HTML 文件，确保每次都是全新转换
                    os.remove(html_file_path)

                try:
                    result_path, has_latex = md2html(md_file_path)
                    latex_status = "[含公式]" if has_latex else ""
                    print(f"转换成功: {md_file_path} -> {result_path} {latex_status}")
                    converted += 1
                    if has_latex:
                        latex_files.append(result_path)
                except Exception as e:
                    errors.append((md_file_path, str(e)))
                    print(f"转换失败: {md_file_path} - {str(e)}")

    print("\n" + "="*50)
    print("转换完成!")
    print(f"总文件数: {converted + skipped + len(errors)}")
    print(f"成功转换: {converted}")
    print(f"跳过文件: {skipped}")
    print(f"失败文件: {len(errors)}")
    
    if latex_files:
        print(f"\n包含 LaTeX 公式的文件 ({len(latex_files)} 个):")
        for f in latex_files:
            print(f"  - {f}")

    if errors:
        print("\n错误详情:")
        for file_path, error in errors:
            print(f"- {file_path}: {error}")


if __name__ == "__main__":
    root_directory = ""
    if not os.path.exists(root_directory):
        print(f"错误: 目录 '{root_directory}' 不存在")
        exit(1)

    print(f"开始批量转换Markdown文件 (根目录: {root_directory})...")
    batch_convert_md_to_html(root_directory)

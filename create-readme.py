import os
from urllib.parse import quote

def build_html_list(root_dir):
    html_lines = ['<ul>']
    build_list_recursive(root_dir, html_lines, root_dir)
    html_lines.append('</ul>')
    return html_lines

def build_list_recursive(current_path, html_lines, root_dir):
    entries = sorted(os.listdir(current_path))
    dirs = [e for e in entries if os.path.isdir(os.path.join(current_path, e)) and not e.startswith('.') and e not in 'Changes']
    md_files = [e for e in entries if e.endswith('.md')]

    for d in dirs:
        html_lines.append(f'<li><strong>📁 {d}/</strong><ul>')
        build_list_recursive(os.path.join(current_path, d), html_lines, root_dir)
        html_lines.append('</ul></li>')

    for f in md_files:
        full_path = os.path.join(current_path, f)
        rel_path = os.path.relpath(full_path, root_dir).replace("\\", "/")
        encoded_path = quote(rel_path)
        html_lines.append(f'<li><a href="{encoded_path}">{f}</a></li>')

def write_readme(readme_path, html_lines):
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write('# Markdown File Tree\n\n')
        f.write('\n'.join(html_lines))
        f.write('\n')

if __name__ == '__main__':
    root_dir = os.path.abspath('.')
    readme_path = os.path.join(root_dir, 'README.md')
    html_lines = build_html_list(root_dir)
    write_readme(readme_path, html_lines)
    print("README.md generated using <ul>/<li> HTML structure.")

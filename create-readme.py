import os
from urllib.parse import quote

def load_untracked_file_set(filepath):
    """Load untracked files into a set for quick lookup."""
    untracked = list()
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    # Normalize path slashes for consistency
                    untracked.append(line.replace("\\", "/"))
    return untracked

def build_html_list(root_dir, untracked_files):
    html_lines = ['<ul>']
    build_list_recursive(root_dir, html_lines, root_dir, untracked_files)
    html_lines.append('</ul>')
    return html_lines

def build_list_recursive(current_path, html_lines, root_dir, untracked_files):
    entries = sorted(os.listdir(current_path))
    dirs = [e for e in entries if os.path.isdir(os.path.join(current_path, e)) and not e.startswith('.')]
    md_files = [
        e for e in entries 
        if e.endswith('.md') and 
        os.path.isfile(os.path.join(current_path, e))
    ]

    for d in dirs:
        html_lines.append(f'<li><strong>📁 {d}/</strong><ul>')
        build_list_recursive(os.path.join(current_path, d), html_lines, root_dir, untracked_files)
        html_lines.append('</ul></li>')

    for f in md_files:
        full_path = os.path.join(current_path, f)
        rel_path = os.path.relpath(full_path, root_dir).replace("\\", "/")
        if rel_path in untracked_files:
            print(f"Skipping untracked file: {rel_path}")
            continue  # Skip untracked files
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
    untracked_file_path = os.path.join(root_dir, 'untracked-files.txt')

    untracked_files = load_untracked_file_set(untracked_file_path)
    html_lines = build_html_list(root_dir, untracked_files)
    write_readme(readme_path, html_lines)

    print("README.md generated — untracked .md files skipped.")

import os
from urllib.parse import quote

def load_untracked_set(filepath):
    """Load untracked files and directories into a set."""
    untracked = set()
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip().replace('\\', '/')
                if line:
                    untracked.add(line.rstrip('/'))
    return untracked

def is_excluded(path, untracked_set):
    """Return True if the path is an untracked file or inside an untracked directory."""
    path = path.replace('\\', '/')
    for entry in untracked_set:
        if path == entry or path.startswith(f"{entry}/"):
            return True
    return False

def has_tracked_md_files(dir_path, root_dir, untracked_set):
    """Return True if the directory contains any tracked .md files (recursively)."""
    for root, dirs, files in os.walk(dir_path):
        rel_root = os.path.relpath(root, root_dir).replace("\\", "/")
        if is_excluded(rel_root, untracked_set):
            dirs.clear()  # don't descend into excluded dirs
            continue
        for file in files:
            if file.endswith('.md'):
                rel_file = os.path.relpath(os.path.join(root, file), root_dir).replace("\\", "/")
                if not is_excluded(rel_file, untracked_set):
                    return True
    return False

def build_html_list(root_dir, untracked):
    html_lines = ['<ul>']
    build_list_recursive(root_dir, html_lines, root_dir, untracked)
    html_lines.append('</ul>')
    return html_lines

def build_list_recursive(current_path, html_lines, root_dir, untracked):
    entries = sorted(os.listdir(current_path))
    dirs = [e for e in entries if os.path.isdir(os.path.join(current_path, e)) and not e.startswith('.')]
    md_files = [e for e in entries if e.endswith('.md') and os.path.isfile(os.path.join(current_path, e))]

    # Filter out directories that are untracked or contain no tracked .md files
    filtered_dirs = []
    for d in dirs:
        full_dir_path = os.path.relpath(os.path.join(current_path, d), root_dir).replace("\\", "/")
        if is_excluded(full_dir_path, untracked):
            continue
        full_dir_abs = os.path.join(current_path, d)
        if has_tracked_md_files(full_dir_abs, root_dir, untracked):
            filtered_dirs.append(d)

    for d in filtered_dirs:
        html_lines.append(f'<li><strong>📁 {d}/</strong><ul>')
        build_list_recursive(os.path.join(current_path, d), html_lines, root_dir, untracked)
        html_lines.append('</ul></li>')

    for f in md_files:
        full_path = os.path.join(current_path, f)
        rel_path = os.path.relpath(full_path, root_dir).replace("\\", "/")
        if is_excluded(rel_path, untracked):
            continue
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

    untracked_set = load_untracked_set(untracked_file_path)
    html_lines = build_html_list(root_dir, untracked_set)
    write_readme(readme_path, html_lines)

    print("README.md generated — untracked and empty directories excluded.")

import os
from urllib.parse import quote

def build_tree(root_dir):
    tree_lines = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip hidden folders and .git
        dirnames[:] = [d for d in dirnames if not d.startswith('.') and d not in ['Changes', '.git']]
        
        level = dirpath.replace(root_dir, '').count(os.sep)
        indent = '  ' * level
        folder_name = os.path.basename(dirpath) or os.path.basename(os.path.abspath(root_dir))

        # Add folder name to tree (skip root)
        if level == 0:
            tree_lines.append(f'📁 {folder_name}/')
        else:
            tree_lines.append(f'{indent}📁 {folder_name}/')

        for f in sorted(filenames):
            if f.endswith('.md'):
                subindent = '  ' * (level + 1)
                rel_path = os.path.relpath(os.path.join(dirpath, f), root_dir).replace("\\", "/")
                encoded_path = quote(rel_path)
                tree_lines.append(f'{subindent}└── [{f}]({encoded_path})')

    return tree_lines

def write_readme(readme_path, tree_lines):
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write('# Markdown File Tree\n\n')
        f.write('\n'.join(tree_lines))
        f.write('\n')

if __name__ == '__main__':
    root_dir = os.path.abspath('.')
    readme_path = os.path.join(root_dir, 'README.md')
    tree_lines = build_tree(root_dir)
    write_readme(readme_path, tree_lines)
    print(f"README.md generated with linked .md files.")

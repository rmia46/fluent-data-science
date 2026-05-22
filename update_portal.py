import os
import json

def generate_tree():
    # Files/folders to strictly ignore
    ignore_list = [
        '.git', '.gitignore', '.github', 'generate_notebooks.py', 
        'update_plan.py', 'update_portal.py', 'portal', 
        '__pycache__', '.ipynb_checkpoints', 'README.md',
        'file_tree.json', 'tree_data.json', 'plan.htm'
    ]

    def path_to_dict(path):
        name = os.path.basename(path)
        d = {'name': name}
        if os.path.isdir(path):
            d['type'] = 'directory'
            # Sort children to keep modules in order (01, 02, etc)
            children = sorted(os.listdir(path))
            d['children'] = [path_to_dict(os.path.join(path, x)) for x in children if x not in ignore_list]
        else:
            d['type'] = 'file'
            # Make path relative to repo root for GitHub links
            d['path'] = os.path.relpath(path, start='.')
        return d

    print("[*] Scanning directory structure...")
    # Only scan the module folders (starting with 0)
    data = []
    root_dirs = sorted([d for d in os.listdir('.') if os.path.isdir(d) and d.startswith('0')])
    
    for d in root_dirs:
        data.append(path_to_dict(d))

    output_path = 'portal/tree_data.js'
    with open(output_path, 'w') as f:
        f.write('const FILE_TREE = ' + json.dumps(data, indent=2) + ';')
    
    print(f"[+] Successfully updated {output_path}")
    print("[!] Run 'git add . && git commit -m \"Update portal tree\" && git push' to apply changes.")

if __name__ == "__main__":
    generate_tree()

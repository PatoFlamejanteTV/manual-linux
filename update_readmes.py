import os

REPO_ROOT = '/home/quack/manual-linux'
BASE_DIR = os.path.join(REPO_ROOT, 'site')
SKIP_DIRS = {'.', '..', '.git', '_includes', '_layouts', '_site', '.jekyll-cache', 'assets', 'css', 'images', 'js', '.github'}

def get_submodules(repo_root):
    submodules = set()
    gitmodules_path = os.path.join(repo_root, '.gitmodules')
    if os.path.exists(gitmodules_path):
        with open(gitmodules_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('path = '):
                    # path = site/extras/foo
                    path = line.split('=', 1)[1].strip()
                    full_path = os.path.join(repo_root, path)
                    submodules.add(full_path)
    return submodules

SUBMODULES = get_submodules(REPO_ROOT)

def get_readme_path(dir_path):
    # Check for likely variants
    for name in ['README.md', 'readme.md', 'ReadMe.md']:
        p = os.path.join(dir_path, name)
        if os.path.exists(p):
            return p
    return os.path.join(dir_path, 'README.md')

def update_readme(dir_path):
    try:
        items = os.listdir(dir_path)
    except Exception as e:
        print(f"Error accessing {dir_path}: {e}")
        return

    files = []
    subdirs = []
    
    current_readme = get_readme_path(dir_path)
    
    for item in items:
        if item.startswith('.'): continue
        if item.lower() == 'readme.md': continue
        if item == 'index.md': continue
        
        full_path = os.path.join(dir_path, item)
        
        if os.path.isdir(full_path):
            if item not in SKIP_DIRS:
                subdirs.append(item)
        elif item.endswith('.md'):
            files.append(item)

    files.sort()
    subdirs.sort()

    title = f"# {os.path.basename(dir_path).capitalize()}"
    description = ""
    
    if os.path.exists(current_readme):
        with open(current_readme, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if lines:
                if lines[0].strip().startswith('# '):
                    title = lines[0].strip()
                
                desc_lines = []
                for line in lines[1:]:
                    l = line.strip()
                    # simplistic stop logic
                    if l.startswith('- ') or l.startswith('* ') or l.startswith('1. ') or (l.startswith('[') and '](' in l):
                        break
                    if l.startswith('## '):
                        break
                    desc_lines.append(line)
                description = "".join(desc_lines).strip()

    new_content = [title + "\n\n"]
    if description:
        new_content.append(description + "\n\n")

    for subdir in subdirs:
         new_content.append(f"- [/{subdir}]({subdir})\n")
    
    for file in files:
        name_no_ext = os.path.splitext(file)[0]
        new_content.append(f"- [{name_no_ext}]({name_no_ext})\n")
        
    with open(current_readme, 'w', encoding='utf-8') as f:
        f.writelines(new_content)
    print(f"Updated {current_readme}")

# Main walk
for root, dirs, files in os.walk(BASE_DIR):
    # Filter subdirectories to avoid recursing into submodules or skipped dirs
    dirs_to_keep = []
    for d in dirs:
        full_path = os.path.join(root, d)
        
        # If directory is in skip list, ignore
        if d.startswith('.') or d in SKIP_DIRS:
            continue
            
        # If directory is a submodule, ignore for recursion (but it stays in fs so it's listed in parent's readme via os.listdir)
        if full_path in SUBMODULES:
            continue
            
        dirs_to_keep.append(d)
    
    # Modify dirs in-place to control recursion
    dirs[:] = dirs_to_keep

    if root == BASE_DIR:
        # Don't update the root site/README.md automatically (unless user wants to, but typically root is special)
        # Previous logic skipped it.
        pass
    else:
        # Double check we are not in a submodule (shouldn't happen due to pruning)
        if root in SUBMODULES:
            continue
            
        dirname = os.path.basename(root)
        if dirname.startswith('.') or dirname in SKIP_DIRS:
            continue
            
        update_readme(root)

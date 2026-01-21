import yaml
import os
import sys

def verify_config():
    """
    Validate SEO-related settings in site/_config.yml.
    
    Performs these checks on the configuration file at 'site/_config.yml':
    - file exists and is readable
    - required plugins ['jekyll-sitemap', 'jekyll-seo-tag', 'jekyll-optional-front-matter'] are declared in `plugins`
    - `excerpt_separator` is set to "\n\n"
    - `defaults` contains an entry with `scope.path == ""` and `values.layout == "default"`
    - `url` property is present and truthy
    
    Returns:
        bool: `True` if all checks pass, `False` otherwise.
    """
    config_path = 'site/_config.yml'
    if not os.path.exists(config_path):
        print(f"ERROR: {config_path} not found.")
        return False

    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    required_plugins = [
        'jekyll-sitemap',
        'jekyll-seo-tag',
        'jekyll-optional-front-matter'
    ]

    plugins = config.get('plugins', [])
    missing_plugins = [p for p in required_plugins if p not in plugins]

    if missing_plugins:
        print(f"ERROR: Missing plugins: {missing_plugins}")
        return False

    if config.get('excerpt_separator') != "\n\n":
        print("ERROR: excerpt_separator is not set to '\\n\\n'")
        return False

    defaults = config.get('defaults', [])
    has_default_layout = False
    for entry in defaults:
        if entry.get('scope', {}).get('path') == "" and entry.get('values', {}).get('layout') == 'default':
            has_default_layout = True
            break

    if not has_default_layout:
        print("ERROR: Default layout 'default' is not set for all pages.")
        return False

    if not config.get('url'):
        print("ERROR: 'url' property is missing in _config.yml (required for SEO).")
        return False

    print("SUCCESS: SEO configuration is correct and automated.")
    return True

if __name__ == "__main__":
    if verify_config():
        sys.exit(0)
    else:
        sys.exit(1)
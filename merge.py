import os
from pathlib import Path

##############################################################################
# CONFIG
##############################################################################

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'scraped_docs')

ESSENTIALS = [
  # Docs
  'cadence_lang_org_docs_why',
  'developers_flow_com',

  # GitHub Repos
  'github_com_onflow_flow_core_contracts',
  'github_com_onflow_flow_ft',
  'github_com_onflow_flow_nft',
  'github_com_onflow_nft_storefront'
]

OUTPUT_DIR = os.path.join(BASE_DIR, 'merged_docs')

##############################################################################
# UTILS
##############################################################################

def ensure_dir_exists(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


def merge_md_files(src_path: str):
    """Merge all .md files in src_path into one file"""
    merged_content = []
    
    for root, _, files in os.walk(src_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    merged_content.append(f.read())
                    merged_content.append("\n\n\n\n\n---\n\n------------ FILE_DIVIDER ------------\n\n---\n\n\n\n\n")
    
    return ''.join(merged_content)

# Merge all docs
def merge_all_md_files(output_path: str):
    """Merge all .md files in DATA_DIR into one file"""
    merged_content = []
    
    for root, dirnames, _ in os.walk(DATA_DIR):
        for dir in dirnames:
            dir_path = os.path.join(root, dir)
            if not os.path.exists(dir_path):
                continue
            merged_content.append(merge_md_files(dir_path))
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(''.join(merged_content))

def merge_essentials_md_files(output_path: str):
    """Merge only .md files from ESSENTIALS folders"""
    merged_content = []
    
    for essential in ESSENTIALS:
        essential_dir = os.path.join(DATA_DIR, essential)
        if not os.path.exists(essential_dir):
            continue
        merged_content.append(merge_md_files(essential_dir))
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(''.join(merged_content))

##############################################################################
# MAIN
##############################################################################

def main():
    ensure_dir_exists(OUTPUT_DIR)
    
    # Merge essentials only
    essentials_output = os.path.join(OUTPUT_DIR, 'essentials_merged.md')
    merge_essentials_md_files(essentials_output)
    print(f"Merged essentials to: {essentials_output}")

    # Merge all files
    all_output = os.path.join(OUTPUT_DIR, 'all_merged.md')
    merge_all_md_files(all_output)
    print(f"Merged all docs to: {all_output}")

if __name__ == "__main__":
    main()

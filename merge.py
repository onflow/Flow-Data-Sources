import os
from pathlib import Path

##############################################################################
# CONFIG
##############################################################################

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'scraped_docs')

CADENCE_DOCS = [
    # GitHub Docs
    'github_com_onflow_cadence_lang_org',

    # Main Repos
    'github_com_onflow_flow_core_contracts',
    'github_com_onflow_flow_ft',
    'github_com_onflow_flow_nft',
    'github_com_onflow_nft_storefront',
    'github_com_onflow_flow_evm_bridge',
    'github_com_dapperlabs_nba_smart_contracts',
    'github_com_dapperlabs_nfl_smart_contracts',
    'github_com_outblock_frw_scripts',
    
    # Ecosystem Repos
    'github_com_ballerz_nft_ballerz',
    'github_com_dappcoderr_cadence_fun',
    'github_com_flowtyio_avataaars',
    'github_com_flowtyio_capability_cache',
    'github_com_flowtyio_fantastec',
    'github_com_flowtyio_flow_contracts',
    'github_com_flowtyio_flow_raffle',
    'github_com_flowtyio_flowty_drops',
    'github_com_flowtyio_flowty_wrapped',
    'github_com_flowtyio_fungible_token_router',
    'github_com_flowtyio_lost_and_found',
    'github_com_flowtyio_nft_catalog',
    'github_com_flowtyio_unblocked',
    'github_com_graffle_cadence_1_0_contracts',
    'github_com_incrementfi_liquid_staking',
    'github_com_incrementfi_money_market',
    'github_com_incrementfi_oracle',
    'github_com_incrementfi_swap',
    'github_com_itahand_coa_example',
    'github_com_itahand_cadence_arch_example',
    'github_com_austinkline_jimbo',
    'github_com_austinkline_managed_account',
    'github_com_blocto_bloctoswap_contracts',
    'github_com_blocto_blt_contracts',
    'github_com_blocto_flow_transactions',
    'github_com_blocto_revv_contracts',
    'github_com_bluesign_cadenceupgrader',
    'github_com_crash13override_flovatar',
    'github_com_dapperlabs_studio_platform_smart_contracts',
    'github_com_emerald_dao_emerald_academy_v2',
    'github_com_emerald_dao_emerald_id',
    'github_com_emerald_dao_float',
    'github_com_emerald_dao_project_toucans_v2',
    'github_com_fixes_world_token_list',
    'github_com_fixes_world_fixes',
    'github_com_onflow_bridged_usdc',
    'github_com_onflow_cadence',
    'github_com_onflow_flips',
    'github_com_onflow_nft_catalog',
    'github_com_onflow_random_coin_toss',
    'github_com_onflow_hybrid_custody',
]

# concat CADENCE_DOCS to ESSENTIALS
ESSENTIALS = [
  # Docs
  'developers_flow_com',
  'docs_wallet_flow_com',
] + CADENCE_DOCS

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

def merge_cadence_docs_md_files(output_path: str):
    """Merge only .md files from CADENCE_DOCS folders"""
    merged_content = []
    
    for cadence_doc in CADENCE_DOCS:
        cadence_doc_dir = os.path.join(DATA_DIR, cadence_doc)
        if not os.path.exists(cadence_doc_dir):
            continue
        merged_content.append(merge_md_files(cadence_doc_dir))
    
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

    # Merge cadence docs only
    cadence_docs_output = os.path.join(OUTPUT_DIR, 'cadence_docs_merged.md')
    merge_cadence_docs_md_files(cadence_docs_output)
    print(f"Merged cadence docs to: {cadence_docs_output}")

    # Merge all files
    all_output = os.path.join(OUTPUT_DIR, 'all_merged.md')
    merge_all_md_files(all_output)
    print(f"Merged all docs to: {all_output}")

if __name__ == "__main__":
    main()

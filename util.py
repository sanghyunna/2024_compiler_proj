import sys
import pandas as pd

def read_csv_file(target_file_dir):
    try:
        return pd.read_csv(target_file_dir)
    except FileNotFoundError:
        print(f"[{target_file_dir}] not found.")
    sys.exit()

def syntax_analyzer(target_string, action_df, goto_df):
    return None
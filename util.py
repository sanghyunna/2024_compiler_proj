import sys
import pandas as pd
from cfg import *

def read_csv_file(target_file_dir):
    try:
        return pd.read_csv(target_file_dir)
    except FileNotFoundError:
        print(f"[{target_file_dir}] not found.")
    sys.exit()

def next_input_symbol(target_token_list, curr_pointer):
    return target_token_list[curr_pointer]

def curr_state(state_stack):
    return state_stack[-1]

def syntax_analyzer(target_token_list, action_df, goto_df):
    ### SLR Parsing based on action, goto table
    cfg = get_cfg()
    curr_pointer = 0
    state_stack = [0]
    curr_token_list = target_token_list
    target_token_list.append("$")
    while True:
        decision = action_df.loc[curr_state(state_stack), next_input_symbol(target_token_list, curr_pointer)]
        if decision[0] == "s":
            state_stack.append(int(decision[1:]))
            curr_pointer += 1
        elif decision[0] == "r":
            rule_num = int(decision[1:])
            rule_dict = cfg[rule_num]
            
        elif decision == "acc":
            print("Accepted.")
            break
        else:
            print("Rejected.") # this rejection means that the input string is not in the language
            break




    return None
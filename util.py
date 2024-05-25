import sys
import pandas as pd
from cfg import *

def read_csv_file(target_file_dir):
    try:
        return pd.read_csv(target_file_dir)
    except FileNotFoundError:
        print(f"[{target_file_dir}] not found.")
    sys.exit()


def return_next_input_symbol(target_token_list, curr_pointer):
    return target_token_list[curr_pointer]

def curr_state(state_stack):
    return state_stack[-1]

def return_terminal_list(action_df):
    return action_df.head(0).columns.tolist()

## 현재 CFG의 terminal들의 List 반환
def is_in_terminal_list(terminal_list, next_input_symbol):
    if next_input_symbol in terminal_list:
        return True
    else:
        return False

def syntax_analyzer(target_token_list, action_df, goto_df):
    ### SLR Parsing based on action, goto table
    terminal_list = return_terminal_list(action_df)

    cfg = get_cfg() 
    curr_pointer = 0 
    state_stack = [0] 
    curr_token_list = target_token_list 
    target_token_list.append("$") 
    while True:

        next_input_symbol = return_next_input_symbol(target_token_list, curr_pointer)
        decision = action_df.loc[curr_state(state_stack), next_input_symbol]

        if decision[0] == "s":
            state_stack.append(int(decision[1:]))  
            curr_pointer += 1   
        elif decision[0] == "r": 
            rule_num = int(decision[1:]) 
            rule_dict = cfg[rule_num] 
            
        elif decision == "acc":
            print("Accepted.")
            break

        #reject 작업
        else:
            if decision == None:
                print("Rejected, invalid Grammar")
                #print(curr_token_list[curr_pointer:])
            elif not is_in_terminal_list(terminal_list, next_input_symbol):
                print("Rejected, invalid token")
                #print(curr_token_list[curr_pointer:])
            else:
                print("Rejected, undetermined Error")
                #print(curr_token_list[curr_pointer:])
            break
            #sys.exit()




    return None
import sys
import pandas as pd
from cfg import *

def read_csv_file(target_file_dir):
    try:
        return pd.read_csv(target_file_dir)
    except FileNotFoundError:
        print(f"[{target_file_dir}] not found.")
    sys.exit()

def next_input_symbol(rhs_list):
    return rhs_list[0]

def print_status(state_stack, lhs_list, rhs_list):
    print("--------------------")
    print(f"STATE_STACK: {state_stack}")
    print(f"LHS_list: {lhs_list}")
    print(f"RHS_list: {rhs_list}")

def advance_pointer(lhs_list, rhs_list):
    temp = rhs_list[0]
    lhs_list.append(temp)
    rhs_list.pop(0)

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

def get_tokens(input_file_dir):
    with open(input_file_dir, 'r') as f:
        return f.read().split()

def syntax_analyzer(target_token_list, action_df, goto_df):
    ### SLR Parsing based on action, goto table
    terminal_list = return_terminal_list(action_df)

    cfg = get_cfg() 
    state_stack = [0] # stack only contains state numbers. In other words, it only contains integers.
    target_token_list.append("$") 
    # 개발 편의를 위해 splitter를 사용하지 않고 lhs, rhs를 따로 저장
    lhs_list = []
    rhs_list = target_token_list.copy()
    
    while True:
        print_status(state_stack, lhs_list, rhs_list)
        
        decision = action_df.loc[curr_state(state_stack), next_input_symbol(rhs_list)]
        print(f"DECISION: {decision}")

        if decision[0] == "s":
            state_stack.append(int(decision[1:]))
            advance_pointer(lhs_list, rhs_list)

        elif decision[0] == "r": 
            rule_num = int(decision[1:]) 
            rule_dict = cfg[rule_num] 
            rule_left = key(rule_dict) # ex) E
            rule_right = val(rule_dict) # ex) ['id', '+', 'T']
            for _ in range(len(rule_right)):
                state_stack.pop()

            res = goto_df.loc[curr_state(state_stack), rule_left]
            if res == "nan":
                print("Rejected, no such field in GOTO table")
                break
            state_stack.append(int(float(res)))

            for i in range(len(rule_right)):
                lhs_list.pop()
            lhs_list.append(rule_left)



            
        elif decision == "acc":
            if len(lhs_list) == 1 and lhs_list[0] == "S'":
                print("Accepted.")
            else:
                print("Rejected, \'acc\' was reached but lhs_list is not empty.")
            break

        #reject 작업
        else:
            if not is_in_terminal_list(terminal_list, next_input_symbol(rhs_list)):
                print("Rejected, invalid token")

            elif decision == "nan":
                print("Rejected, invalid Grammar")
                # 개인적으로 이 부분은 invalid grammar가 아니라 invalid input 정도가 더 적당할 수 있을 것 같습니다!

            else:
                print("Rejected, undetermined Error")

            break
            #sys.exit()




    return None

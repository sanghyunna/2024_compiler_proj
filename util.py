import sys
import pandas as pd
from cfg import *

# CFG 파일 읽어오기
def read_csv_file(target_file_dir):
    try:
        return pd.read_csv(target_file_dir)
    except FileNotFoundError:
        print(f"[{target_file_dir}] not found.")
    sys.exit()

# 다음 input symbol 반환
def next_input_symbol(rhs_list):
    return rhs_list[0]

# 현재 상태 출력
def print_status(state_stack, lhs_list, rhs_list):
    print("--------------------")
    print(f"STATE_STACK: {state_stack}")
    print(f"LHS_list: {lhs_list}")
    print(f"RHS_list: {rhs_list}")

# Pointer 옮기는 함수
def advance_pointer(lhs_list, rhs_list):
    temp = rhs_list[0]
    lhs_list.append(temp)
    rhs_list.pop(0)

# 현재 state 반환
def curr_state(state_stack):
    return state_stack[-1]

## 현재 CFG의 terminal들의 List 반환, SLR table의 head(0)부분에는 terminal들이 있음.
def return_terminal_list(action_df):
    return action_df.head(0).columns.tolist()

## 현재 CFG의 terminal에 속하는지 반환. terminal_list를 이용해 next_input_symbol이 이 리스트안에 속하지 않으면 False를 반환
def is_in_terminal_list(terminal_list, next_input_symbol):
    if next_input_symbol in terminal_list:
        return True
    else:
        return False

# 토큰을 읽어와서 리스트로 반환
def get_tokens(input_file_dir):
    with open(input_file_dir, 'r') as f:
        return f.read().split()



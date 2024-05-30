"""
## FLOW ##
    <Before Runtime>
    Read CFG -> Test Ambiguity -> Create NFA -> Convert to DFA -> Create parsing table

    <During Runtime>
    Receive input string -> Parse input string -> Apply parsing table -> Accept or Reject

## Additional Requirements ##
    - Print parse tree for accepted strings
    - Print error report(ex. error location) for rejected strings
"""

import sys
from syntax_analyzer import *

## SLR Table action, goto table
action_file_dir = "./action.csv"
goto_file_dir = "./goto.csv"

## Target string

#input file 입력받는 걸로 바꿀 예정
token_list = []
if len(sys.argv) == 2:
    input_file_dir = sys.argv[1]
    token_list = get_tokens(input_file_dir)
    #token_list 테스트
    print(token_list)
elif len(sys.argv) == 1:
    print("Please enter target string to parse.")
    sys.exit()
else:
    print("Invalid input.")
    sys.exit()

## Read action, goto table
action_df = read_csv_file(action_file_dir).astype(str)
goto_df = read_csv_file(goto_file_dir).astype(str)
#데이터 프레임 안의 문자열을 String으로 변환


#test파일
# print(action_df.head())
# print(goto_df.head())

for token in token_list:
    if token not in return_terminal_list(action_df):
        print(f"\n<***Rejected, Invalid token detected***>: \'{token}\' \n")
        print("==================")
        print("Analysis complete.")
        sys.exit()

syntax_analyzer(token_list, action_df, goto_df)

print("==================")
print("Analysis complete.")

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
from util import *

## SLR Table action, goto table
action_file_dir = "./action.csv"
goto_file_dir = "./goto.csv"

## Target string

#input file 입력받는 걸로 바꿀 예정
token_list = []
if len(sys.argv) > 1:
    for arg in sys.argv:
        token_list.append(arg)
    del(token_list[0])
else:
    print("Please enter target string to parse.")
    sys.exit()

## Read action, goto table
action_df = read_csv_file(action_file_dir)
goto_df = read_csv_file(goto_file_dir)


#test파일
print(action_df.head())
print(goto_df.head())

syntax_analyzer(token_list, action_df, goto_df)

print("Analysis complete.")

input('')
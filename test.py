'''
## FLOW ##
    <Before Runtime>
    Read CFG -> Test Ambiguity -> Create NFA -> Convert to DFA -> Create parsing table

    <During Runtime>
    Receive input string -> Parse input string -> Apply parsing table -> Accept or Reject

## Additional Requirements ##
    - Print parse tree for accepted strings
    - Print error report(ex. error location) for rejected strings
'''

import pandas as pd

#read_csv(): pandas 라이브러리로 dataFrame 반환
action_df = pd.read_csv("./action.csv").astype(str)
# goto_df = pd.read_csv("./goto.csv")

print(action_df.head())
print(action_df.iloc[4,2])

print(action_df.iloc[:0])
print(action_df.head(0).columns.tolist())


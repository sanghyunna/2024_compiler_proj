from util import *
from parsetree import *

def syntax_analyzer(target_token_list, action_df, goto_df):
    ### SLR Parsing based on action, goto table
    terminal_list = return_terminal_list(action_df)

    cfg = get_cfg() 
    state_stack = [0] # stack only contains state numbers. In other words, it only contains integers.
    target_token_list.append("$") 
    # 개발 편의를 위해 splitter를 사용하지 않고 lhs, rhs를 따로 저장
    lhs_list = []
    rhs_list = target_token_list.copy()

    #reduce_cfg_list선언 => Parsetree에 넘길 인자
    reduce_cfg_list = []
    
    while True:
        
        decision = action_df.loc[curr_state(state_stack), next_input_symbol(rhs_list)]

        print_status(state_stack, lhs_list, rhs_list)
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

            #reduce가 일어났을 때 CFG번호 reduce_cfg_list저장
            reduce_cfg_list.append(rule_num)

            for i in range(len(rule_right)):
                lhs_list.pop()
            lhs_list.append(rule_left)

        elif decision == "acc":
            #if len(lhs_list) == 1 and lhs_list[0] == "S'":
                print("=======================\n<ACCEPTED!!!!.> ")
                print('Print Prase tree? say \'Yes\'')
                input('')
                print(reduce_cfg_list)
                root_node = construct_parse_tree(reduce_cfg_list)
                print_parse_tree(root_node)

                break
            #else:
             #   print("Rejected, \'acc\' was reached but lhs_list is not empty.")
            #break

        #reject 작업
        else:
            if decision == "nan":
                print("\n<***Rejected, Invalid input(Grammar) detected***, The corresponding field in the SLR table does not exist> \n")

            else:
                print("Rejected, undetermined Error")

            break
            #sys.exit()




    return None
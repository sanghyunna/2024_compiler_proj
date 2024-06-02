from util import *

from anytree import Node, RenderTree
from anytree.exporter import DotExporter

#String으로 변환 print(list(cfg[0].keys())[0])
# print(list(cfg[1].values())[0]    )

#초기 구상
'''def construct_parse_tree(cfg_number_list):
    cfg = get_cfg()
    stack = []

    for cfg_number in cfg_number_list:

        parent_node_name = list(cfg[cfg_number].keys())[0]
        parent_node = create_node(parent_node_name)
                
        for child_node_name in list(cfg[cfg_number].values())[0]:
            
            if check_child_node_is_in_stack(stack, child_node_name):
                child_node = stack.pop()
                child_node.parent = parent_node
                
            else: 
                 child_node = create_node(child_node_name)
                 child_node.parent = parent_node
            #child_node.parent = parent_node

        stack.append(parent_node)

    root_node = stack.pop()
    return root_node
'''

def construct_parse_tree(cfg_number_list):
    #action.df생성
    action_file_dir = "./action.csv"
    action_df = read_csv_file(action_file_dir)
    terminal_list = return_terminal_list(action_df) #해당 CFG의 Grammar에 속한 terminal들의 리스트를 가져옴

    cfg = get_cfg() #CFG Grammar rule을 가져오기 위한 문장
    stack = []      #Non terminal의 child node를 저장하기 위한 stack
    child_node_list = [] #child node들의 이름을 저장하기 위한 list

    for cfg_number in cfg_number_list:
        #디버깅용 문장, CFG NUMBER와 CFG GRAMMER를 출력함
        print("<CFG NUMBER> ", cfg_number)  
        print("<CFG GRAMMER> ", cfg[cfg_number])

        #parent_node_name과 해당 parent node가 가지고 있는 child_node의 이름들을 불러옴.
        parent_node_name = list(cfg[cfg_number].keys())[0]
        child_node_list = list(cfg[cfg_number].values())[0]

        #parent_node라면 node를 create함.
        parent_node = create_node(parent_node_name)
        print("<Parent NODE> ", parent_node_name)  

        #child_node list가 비어있을 때, epsilon을 표현하기 위해 ''를 추가함.
        if not child_node_list:
            child_node_list.append("\'\'")

        #반복문 동작
        for child_node_name in child_node_list:
            #디버깅용 문장
            print("<CHILD NODE> ", child_node_name)  
            #Non terminal의 child node가 stack에 있다면, pop하고 parent node에 연결함
            if check_child_node_is_in_stack(stack, child_node_name):
                #stack 재구성 과정
                new_stack = []
                while stack:
                    element = stack.pop()
                    if element.name == child_node_name:
                        child_node = element
                        child_node.parent = parent_node
                        break
                    new_stack.append(element)
                while new_stack:
                    stack.append(new_stack.pop())
                #디버깅용 문장. stack에서 빠져나오는지 확인
                print("Child node", child_node_name, "found in stack. Popping from stack and setting parent as", parent_node_name)
            #child node가 stack에 없다면
            else: 
                #child node를 create함, parent_node와 연결함.
                child_node = create_node(child_node_name)
                child_node.parent = parent_node
                #디버깅용 문장. child node가 parent node에 연결되었는지 확인
                print("Child node", child_node_name, "not found in stack. Creating new node and setting parent as", parent_node_name)
                
                #child node가 not terminal(Nonterminal)이고, epsilon이 아닐 때만 stack에 저장함.
                if child_node.name not in terminal_list and not "\'\'":
                 stack.append(child_node) 
        #parent node를 stack에 저장함. 다음 iteration에서 child node의 자격을 가짐
        stack.append(parent_node)
        #디버깅용 문장. stack의 state를 출력함.
        print("<stack> ")
        for node in stack:
             print(node.name)
        print("=================")
    #맨 마지막에 stack에 혼자 남아있는 root node를 반환
    root_node = stack.pop()
    return root_node


#node를 create하기 위한 메서드
def create_node(name):

    return Node(name)

#child_node가 stack에 있는지 판단하는 메서드
def check_child_node_is_in_stack(stack, child_node_name):
        for node in stack:
            if node.name == child_node_name:
                 return True
            
        return False
                
#parse tree를 출력함. RenderTree External library 이용
def print_parse_tree(root_node):
     for pre, fill, node in RenderTree(root_node):
          print("%s%s " % (pre, node.name))
     
#test
#root_node = construct_parse_tree([4,20,31,30,29,24,33,27,24,23,17,14,12,7,34,18,3,2,1])                    
#root_node = construct_parse_tree([4, 20, 31, 30, 29, 31, 30, 29, 24, 31, 30, 29, 24, 33, 27, 24, 23, 32, 27, 24, 23, 24, 32, 27, 24, 23, 17, 14, 12, 7, 34, 18, 3, 2, 1])  
#print_parse_tree(root_node)


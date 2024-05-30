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

#굳이 stack을 쓸 필요 없을 듯
def construct_parse_tree(cfg_number_list):
    action_file_dir = "./action.csv"
    action_df = read_csv_file(action_file_dir)
    terminal_list = return_terminal_list(action_df)

    cfg = get_cfg()
    stack = []

    for cfg_number in cfg_number_list:
        print("<CFG NUMBER> ", cfg_number)  
        print("<CFG GRAMMER> ", cfg[cfg_number])

        parent_node_name = list(cfg[cfg_number].keys())[0]
        parent_node = create_node(parent_node_name)
        print("<Parent NODE> ", parent_node_name)  
     
        for child_node_name in list(cfg[cfg_number].values())[0]:
            print("<CHILD NODE> ", child_node_name)  
            
            if check_child_node_is_in_stack(stack, child_node_name):
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

                print("Child node", child_node_name, "found in stack. Popping from stack and setting parent as", parent_node_name)
            else: 
                child_node = create_node(child_node_name)
                child_node.parent = parent_node
                print("Child node", child_node_name, "not found in stack. Creating new node and setting parent as", parent_node_name)
                
                if child_node.name not in terminal_list:
                 stack.append(child_node) 

        stack.append(parent_node)
        print("<stack> ")
        for node in stack:
             print(node.name)
        print("=================")

    root_node = stack.pop()
    return root_node


def create_node(name):

    return Node(name)

def check_child_node_is_in_stack(stack, child_node_name):
        for node in stack:
            if node.name == child_node_name:
                 return True
            
        return False
                
def print_parse_tree(root_node):
     for pre, fill, node in RenderTree(root_node):
          print("%s%s " % (pre, node.name))
     
#test
#root_node = construct_parse_tree([4,20,31,30,29,24,33,27,24,23,17,14,12,7,34,18,3,2,1])                    
#root_node = construct_parse_tree([4, 20, 31, 30, 29, 31, 30, 29, 24, 31, 30, 29, 24, 33, 27, 24, 23, 32, 27, 24, 23, 24, 32, 27, 24, 23, 17, 14, 12, 7, 34, 18, 3, 2, 1])  
#print_parse_tree(root_node)


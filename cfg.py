# cfg를 텍스트로 저장하지 않고, 함수의 형태로 가져올 수 있도록 구성함
def get_cfg():
    cfg = [
        {"S\'": ["CODE"]},
        {"CODE": ["VDECL", "CODE"]},
        {"CODE": ["FDECL", "CODE"]},
        {"CODE": []},
        {"VDECL": ["vtype", "id", "semi"]},
        {"VDECL": ["vtype", "ASSIGN", "semi"]},
        {"ASSIGN": ["id", "assign", "RHS"]},
        {"RHS": ["EXPR"]},
        {"RHS": ["literal"]},
        {"RHS": ["character"]},
        {"RHS": ["boolstr"]},
        {"EXPR": ["T_EXPR", "addsub", "EXPR"]},
        {"EXPR": ["T_EXPR"]},
        {"T_EXPR": ["F_EXPR", "multdiv", "T_EXPR"]},
        {"T_EXPR": ["F_EXPR"]},
        {"F_EXPR": ["lparen", "EXPR", "rparen"]},
        {"F_EXPR": ["id"]},
        {"F_EXPR": ["num"]},
        {"FDECL": ["vtype", "id", "lparen", "ARG", "rparen", "lbrace", "BLOCK", "RETURN", "rbrace"]},
        {"ARG": ["vtype", "id", "MOREARGS"]},
        {"ARG": []},
        {"MOREARGS": ["comma", "vtype", "id", "MOREARGS"]},
        {"MOREARGS": []},
        {"BLOCK": ["STMT", "BLOCK"]},
        {"BLOCK": []},
        {"STMT": ["VDECL"]},
        {"STMT": ["ASSIGN", "semi"]},
        {"STMT": ["if", "lparen", "COND", "rparen", "lbrace", "BLOCK", "rbrace", "ELSE"]},
        {"STMT": ["while", "lparen", "COND", "rparen", "lbrace", "BLOCK", "rbrace"]},
        {"COND": ["boolstr", "COND_T"]},
        {"COND_T": ["comp", "boolstr", "COND_T"]},
        {"COND_T": []},
        {"ELSE": ["else", "lbrace", "BLOCK", "rbrace"]},
        {"ELSE": []},
        {"RETURN": ["return", "RHS", "semi"]}
    ]
    return cfg

# cfg rule의 key를 반환
def key(rule_dict):
    return list(rule_dict.keys())[0]

# cfg rule의 value를 반환
def val(rule_dict):
    return list(rule_dict.values())[0]

cfg = get_cfg()

#print(list(cfg[1].keys())[0])
#print(list(cfg[1].values())[0]    )




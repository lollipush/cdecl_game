class AST(object):
    def __init__(self, _type, _value):
        self._type = _type
        self._value = _value
        pass

grammar = {
        'Main': ( ( 'Decl', 'semicolon' ), ),
        'Decl': ( ( 'Type', 'id', 'lpar', 'ParamList', 'rpar' ), ),
        'Type': ( ( 'char', ) ,
                  ( 'int', ) ,
                  ( 'signed', ) ,
                  ( 'unsigned', ) ,
                  ( 'float', ) ,
                  ( 'double', ) ,
                  ( 'Type', 'star' ) ,
            ),
        'ParamList': ( ( 'Param', ),
                       ( 'ParamList', 'dot', 'Param', ),
                       ( ),
            ),
        'Param': ( ( 'Type', 'id' ),
            ),
}

def accept_token(tks, start, _type):
    if start >= len(tks) or tks[start]._type not in _type:
        return 0, None
    return 1, AST(tks[start]._type, tks[start])


def accppt_param(tks, start):
    if start >= len(tks):
        return 0, None
    size_type, ast_type = accept_type(tks, start)
    if size_type == 0:
        return 0, None
    start += size_type
    size_id, ast_id = accept_token(tks, start, ('id', ))
    if size_id == 0:
        return 0, None
    return size_type + size_id, AST('Param', (ast_type, ast_id))


def accept_paramlist(tks, start):
    if start >= len(tks):
        return 0, None
    size, _ast = accept_param(tks, start)
    ast = []
    if size > 0:
        ast.append(_ast)
        start += size
        while True:
            size_dot, ast_dot = accept_token(tks, start, ('dot', ))
            if size_dot == 0:
                break
            start += size_dot
            size_param, ast_param = accept_param(tks, start)
            if size_param == 0:
                break
            start += size_param
            size += size_dot + size_param
            ast.append(ast_dot)
            ast.append(ast_param)
    return size, AST('ParamList', tuple(ast))


def accept_type(tks, start):
    if start >= len(tks):
        return 0, None
    ast = []
    size = 0
    _size, _ast = accept_token(tks, start, ('float', 'double', ))
    size += _size
    if size == 0:
        _size, _ast = accept_token(tks, start, ('unsigned', 'signed', ))
        if _size > 0:
            start += _size
            size += _size
            ast.append(_ast)
        _size, _ast = accept_token(tks, start, ('long', 'short', ))
        if _size > 0:
            start += _size
            size += _size
            ast.append(_ast)
        _size, _ast = accept_token(tks, start, ('int', 'char', ))
        if _size > 0:
            start += _size
            size += _size
            ast.append(_ast)
        else:
            return 0, None
    while True:
        _size, _ast = accept_token(tks, start, ('star', ))
        if _size > 0:
            start += _size
            size += _size
            ast.append(_ast)
        else:
            break
    return size, AST('Type', tuple(ast))


def accept_decl(tks, start):
    if start >= len(tks):
        return 0, None
    size_type, ast_type = accept_type(tks, start)
    if size_type == 0:
        return 0, None
    start += size_type
    size_id, ast_id = accept_token(tks, start, ('id', ))
    if size_id == 0:
        return 0, None
    start += size_id
    size_lpar, ast_lpar = accept_token(tks, start, ('lpar', ))
    if size_lpar == 0:
        return 0, None
    start += size_lpar
    size_paramlist, ast_paramlist = accept_paramlist(tks, start)
    if size_paramlist == 0:
        return 0, None
    start += size_paramlist
    size_rpar, ast_rpar = accept_token(tks, start, ('rpar', ))
    if size_rpar == 0:
        return 0, None
    return size_type + size_id + size_lpar + size_paramlist + size_rpar, AST('Decl', (ast_type, ast_id, ast_lpar, ast_paramlist, ast_rpar))


def accept_main(tks, start):
    if start >= len(tks):
        return 0, None
    size_decl, ast_decl = accept_decl(tks, start)
    if size_decl == 0:
        return 0, None
    start += size_decl
    size_semicolon, ast_semicolon = accept_token(tks, start, ('semicolon', ))
    if size_semicolon == 0:
        return 0, None
    return size_decl + size_semicolon, AST('Main', (ast_decl, ast_semicolon))


def parser(tks):
    size, ast = accept_main(tks, 0)
    if size > 0:
        return ast
    else:
        raise Exception('syntax error')
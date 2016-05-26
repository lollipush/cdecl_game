class Token(object):
    def __init__(self, _type, _value):
        self._type = _type
        self._value = _value

    def __str__(self):
        return '<{0} {1}>'.format(self._type, repr(self._value))

    def __repr__(self):
        return '<{0} {1}>'.format(self._type, repr(self._value))

keywords = ('auto', 'rigister', 'static', 'extern', 'typedef', 'const', 'volatile', 'void', 'char', 'short', 'int', 'long', 'float', 'double', 'unsigned', 'signed', 'struct', 'union', 'enum', )

def tokenizer(s):
    i = 0
    while i < len(s):
        if s[i] in ' \t\r\n':
            i += 1
        elif s[i] == '(':
            i += 1
            yield Token('lpar', '(')
        elif s[i] == ')':
            i += 1
            yield Token('rpar', ')')
        elif s[i] == '[':
            i += 1
            yield Token('lbrkt', '[')
        elif s[i] == ']':
            i += 1
            yield Token('rbrkt', ']')
        elif s[i] == '{':
            i += 1
            yield Token('lbrace', '{')
        elif s[i] == '}':
            i += 1
            yield Token('rbrace', '}')
        elif s[i] == '=':
            i += 1
            yield Token('assign', '=')
        elif s[i] == '*':
            i += 1
            yield Token('star', '*')
        elif s[i] == '.':
            if i + 2 < len(s) and s[i + 1] == '.' and s[i + 2] == '.':
                i += 3
                yield Token('ellipsis', '...')
            else:
                i += 1
                yield Token('dot', '.')
        elif s[i] == ',':
            i += 1
            yield Token('comma', ',')
        elif s[i] == ';':
            i += 1
            yield Token('semicolon', ';')
        elif s[i].isalpha() or s[i] == '_':
            t = i
            while i < len(s) and (s[i].isalnum() or s[i] == '_'):
                i += 1
            v = s[t:i]
            if v in keywords:
                yield Token(v, v)
            else:
                yield Token('id', v)
        elif s[i].isdigit():
            t = i
            if i + 2 < len(s) and s[i] == '0' and s[i + 1].lower() == 'x':
                i += 2
                alphabet = '0123456789abcdefABCDEF'
            else:
                i += 1
                alphabet = '0123456789'
            while i < len(s) and s[i] in alphabet:
                i += 1
            yield Token('number', s[t:i])
        else:
            raise Exception('invalid token: ' + s[i:])







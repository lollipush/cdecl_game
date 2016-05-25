class Token(object):
    def __init__(self, _type, _value):
        self._type = _type
        self._value = _value

    def __str__(self):
        return '<{0} {1}>'.format(self._type, repr(self._value))

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
        elif s[i] == '*':
            i += 1
            yield Token('star', '*')
        elif s[i] == ',':
            i += 1
            yield Token('dot', ',')
        elif s[i] == ';':
            i += 1
            yield Token('semicolon', ';')
        elif s[i].isalpha() or s[i] == '_':
            t = i
            while s[i].isalnum() or s[i] == '_':
                i += 1
            v = s[t:i]
            if v in ['int', 'char', 'float', 'double', 'unsigned', 'signed', 'short', 'long']:
                yield Token('type', s[t:i])
            else:
                yield Token('id', s[t:i])
        elif s[i].isdigit():
            t = i
            while s[i].isdigit():
                i += 1
            yield Token('number', s[t:i])
        else:
            raise Exception('invalid token: ' + s[i:])







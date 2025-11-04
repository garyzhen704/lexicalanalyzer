# Token Definitions for Lexical Analyzer
# CPSC 323 - Project 1

# All keywords we need to recognize
KEYWORDS = {
    'int', 'float', 'char', 'string',
    'if', 'else', 'for', 'return',
    'while', 'void', 'do', 'break'
}

# All operators we need to recognize
OPERATORS = {
    '+', '-', '*', '/', '%', '=',
    '==', '!=', '<', '>', '<=', '>=',
    '++', '--', '&&', '||', '!'
}

# All separators including parentheses and punctuation
SEPARATORS = {
    '(', ')', '{', '}', '[', ']',
    ';', ','
}

# Token type names for output
TOKEN_KEYWORD = "keyword"
TOKEN_IDENTIFIER = "identifier"
TOKEN_OPERATOR = "operator"
TOKEN_SEPARATOR = "separator"
TOKEN_LITERAL = "literal"

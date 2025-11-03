"""
Token Definitions for C++ Lexical Analyzer
CPSC 323 - Project 1
Team: [Person A Name], [Person B Name], [Person C Name]
"""

KEYWORDS = {
    'int', 'float', 'char', 'string',
    'if', 'else', 'for', 'return',
    'while', 'void', 'do', 'break'
}

OPERATORS = {
    '+', '-', '*', '/', '%', '=',
    '==', '!=', '<', '>', '<=', '>=',
    '++', '--', '&&', '||', '!'
}

# Combine parentheses and punctuation into SEPARATORS (per assignment)
SEPARATORS = {
    '(', ')', '{', '}', '[', ']',
    ';', ','
}

# Token type names (per assignment instructions)
TOKEN_KEYWORD = "keyword"
TOKEN_IDENTIFIER = "identifier"
TOKEN_OPERATOR = "operator"
TOKEN_SEPARATOR = "separator"       # Changed from parentheses/punctuation
TOKEN_LITERAL = "literal"           # Changed from constant

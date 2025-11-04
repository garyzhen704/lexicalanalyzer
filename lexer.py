from token_definitions import *
import re

def remove_comments(code):
    # Regex pattern has two groups: group 1 = strings/chars, group 2 = comments
    # We match strings first to avoid removing comment-like text inside strings
    # (?:[^"\\]|\\.)* matches any char except " or \, or any escaped char
    pattern = r'("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\')|(/\*.*?\*/|//[^\n]*)'
    
    def replace_func(match):
        if match.group(1):
            return match.group(1)  # keep strings and chars unchanged
        else:
            return ''  # replace comments with empty string
    
    # re.DOTALL makes . match newlines for multi-line comments
    code = re.sub(pattern, replace_func, code, flags=re.DOTALL)
    return code

def tokenize(code):
    # Regex pattern to extract all tokens from the code
    # Order matters, need to check multi-char patterns before single-char
    # \d matches digits, \w matches word chars, [a-zA-Z_] starts identifiers
    pattern = r'''
        "(?:[^"\\]|\\.)*"       |  # strings
        '(?:[^'\\]|\\.)'        |  # characters
        \d+\.\d+                |  # floats (before integers)
        \d+                     |  # integers
        >=|<=|==|!=|\+\+|--|\&\&|\|\|| |  # multi-character operators
        [a-zA-Z_]\w*            |  # identifiers and keywords
        [+\-*/%=<>!;,(){}[\]]       # single-character operators and separators
    '''
    
    tokens = re.findall(pattern, code, re.VERBOSE)
    tokens = [t for t in tokens if t.strip()]  # remove any whitespace tokens
    return tokens

def classify_token(lexeme):
    # Check keywords first so "int" doesn't get classified as an identifier
    if lexeme in KEYWORDS:
        return TOKEN_KEYWORD
    
    if lexeme in OPERATORS:
        return TOKEN_OPERATOR
    
    if lexeme in SEPARATORS:
        return TOKEN_SEPARATOR
    
    # Check for different types of literals using regex
    if re.match(r'^\d+$', lexeme):  # integers like 10, 42
        return TOKEN_LITERAL
    
    if re.match(r'^\d+\.\d+$', lexeme):  # floats like 20.5
        return TOKEN_LITERAL
    
    if re.match(r'^".*"$', lexeme):  # strings like "Hello"
        return TOKEN_LITERAL
    
    if re.match(r"^'(?:[^'\\]|\\.)'$", lexeme):  # characters like 'x'
        return TOKEN_LITERAL
    
    # Everything else is an identifier
    return TOKEN_IDENTIFIER

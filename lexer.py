from token_definitions import *
import re

def remove_comments(code):
    # Remove // and /* */ style comments but keep them if they appear in strings
    # The pattern matches strings/chars first, then matches comments
    pattern = r'("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\')|(/\*.*?\*/|//[^\n]*)'
    
    def replace_func(match):
        if match.group(1):
            return match.group(1)  # keep strings and chars
        else:
            return ''  # remove comments
    
    code = re.sub(pattern, replace_func, code, flags=re.DOTALL)
    return code

def tokenize(code):
    # Extract tokens using regex patterns
    # Order matters, longer patterns need to be checked before shorter ones
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
    tokens = [t for t in tokens if t.strip()]
    return tokens

def classify_token(lexeme):
    # Check what type of token this is
    # Check keywords first so "int" doesn't get classified as an identifier
    if lexeme in KEYWORDS:
        return TOKEN_KEYWORD
    
    if lexeme in OPERATORS:
        return TOKEN_OPERATOR
    
    if lexeme in SEPARATORS:
        return TOKEN_SEPARATOR
    
    # Check for different types of literals
    if re.match(r'^\d+$', lexeme):  # integers
        return TOKEN_LITERAL
    
    if re.match(r'^\d+\.\d+$', lexeme):  # floats
        return TOKEN_LITERAL
    
    if re.match(r'^".*"$', lexeme):  # strings
        return TOKEN_LITERAL
    
    if re.match(r"^'(?:[^'\\]|\\.)'$", lexeme):  # characters
        return TOKEN_LITERAL
    
    # Everything else is an identifier
    return TOKEN_IDENTIFIER

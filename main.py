from lexer import remove_comments, tokenize, classify_token
from token_definitions import *
import sys

def format_output(lexeme, token_type):
    # Format output as "lexeme" = token_type
    return '"{}" = {}'.format(lexeme, token_type)

def process_file(input_filename):
    # Read input file
    with open(input_filename, 'r') as f:
        code = f.read()
    
    # Remove comments from the source code
    clean_code = remove_comments(code)
    
    # Break code into tokens
    tokens = tokenize(clean_code)
    
    # Classify and format each token
    results = []
    for token in tokens:
        token_type = classify_token(token)
        formatted = format_output(token, token_type)
        results.append(formatted)
    
    return results

def main():
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    try:
        results = process_file(input_file)
        
        # Print to console
        for line in results:
            print(line)
        
        # Save to output file
        with open("output.txt", "w") as f:
            f.write("\n".join(results))
            
    except FileNotFoundError:
        print("Error: File '{}' not found".format(input_file))
        sys.exit(1)
    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)

if __name__ == "__main__":
    main()

# tokenizer.py
import re

RESERVED = {
    "program", "var", "begin", "end", "integer", "show"
}

# Regex patterns for each token
TOKEN_REGEX = [
    (r'\s+', None),  # Skip whitespace
    (r'"value="', 'STRING'),
    (r'[a-zA-Z][a-zA-Z0-9]*', 'IDENT'),
    (r'[0-9]+', 'NUMBER'),
    (r'[+\-*/=;,():]', 'SYMBOL'),
]


def lexer(source_code):
    tokens = []
    pos = 0
    while pos < len(source_code):
        match_found = False
        for pattern, token_type in TOKEN_REGEX:
            regex = re.compile(pattern)
            match = regex.match(source_code, pos)
            if match:
                value = match.group(0)
                if token_type:
                    if token_type == 'IDENT' and value in RESERVED:
                        tokens.append(value)  # reserved word
                    elif token_type == 'STRING':
                        tokens.append('"value="')
                    else:
                        tokens.append(value)
                pos = match.end(0)
                match_found = True
                break
        if not match_found:
            raise SyntaxError(f"Unexpected character: {source_code[pos]}")
    return tokens


if __name__ == '__main__':
    SOURCE_CODE = "final25.txt"
    with open(SOURCE_CODE, "r") as f:
        code = f.read()
    result = lexer(code)
    print(result)

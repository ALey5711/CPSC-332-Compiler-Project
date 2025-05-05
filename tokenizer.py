# tokenizer.py
import re

RESERVED = {
    "program", "var", "begin", "end", "integer", "show"
}

TOKEN_REGEX = [
    (r'\s+', None),                      # Skip whitespace
    (r'"value="', 'STRING'),
    (r'[a-zA-Z][a-zA-Z0-9]*', 'IDENT'),  # Identifiers or reserved words
    (r'[0-9]+', 'NUMBER'),               # Numbers (if not part of ident)
    (r'[+\-*/=;,():]', 'SYMBOL'),        # Symbols
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
                    if token_type == 'IDENT':
                        if value in RESERVED:
                            tokens.append(value)
                        else:
                            # Split non-reserved ident
                            tokens.extend(list(value))
                    elif token_type == 'STRING':
                        tokens.append('"value="')
                    else:
                        tokens.append(value)
                pos = match.end(0)
                match_found = True
                break
        if not match_found:
            raise SyntaxError(f"Unexpected character: {source_code[pos]}")
    tokens.append('$')
    return tokens


if __name__ == '__main__':
    with open("final25.txt", "r") as f:
        code = f.read()
    result = lexer(code)
    print(result)

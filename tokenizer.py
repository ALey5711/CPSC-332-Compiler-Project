# tokenizer.py
import re

RESERVED_KEYWORDS = {
    "program", "var", "begin", "end", "integer", "show"
}

TOKEN_REGEX = [
    (r'\s+', None),                      # Skip whitespace
    (r'"value="', 'STRING'),
    (r'[a-zA-Z][a-zA-Z0-9]*', 'IDENT'),  # Identifiers or reserved words
    # Numbers (to be split into single digits)
    (r'[0-9]+', 'NUMBER'),
    (r'[+\-*/=;,():]', 'SYMBOL'),      # Symbols
]


def lexer(source_code):
    tokens = []
    position = 0

    while position < len(source_code):
        match_found = False

        for pattern, token_type in TOKEN_REGEX:
            regex = re.compile(pattern)
            match = regex.match(source_code, position)

            if match:
                matched_text = match.group(0)

                if token_type:
                    if token_type == 'IDENT':
                        if matched_text in RESERVED_KEYWORDS:
                            tokens.append(matched_text)
                        else:
                            tokens.extend(list(matched_text))

                    elif token_type == 'STRING':
                        tokens.append('"value="')

                    elif token_type == 'NUMBER':
                        tokens.extend(list(matched_text))  # Split each digit

                    else:
                        tokens.append(matched_text)

                position = match.end()
                match_found = True
                break

        if not match_found:
            raise SyntaxError(
                f"Unexpected character at position {position}: '{source_code[position]}'")

    tokens.append('$')
    return tokens


if __name__ == '__main__':
    with open("final25.txt", "r") as file:
        source = file.read()
    token_list = lexer(source)
    print(token_list)

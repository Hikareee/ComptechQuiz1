TOKEN_KEYWORD = 'keyword'

def lexer(file):
    tokens = []
    i = 0
    code_length = len(file)

    while i < code_length:
        char = file[i]

        if char == "i":
            i+=1
            if char == "n":
                i+=1
                if char == "t":
                    i+=1
                    tokens.append((TOKEN_KEYWORD,"int"))
        elif char == "f":
            i+=1
            if char == "l":
                i+=1
                if char == "o":
                    i+=1
                    if char == "a":
                        i+=1
                        if char == "t":
                            i+=1
                            tokens.append((TOKEN_KEYWORD,"float"))
        if char == "w":
            i+=1
            if char == "h":
                i+=1
                if char == "i":
                    i+=1
                    if char == "l":
                        i+=1
                        if char == "e":
                            i+=1
                            tokens.append((TOKEN_KEYWORD,"while"))
        elif char == "m":
            i+=1
            if char == "a":
                i+=1
                if char == "i":
                    i+=1
                    if char == "n":
                        i+=1
                        tokens.append((TOKEN_KEYWORD,"main"))
        elif char == "c":
            i+=1
            if char == "o":
                i+=1
                if char == "n":
                    i+=1
                    if char == "s":
                        i+=1
                        if char == "t":
                            i+=1
                            tokens.append((TOKEN_KEYWORD,"const"))
    return tokens


def user_input():
    print("Input your calculation (Add an empty line to enter): ")

    #it can take not only a single input line, so users can enter newlines and type their input,
    #but once it is just an empty line input, the lexer will prompt to start
    input_lines = []
    while True:
        line = input()
        if not line:
            break
        input_lines.append(line)
    return '\n'.join(input_lines)

def main():
    wee = user_input()
    tokens = lexer(wee)
    #printing each of the tokens and lexeme detected in the input
    for token_type, token_value in tokens:
        print(f"{TOKEN_KEYWORD if token_type == 'keyword' else token_type}: {token_value}")

main()


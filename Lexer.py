def is_keyword(code):
    keywords = ['int', 'float', 'while', 'main', 'const']
    return code in keywords


def lexer(code):
    i = 0
    tokens = []
    lexemes = []
    code_length = len(code)
    while i < code_length:
        if code[i].isspace():
            i += 1
        elif code[i:i+2] == '//':
            i = code.index('\n', i)
        elif code[i:i+2] == '/*':
            i = code.index('*/', i) + 2
        elif code[i].isalpha():
            j = i + 1
            while j < len(code) and (code[j].isalpha() or code[j].isdigit()):
                j += 1
            if is_keyword(code[i:j]):
                tokens.append('keyword')
                lexemes.append(code[i:j])
            i = j
        else:
            i += 1
    return tokens, lexemes


code = 'int main(){const float payment = 384.00;float bal;int month = 0;bal=15000;while (bal>0){printf("Month: %2d Balance: %10.2f\n", month, bal);bal=bal-payment+0.015*bal;month=month+1;}}'
tokens, lexemes = lexer(code)
for token, lexeme in zip(tokens, lexemes):
    print(token, lexeme)

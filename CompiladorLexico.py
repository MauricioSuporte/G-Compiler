arquivo = open("entrada.txt", "r")
contador = 0
tokens = []
for linha in arquivo:
    contador = contador + 1
    linha = linha.rstrip()
    i = 0
    tam = len(linha)
    while i < tam:
        if linha[i] == ":" and linha[i+1] == "=":
            tokens.append(" :=")
            i = i + 2
        elif linha[i] == "v" and linha[i+1] == "a" and linha[i+2] == "r":
            tokens.append(" var")
            i = i + 3
        elif linha[i] == "i" and linha[i+1] == "n" and linha[i+2] == "t" and linha[i+3] == "e" \
                and linha[i+4] == "g" and linha[i+5] == "e" and linha[i+6] == "r":
            tokens.append(" integer")
            i = i + 7
        elif linha[i] == "r" and linha[i+1] == "e" and linha[i+2] == "a" and linha[i+3] == "l":
            tokens.append(" real")
            i = i + 4
        elif linha[i] == "," or linha[i] == ";" or linha[i] == "+" or linha[i] == ":":
            tokens.append(" " + linha[i])
            i = i + 1
        elif ((linha[i] >= "a" and linha[i] <= "z") or (linha[i] >= "A" and linha[i] <= "Z")):
            j = i + 1
            temp = linha[i]
            while (j < tam):
                if ((linha[j] >= "a" and linha[j] <= "z") or (linha[j] >= "A" and linha[j] <= "Z")
                        or (linha[j] >= "1" and linha[j] <= "9")):
                    temp = temp + linha[j]
                    j = j + 1
                else:
                    break
            tokens.append(" " + temp)
            i = j
        elif linha[i] == "i" and linha[i+1] == "f":
            tokens.append(" if")
            i = i + 2
        elif linha[i] == "t" and linha[i+1] == "h" and linha[i+2] == "e" and linha[i+3] == "n":
            tokens.append(" then")
            i = i + 4
        elif linha[i] == " ":
            i = i + 1
            continue
        else:
            print("Erro lexico, caracter " + linha[i] + " nao conhecido")
            i = i + 1
tokens[0] = tokens[0].replace(" ", "")
print(tokens)
arqSintatico = open("entradaSintatico.txt", "w")
arqSintatico.writelines(tokens)
arqSintatico.close()
arquivo.close()
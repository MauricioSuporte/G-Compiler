arquivo = open("entradaSintatico.txt", "r")
tokens = arquivo.read()
tokens = tokens.split(" ")

def Z(ch, pos):
    if ch == "var":
        ch, pos = I(ch, pos)
        ch, pos = S(ch, pos)
        print("Cadeia sintaticamente correta.")
    else:
        print("Erro, esperado var e encontrado %s no %dº token" %(ch, pos+1))

def I(ch, pos):
    if ch == "var":
        ch, pos = proxsimb(ch, pos)
        ch, pos = D(ch, pos)
        return (ch, pos)
    else:
        print("Erro, esperado var e encontrado %s no %dº token" %(ch, pos+1))

def D(ch, pos):
    if ch == "id":
        ch, pos = L(ch, pos)
        if ch == ":":
            ch, pos = proxsimb(ch, pos)
            ch, pos = K(ch, pos)
            ch, pos = O(ch, pos)
            return (ch, pos)
        else:
            print("Erro, esperado : e encontrado %s no %dº token" %(ch, pos+1))
    elif ch == "if":
        return (ch, pos)
    else:
        print("Erro, esperado id ou if e encontrado %s no %dº token" % (ch, pos + 1))

def L(ch, pos):
    if ch == "id":
        ch, pos = proxsimb(ch, pos)
        ch, pos = X(ch, pos)
        return(ch, pos)
    else:
        print("Erro, esperado id e encontrado %s no %dº token" %(ch, pos+1))

def X(ch, pos):
    if ch == ",":
        ch, pos = proxsimb(ch, pos)
        ch, pos = L(ch, pos)
        return(ch, pos)
    elif ch == ":":
        return (ch, pos)   #Como fazer elemento neutro????
    else:
        print("Erro, esperado , ou : e encontrado %s no %dº token" %(ch, pos+1))

def K(ch, pos):
    if ch == "integer":
        ch, pos = proxsimb(ch, pos)
        return (ch, pos)
    elif ch == "real":
        ch, pos = ch, pos = proxsimb(ch, pos)
        return (ch, pos)
    else:
        print("Erro, esperado integer ou real e econtrado %s no %dº token" %(ch, pos+1))

def O(ch, pos):
    if ch == ";":
        ch, pos = proxsimb(ch, pos)
        ch, pos = D(ch, pos)
        return (ch, pos)
    else:
        print("Erro, esperado id e econtrado %s no %dº token" %(ch, pos+1))

def S(ch, pos):
    if ch == "id":
        ch, pos = proxsimb(ch, pos)
        if ch == ":=":
            ch, pos = proxsimb(ch, pos)
            ch, pos = E(ch, pos)
            return (ch, pos)
        else:
            print("Erro, esperado := e econtrado %s no %dº token" %(ch, pos+1))
    elif ch == "if":
        ch, pos = proxsimb(ch, pos)
        ch, pos = E(ch, pos)
        if ch == "then":
            ch, pos = proxsimb(ch, pos)
            ch, pos = S(ch, pos)
            return (ch, pos)
        else:
            print("Erro, esperado then e econtrado %s no %dº token" %(ch, pos+1))
    else:
        print("Erro, esperado id e econtrado %s no %dº token" %(ch, pos+1))

def E(ch, pos):
    if ch == "id":
        ch, pos = T(ch, pos)
        ch, pos = R(ch, pos)
        return (ch, pos)
    else:
        print("Erro, esperado id e econtrado %s no %dº token" %(ch, pos+1))

def R(ch, pos):
    if ch == "+":
        ch, pos = proxsimb(ch, pos)
        ch, pos = T(ch, pos)
        ch, pos = R(ch, pos)
        return (ch, pos)
    elif ch == "then":
        return (ch, pos)
    elif ch == "#":
        return (ch, pos)
    else:
        print("Erro, esperado + e econtrado %s no %dº token" %(ch, pos+1))


def T(ch, pos):
    if ch == "id":
        ch, pos = proxsimb(ch, pos)
        return (ch, pos)
    else:
        print("Erro, esperado id e econtrado %s no %dº token" %(ch, pos+1))


def proxsimb(ch, pos):
    if pos < len(tokens)-1:
        return (tokens[pos + 1], pos + 1)
    else:
        return ("#", pos)


#Main
Z(tokens[0], 0)
arquivo.close()
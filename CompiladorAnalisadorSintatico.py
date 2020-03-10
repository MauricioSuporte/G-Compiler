arquivo = open("entradaSintatico.txt", "r")
tokens = arquivo.read()
tokens = tokens.split(" ")
posInicial = 0
posFinal = 0
tabSimb = []
verificacoes = []
cod3Ende = []

def Z(ch, pos):
    if ch == "var":
        ch, pos = I(ch, pos)
        ch, pos = S(ch, pos)
        print("Cadeia sintaticamente correta.")
    else:
        print("Erro, esperado var e encontrado %s no %dº token" %(ch, pos+1))
        exit()

def I(ch, pos):
    if ch == "var":
        ch, pos = proxsimb(ch, pos)
        ch, pos = D(ch, pos)
        return (ch, pos)
    else:
        print("Erro, esperado var e encontrado %s no %dº token" %(ch, pos+1))
        exit()

def D(ch, pos):
    if isIdent(ch):
        ch, pos = L(ch, pos)
        if ch == ":":
            ch, pos = proxsimb(ch, pos)
            ch, pos = K(ch, pos)
            ch, pos = O(ch, pos)
            return (ch, pos)
        else:
            print("Erro, esperado : e encontrado %s no %dº token" %(ch, pos+1))
            exit()
    elif ch == "if":
        return (ch, pos)
    else:
        print("Erro, esperado identificador ou if e encontrado %s no %dº token" % (ch, pos + 1))
        exit()

def L(ch, pos):
    if isIdent(ch):
        addTabSimb(ch)
        ch, pos = proxsimb(ch, pos)
        ch, pos = X(ch, pos)
        return(ch, pos)
    else:
        print("Erro, esperado identificador e encontrado %s no %dº token" %(ch, pos+1))
        exit()

def X(ch, pos):
    if ch == ",":
        ch, pos = proxsimb(ch, pos)
        ch, pos = L(ch, pos)
        return(ch, pos)
    elif ch == ":":
        return (ch, pos)   #Como fazer elemento neutro????
    else:
        print("Erro, esperado , ou : e encontrado %s no %dº token" %(ch, pos+1))
        exit()

def K(ch, pos):
    if ch == "integer":
        addTipo(ch, ch)
        ch, pos = proxsimb(ch, pos)
        return (ch, pos)
    elif ch == "real":
        addTipo(ch, ch)
        ch, pos = ch, pos = proxsimb(ch, pos)
        return (ch, pos)
    else:
        print("Erro, esperado integer ou real e econtrado %s no %dº token" %(ch, pos+1))
        exit()

def O(ch, pos):
    if ch == ";":
        ch, pos = proxsimb(ch, pos)
        ch, pos = D(ch, pos)
        return (ch, pos)
    elif isIdent(ch):
        return (ch, pos)
    elif ch == "if":
        return (ch, pos)
    else:
        print("Erro, esperado ; ou identificador ou if e econtrado %s no %dº token" %(ch, pos+1))
        exit()

def S(ch, pos):
    if isIdent(ch):
        addListaVerificacao(ch)
        ch, pos = proxsimb(ch, pos)
        if ch == ":=":
            ch, pos = proxsimb(ch, pos)
            ch, pos = E(ch, pos)
            return (ch, pos)
        else:
            print("Erro, esperado := e econtrado %s no %dº token" %(ch, pos+1))
            exit()
    elif ch == "if":
        ch, pos = proxsimb(ch, pos)
        ch, pos = E(ch, pos)
        if ch == "then":
            ch, pos = proxsimb(ch, pos)
            ch, pos = S(ch, pos)
            return (ch, pos)
        else:
            print("Erro, esperado then e econtrado %s no %dº token" %(ch, pos+1))
            exit()
    else:
        print("Erro, esperado identificador ou if e econtrado %s no %dº token" %(ch, pos+1))
        exit()

def E(ch, pos):
    if isIdent(ch):
        ch, pos = T(ch, pos)
        ch, pos = R(ch, pos)
        return (ch, pos)
    else:
        print("Erro, esperado identificador e econtrado %s no %dº token" %(ch, pos+1))
        exit()

def R(ch, pos):
    if ch == "+":
        ch, pos = proxsimb(ch, pos)
        ch, pos = T(ch, pos)
        ch, pos = R(ch, pos)
        return (ch, pos)
    elif ch == "then":
        global verificacoes
        if (not verificaTipo(verificacoes)):
            exit()
        verificacoes = []
        return (ch, pos)
    elif ch == "#":
        if (not verificaTipo(verificacoes)):
            exit()
        verificacoes = []
        return (ch, pos)
    else:
        print("Erro, esperado + ou then e econtrado %s no %dº token" %(ch, pos+1))
        exit()


def T(ch, pos):
    if isIdent(ch):
        addListaVerificacao(ch)
        ch, pos = proxsimb(ch, pos)
        return (ch, pos)
    else:
        print("Erro, esperado identificador e econtrado %s no %dº token" %(ch, pos+1))
        exit()


def proxsimb(ch, pos):
    if pos < len(tokens)-1:
        return (tokens[pos + 1], pos + 1)
    else:
        return ("#", pos)

def isIdent(ch):
    if ch == "var" or ch == "integer" or ch == "real" or ch == "if" or ch == "then":
        resultado = False
    elif (ch[0] >= "a" and ch[0] <= "z") or (ch[0] >= "A" and ch[0] <= "Z"):
        resultado = True
    else:
        resultado = False
    return resultado

def addTabSimb(ch):
    global posFinal, tabSimb
    for i in range(0, len(tabSimb)):
        if tabSimb[i]['Cadeia'] == ch:
            print('Cadeia ' + ch + " ja existe na tabela de simbolos.")
            exit()
    posFinal = posFinal + 1
    conteudo = {'Cadeia': ch, 'Token': 'id', 'Categoria': 'var', 'Tipo': 'null'}
    tabSimb.append(conteudo)

def addTipo(ch, tipo):
    global posInicial, posFinal, tabSimb
    for i in range(posInicial, posFinal):
        tabSimb[i]['Tipo'] = tipo
    posInicial = posFinal

def addListaVerificacao(ch):
    global verificacoes, tabSimb
    for i in range(len(tabSimb)):
        if tabSimb[i]['Cadeia'] == ch:
            verificacoes.append(tabSimb[i]['Tipo'])

def verificaTipo(verificacoes):
    tipo = verificacoes[0]
    for i in verificacoes:
        if i != tipo:
            print("Impossivel operar real com inteiro")
            return False
    verificacoes = []
    return True


#Main
Z(tokens[0], 0)
arquivo.close()

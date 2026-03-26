def modifica_convidados(c):
    if c[1] in c[0]:
        c[0][c[0].index(c[1])] = c[2]
    return c[0]

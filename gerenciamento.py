f = open(r'C:\Users\mateu\Documents\UFRN\8º Semestre\SO\build-gerenciamentodememoria-Desktop_Qt_5_11_1_MinGW_32bit-Debug\sequencia01.txt','r').readlines()

acerto_pagina = 0
falha_pagina = 0
acesso_memoria = 0
operacao_ES = 0
tab_pag = [False]*1024
tempo_acesso = 0

for i in range (0, len(f)):
    f[i] = int(f[i])
    f[i] = format(f[i],'017b')
    pagina = f[i][0:10]
    deslocamento = f[i][11:17]
    acesso_memoria += 1
    tempo_acesso += 0.2
    if(tab_pag[int(pagina,2)] == True):
        acerto_pagina+=1
        acesso_memoria+=1
        tempo_acesso+=0.2
    elif(tab_pag[int(pagina,2)] == False):
        falha_pagina += 1
        operacao_ES += 1
        tempo_acesso += 8
        tab_pag[int(pagina,2)] = True
print('============== SEQUENCIA 01 SEM TLB ===============')
print('Acesso memoria sequencia01 = ', acesso_memoria)
print('Acerto pagina sequencia01 = ', acerto_pagina)
print('Falha pagina sequencia01 = ', falha_pagina)
print('Operação E/S sequencia01 = ', operacao_ES)
print('Tempo de acesso sequencia01 = ', tempo_acesso/100.0, "s")

print("\n")

f = open(r'C:\Users\mateu\Documents\UFRN\8º Semestre\SO\build-gerenciamentodememoria-Desktop_Qt_5_11_1_MinGW_32bit-Debug\sequencia02.txt','r').readlines()

acerto_pagina = 0
falha_pagina = 0
acesso_memoria = 0
operacao_ES = 0
tab_pag = [False]*1024
tempo_acesso = 0

for i in range (0, len(f)):
    f[i] = int(f[i])
    f[i] = format(f[i],'017b')
    pagina = f[i][0:10]
    deslocamento = f[i][11:17]
    acesso_memoria += 1
    tempo_acesso += 0.2
    if(tab_pag[int(pagina,2)] == True):
        acerto_pagina+=1
        acesso_memoria+=1
        tempo_acesso += 0.2
    elif(tab_pag[int(pagina,2)] == False):
        falha_pagina += 1
        operacao_ES += 1
        tempo_acesso +=8
        tab_pag[int(pagina,2)] = True
print('============== SEQUENCIA 02 SEM TLB ===============')
print('Acesso memoria sequencia02 = ', acesso_memoria)
print('Acerto pagina sequencia02 = ', acerto_pagina)
print('Falha pagina sequencia02 = ', falha_pagina)
print('Operação E/S sequencia02 = ', operacao_ES)
print('Tempo de acesso sequencia02 = ', tempo_acesso/100.0, "s")

vet_tlb = [{'pag': -1, 'val': False}]*128

print("\n")

f = open(r'C:\Users\mateu\Documents\UFRN\8º Semestre\SO\build-gerenciamentodememoria-Desktop_Qt_5_11_1_MinGW_32bit-Debug\sequencia01.txt','r').readlines()

acerto_tlb = 0
falha_tlb = 0
end_tbl = 0
acerto_pagina = 0
falha_pagina = 0
acesso_memoria = 0
operacao_ES = 0
tab_pag = [False]*1024
tempo_acesso = 0
flag = False
i_tlb = 0

for i in range (0, len(f)):
    f[i] = int(f[i])
    f[i] = format(f[i],'017b')
    pagina = f[i][0:10]
    deslocamento = f[i][11:17]

    if (pagina == vet_tlb[i_tlb]['pag']) and vet_tlb[i_tlb]['val'] == True:
        acerto_tlb += 1
        flag = True
    elif (pagina != vet_tlb[i_tlb]['pag']) or vet_tlb[i_tlb]['val'] == False:
        falha_tlb += 1
        acesso_memoria += 1
        tempo_acesso += 0.2
        if(tab_pag[int(pagina,2)] == True):
            acerto_pagina += 1
            acesso_memoria += 1
            tempo_acesso += 0.2
        else:
            falha_pagina += 1
            operacao_ES += 1
            tempo_acesso += 8
            tab_pag[int(pagina, 2)] = True
        vet_tlb[i_tlb]['pag'] = pagina
        vet_tlb[i_tlb]['val'] = True
        i_tlb += 1
    if i_tlb == 128:
        i_tlb = 0


print('============== SEQUENCIA 01 COM TLB ===============')
print('Acesso memoria sequencia01 = ', acesso_memoria)
print('Acerto pagina sequencia01 = ', acerto_pagina)
print('Falha pagina sequencia01 = ', falha_pagina)
print('Operação E/S sequencia01 = ', operacao_ES)
print('Tempo de acesso sequencia01 = ', tempo_acesso/100.0, "s")
print('Acerto tlb sequencia01 = ', acerto_tlb)
print('Falha tlb sequencia01 = ',falha_tlb)


vet_tlb = [{'pag': -1, 'val': False}]*128

print("\n")

f = open(r'C:\Users\mateu\Documents\UFRN\8º Semestre\SO\build-gerenciamentodememoria-Desktop_Qt_5_11_1_MinGW_32bit-Debug\sequencia02.txt','r').readlines()

acerto_tlb = 0
falha_tlb = 0
end_tlb = 0
acerto_pagina = 0
falha_pagina = 0
acesso_memoria = 0
operacao_ES = 0
tab_pag = [False]*1024
tempo_acesso = 0
flag = False
i_tlb = 0

for i in range (0, len(f)):
    f[i] = int(f[i])
    f[i] = format(f[i],'017b')
    pagina = f[i][0:10]
    deslocamento = f[i][11:17]

    if (pagina == vet_tlb[i_tlb]['pag']) and vet_tlb[i_tlb]['val'] == True:
        acerto_tlb += 1
        flag = True
    elif (pagina != vet_tlb[i_tlb]['pag']) or vet_tlb[i_tlb]['val'] == False:
        falha_tlb += 1
        acesso_memoria += 1
        tempo_acesso += 0.2
        end_tlb+=1
        if end_tlb == 128:
            end_tlb = 0
        if(tab_pag[int(pagina,2)] == True):
            acerto_pagina += 1
            acesso_memoria += 1
            tempo_acesso += 0.2
        else:
            falha_pagina += 1
            operacao_ES += 1
            tempo_acesso += 8
            tab_pag[int(pagina, 2)] = True
        vet_tlb[end_tlb]['pag'] = pagina
        vet_tlb[end_tlb]['val'] = True
        i_tlb += 1
    if i_tlb == 128:
        i_tlb = 0


print('============== SEQUENCIA 02 COM TLB ===============')
print('Acesso memoria sequencia02 = ', acesso_memoria)
print('Acerto pagina sequencia02 = ', acerto_pagina)
print('Falha pagina sequencia02 = ', falha_pagina)
print('Operação E/S sequencia02 = ', operacao_ES)
print('Tempo de acesso sequencia02 = ', tempo_acesso/100.0, "s")
print('Acerto tlb sequencia02 = ', acerto_tlb)
print('Falha tlb sequencia02 = ',falha_tlb)

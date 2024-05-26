#coding: utf-8
#author: Alvaro A. Beck

# escreveno em um arquivo
arq = open('arqtexto.txt', 'w')
arq.write('Essa é a primeira linha do arquivo texto.\n')
arq.write('Essa é a segunda linha do arquivo texto.')
arq.close()

# lendo de um arquivo
arq = open('arqtexto.txt', 'r')
#texto = arq.readlines()
texto = arq.read()
arq.close()

print(texto)


#função recursiva
def pot(b, e):
    if e == 0:
        return 1
    return b * pot(b, e - 1)

print(pot(2, 1))

# listas - Não permitem itens repetidos
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1)
print(s2)
print(s1.union(s2))
print(s1.difference(s2))
print(s1.intersection(s2))

'''
    Criar um programa que receba parâmetros na linha de comando.
'''

import sys

def main(args):
    print(f'Script Python: {args[0]}, abaixo os argumentos passados:')
    if len(args) > 1:
        for i in range(1,len(args)):
            print(args[i])
        
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
    #main(sys.argv)
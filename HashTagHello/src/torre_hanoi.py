'''
    SOlução da Torre de Hanoi com uma função recursiva.
    https://stringfixer.com/pt/Towers_of_Hanoi
    https://panda.ime.usp.br/panda/static/pythonds_pt/04-Recursao/08-problemasComplexos.html
'''
'''
# SOlução recursiva original:
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print('Movendo o disco de', fp, 'para', tp)

# Torre de Hanoi
if __name__ == '__main__':
    moveTower(130,"A","B","C")
'''
#import multiprocessing
import threading

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        #moveTower(height-1,fromPole,withPole,toPole)
        #p = multiprocessing.Process(target=moveTower, args=(height-1,fromPole,withPole,toPole), daemon=False)
        p = threading.Thread(target=moveTower, args=(height-1,fromPole,withPole,toPole), daemon=False)
        p.start()
        #p.join()
        #moveDisk(fromPole,toPole)
        p = threading.Thread(target=moveDisk, args=(fromPole,toPole), daemon=False)
        p.start()
        #p.join()
        #moveTower(height-1,withPole,toPole,fromPole)
        p = threading.Thread(target=moveTower, args=(height-1,withPole,toPole,fromPole), daemon=False)
        p.start()
        #p.join()

def moveDisk(fp,tp):
    print('Movendo o disco de', fp, 'para', tp)

if __name__ == '__main__':
    moveTower(30,"A","B","C")

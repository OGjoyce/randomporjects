import os
import sys
import subprocess

# Soluciones
s1 = '1,6;9;15;9;9'
s2 = '2,6;9;F;9;9'
s3 = '3,J'
s4 = '4,F'
s5 = '5,F8F1F'
s6 = '6,E999E'


s7 = '[86,56,82,15,0,88] [77,11,25,2];[0, 2, 11, 15, 25, 56, 77, 82, 86, 88]'
s8 = '[61,16,67,30,43,7] [86,13];[7, 13, 16, 30, 43, 61, 67, 86]'
s9 = '[38,52] [86,12];[12, 38, 52, 86]'
s10 = '[15,93,98,41,23,93,91,99,63] [13,2];'
s10 += '[2, 13, 15, 23, 41, 63, 91, 93, 93, 98, 99]'
s11 = 'jklhasdjk 1,klmibtekl'
s12 = 'qweujoir 3,tzhxmrlu'
s13 = 'abcdefghijklmnopqrstuvwxyz 26,abcdefghijklmnopqrstuvwxyz'
s14 = 'abc 27,bcd'
s15 = 'holamundo 10,ryvkwexny'


def execute(cmd):
    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
    out, err = proc.communicate()
    return out, proc.returncode


def evaluate(total, tests, program, separator=','):
    if len(tests) == 0:
        out, returncode = execute('python ' + program)
        if (returncode != 0):
            total=0
        else:
            total-=(1000 - int(out.strip()))/25
    else:
        discount = float(total) / len(tests)
        for test in tests:
            cmd, result = test.split(separator)
            out, returncode = execute('python ' + program + ' ' + cmd)
            if not (returncode == 0 and out.strip().upper() == result):
                total -= discount
    return int(total)


def ex1():
    return evaluate(40, [s1, s2, s3,s4,s5,s6], 'ejercicio1.py')


def ex2():
    return 10 if os.path.isfile('ejercicio2.png') else 0


def ex3():
    return evaluate(40,[], 'ejercicio3.py', separator=';')


def ex4():
    return 10 if os.path.isfile('ejercicio4.png') else 0


def main(n):
    fs = [ex1, ex2, ex3, ex4]
    if n != -1:
        print('Calificando Ejercicio: {0}'.format(n))
        print('.' * 20)
        if (n == 2 or n == 4):
            print('Nota: {0}/10'.format(fs[n-1]()))
        else:
            print('Nota: {0}/40'.format(fs[n-1]()))
    else:
        total = 0
        print('Calificando Todo:\n')
        for n, ex in enumerate(fs):
            nota = ex()
            print('Calificando Ejercicio: {0}'.format(n + 1))
            print('.' * 20)
            if (n == 1 or n == 3):
                print('Nota: {0}/10'.format(nota))
            else:
                print('Nota: {0}/40'.format(nota))
            
            total += nota
            print('')
        print('TOTAL: {0}/100'.format(total))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        main(-1)
    else:
        main(int(sys.argv[1]))

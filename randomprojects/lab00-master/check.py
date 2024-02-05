import os
import sys
import subprocess

# Soluciones
s1 = '11,Fibonacci de 11: 89'
s2 = '15,Fibonacci de 15: 610'
s3 = '23,Fibonacci de 23: 28657'
s4 = '21,Fibonacci de 21: 10946'
s5 = '25,Fibonacci de 25: 75025'
s6 = '[56,55,67,60,56,33,15] [97,11,78,38];'
s6 += '[11, 15, 33, 38, 55, 56, 56, 60, 67, 78, 97]'
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
    discount = float(total) / len(tests)
    for test in tests:
        cmd, result = test.split(separator)
        out, returncode = execute('java ' + program + ' ' + cmd)
        if not (returncode == 0 and out.strip() == result):
            total -= discount
    return total


def ex1():
    return 25 if os.path.isdir('./.git') else 0


def ex2():
    return evaluate(25, [s1, s2, s3, s4, s5], 'Fibonacci')


def ex3():
    return evaluate(25, [s6, s7, s8, s9, s10], 'Zipper', separator=';')


def ex4():
    return evaluate(25, [s11, s12, s13, s14, s15], 'Perm')


def main(n):
    fs = [ex1, ex2, ex3, ex4]
    if n != -1:
        print('Calificando Ejercicio: {0}'.format(n))
        print('.' * 20)
        print('Nota: {0}/25'.format(fs[n-1]()))
    else:
        total = 0
        print('Calificando Todo:\n')
        for n, ex in enumerate(fs):
            nota = ex()
            print('Calificando Ejercicio: {0}'.format(n + 1))
            print('.' * 20)
            print('Nota: {0}/25'.format(nota))
            total += nota
            print('')
        print('TOTAL: {0}/100'.format(total))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        main(-1)
    else:
        main(int(sys.argv[1]))

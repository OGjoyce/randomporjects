#include <stdio.h>
#include <stdlib.h>

// Retorna el n-esimo bit de x
// Asuman que n esta entre 0 y 31
unsigned get_bit(unsigned x,
                 unsigned n) {
	  return (x >> n) & 1;
}

// Cambia el n-esimo bit de x por el valor dado de v
// asuman que n esta entre 0 y 31 y v es 0 o 1
void set_bit(unsigned * x,
             unsigned n,
             unsigned v) {

    (* x) = ((* x) & (0xFFFFFFFF - (1 << n))) + (v << n);
}

// Invierte el n-esimo bit del valor de x
// Asuman que n esta entre 0 y 31
void flip_bit(unsigned * x,
              unsigned n) {

   unsigned tmp = ~get_bit(*x, n);
    tmp = get_bit(tmp, 0);
    set_bit(x, n, tmp);
}

/*
 * Pueden ignorar el resto de este archivo
 */

void test_get_bit(unsigned x,
                  unsigned n,
                  unsigned expected) {
    unsigned a = get_bit(x, n);
    if(a!=expected) {
        printf("get_bit(0x%08x,%u): 0x%08x, expected 0x%08x\n",x,n,a,expected);
    } else {
        printf("get_bit(0x%08x,%u): 0x%08x, correct\n",x,n,a);
    }
}

void test_set_bit(unsigned x,
                  unsigned n,
                  unsigned v,
                  unsigned expected) {
    unsigned o = x;
    set_bit(&x, n, v);
    if(x!=expected) {
        printf("set_bit(0x%08x,%u,%u): 0x%08x, expected 0x%08x\n",o,n,v,x,expected);
    } else {
        printf("set_bit(0x%08x,%u,%u): 0x%08x, correct\n",o,n,v,x);
    }
}

void test_flip_bit(unsigned x,
                   unsigned n,
                   unsigned expected) {
    unsigned o = x;
    flip_bit(&x, n);
    if(x!=expected) {
        printf("flip_bit(0x%08x,%u): 0x%08x, expected 0x%08x\n",o,n,x,expected);
    } else {
        printf("flip_bit(0x%08x,%u): 0x%08x, correct\n",o,n,x);
    }
}

unsigned stoi(const char * str) {
    char * x = NULL;
    const long parsed = strtol(str, &x, 0);
    return x==str ? 0 : (unsigned)parsed;
}

int main(int argc,
         const char * argv[]) {

    char c[1000];
    FILE *fp;
    unsigned test_number;
    unsigned n_bit1;
    unsigned n_bit2;
    unsigned n_val;
    unsigned temp;
    if (argc > 5 && (strcmp(argv[1], "test") == 0)) {

        test_number = stoi(argv[2]);
        temp = test_number;
        n_bit1 = stoi(argv[3]);
        n_bit2 = stoi(argv[4]);
        n_val = stoi(argv[5]);
        fp = fopen("e2_sol.txt", "wb");
    	if(fp == NULL) {
    		printf("%s\n", "Error! En el archivo de salida");
    		exit(1);
    	}
    	fprintf(fp,"%d\n", get_bit(test_number, n_bit1));
        set_bit(&test_number, n_bit1, n_val);
        fprintf(fp,"%d\n", test_number);
        flip_bit(&temp, n_bit2);
        fprintf(fp,"%d", temp);
    	fclose(fp);
    } else {
        printf("\nTesting get_bit()\n\n");
        test_get_bit(0b1001110,0,0);
        test_get_bit(0b1001110,1,1);
        test_get_bit(0b1001110,5,0);
        test_get_bit(0b11011,3,1);
        test_get_bit(0b11011,2,0);
        test_get_bit(0b11011,9,0);
        printf("\nTesting set_bit()\n\n");
        test_set_bit(0b1001110,2,0,0b1001010);
        test_set_bit(0b1101101,0,0,0b1101100);
        test_set_bit(0b1001110,2,1,0b1001110);
        test_set_bit(0b1101101,0,1,0b1101101);
        test_set_bit(0b1001110,9,0,0b1001110);
        test_set_bit(0b1101101,4,0,0b1101101);
        test_set_bit(0b1001110,9,1,0b1001001110);
        test_set_bit(0b1101101,7,1,0b11101101);
        printf("\nTesting flip_bit()\n\n");
        test_flip_bit(0b1001110,0,0b1001111);
        test_flip_bit(0b1001110,1,0b1001100);
        test_flip_bit(0b1001110,2,0b1001010);
        test_flip_bit(0b1001110,5,0b1101110);
        test_flip_bit(0b1001110,9,0b1001001110);
        printf("\n");
    }

    return 0;
}

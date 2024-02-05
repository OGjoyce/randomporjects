#include <stdio.h>
#include <stdlib.h>

// Solo cambien estos 4 valores

#define V0 3
#define V1 0
#define V2 1
#define V3 3

int main(void) {
	int a;
	char *s;

	printf("Berkeley eccentrics:\n====================\n");

	for(a=0; a<V0; a++) {
		printf("Happy ");
	}
	printf("\n");

	switch(V1) {
		case 0:		printf("Yoshua\n"); break;
		case 1: 	printf("Triangle Man\n");	break;
		case 2: 	printf("Chinese Erhu Guy\n");
		case 3: 	printf("Yoshua\n");		break;
		case 4:		printf("Dr. Jokemon\n");	break;
		case 5:		printf("Hat Lady\n");
		default:	printf("I don't know these people!\n");
	}

	// Operacion ternaria
	s = (V3==3) ? "Go" : "Boo";

	if(V2) {
		printf("\n%s BEARS!\n",s);
	} else  {
		printf("\n%s CARDINAL!\n",s);
	}

	char c[1000];
	FILE *fp;
	fp = fopen("e1_sol.txt", "wb");
	if(fp == NULL) {
		printf("%s\n", "Error! En el archivo de salida");
		exit(1);
	}
	fprintf(fp,"%d\n",V0);
	fprintf(fp,"%d\n",V1);
	fprintf(fp,"%d\n",V2);
	fprintf(fp,"%d",V3);
	fclose(fp);

	return 0;
}

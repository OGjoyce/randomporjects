#include <stdio.h>
#include <stdlib.h>

#define MENU ">>Nombre del archivo: "

#define CHUNK 1024 /* read 1024 bytes at a time */
char buf[CHUNK];
FILE *file;
size_t nread;

file = fopen("test.txt", "r");
if (file) {
    while ((nread = fread(buf, 1, sizeof buf, file)) > 0)
        fwrite(buf, 1, nread, stdout);
    if (ferror(file)) {
        /* deal with error */
    }
    fclose(file);
}

int main(int argc, char* argv[]){
	if(argc == 1){
		printf(MENU);
	}
	return 0;
}
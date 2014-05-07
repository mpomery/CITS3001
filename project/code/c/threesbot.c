/**
 * threesbot - bot to play threes as best as possible
 * @file threesbot.c
 * @author Mitchell Pomery (21130887)
 */

#include <stdio.h>
#include <stdlib.h>


void usage() {
	(void) fprintf(stderr, "usage:\n\tthreesbot input output\n");
	exit(1);
}

int main(int argc, char *argv[]) {
	if (argc != 3) {
		usage();
	}
	
	// Variables
	FILE *fp;
	int board[4][4]; // Playing board
	int tiles[1024];
	
	fp = fopen(argv[1], "r"); //Open File
	
	
	char* line = (char*) malloc(1024);
	fgets(line, 1024, fp);// Read the two comment lines
	fgets(line, 1024, fp);
	free(line);
	
	
	for (int x = 0; x < 4; x++) {
		for (int y = 0; y < 4; y++) {
			int i = 0;
			fscanf(fp, "%d", &i);
			board[x][y] = i;
			printf("%i ", board[x][y]);
		}
		printf("\n");
	}
	
	int tile;
	int numtiles = 0;
	
	while (!feof(fp)) {
		fscanf(fp, "%d", &tile);
		tiles[numtiles] = tile;
		printf ("%d ", tiles[numtiles]);
		numtiles++;
	}
	
	fclose(fp);
}
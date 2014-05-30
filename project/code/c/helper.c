/*---------------------------------------------------------------*
 * helper.c                                                      *
 *                                                               *
 *     @author: Kieran Hannigan - 21151118                       *
 *---------------------------------------------------------------*
 *                                                               *
 * Please see the report for information about this project.     *
 *                                                               *
 *---------------------------------------------------------------*/

#include "threebot.h"

// Print the program usage.
void printUsage(){
	printf("\nIncorrect input arguments. Use:\n\tthreebot [inputfile.txt] [outputfile.txt]\n\n");
	exit(EXIT_FAILURE);
}

// Converts a direction to the corresponding character
char directionToCharacter(DIRECTION direction) {
	switch(direction) {
		case UP:
			return 'U';
		case RIGHT:
			return 'R';
		case DOWN:
			return 'D';
		case LEFT:
			return 'L';
		default:
			return 'N';
	}
}

// Converts an int to the corresponding direction.
DIRECTION intToDirection(int i) {
	switch(i) {
		case 0:
			return UP;
		case 1:
			return LEFT;
		case 2:
			return DOWN;
		case 3:
			return RIGHT;
	}
	return NONE;
}

// Prints a board to stdout
void printBoard(BOARD board) {
	printf("-----------------------------\n");
	for(int r=0; r<4; ++r) {
		printf("|");
		for(int c=0; c<4; ++c) {
			if(board[r][c] == 0) {
				printf("      |");
			} else {
				printf("%6i|", board[r][c]);
			}
		}
		printf("\n");
	}
	printf("-----------------------------\n");
}

/* Operation to enqueue a game */
void enqueue(PQUEUE * pqueue, GAME game) {
	GAME temp;
	int i, j;

	if (pqueue->front == MAX_GAME_SIZE - 1) {
		printf("Primary queue overflow.\n");
		exit(EXIT_FAILURE);
	} else if (pqueue->front == -1) {
		pqueue->front = 0;
	}
	pqueue->back++;
	pqueue->node[pqueue->back] = game;
	for (i = pqueue->front; i < pqueue->back; i++) {
		for (j = i + 1; j <= pqueue->back; j++) {
			// Reorganize queue
			if (pqueue->node[i].utility < pqueue->node[j].utility) {
				temp = pqueue->node[i];
				pqueue->node[i] = pqueue->node[j];
				pqueue->node[j] = temp;
			}
		}
	}
	return;
}

/* Operation to dequeue a game */
GAME dequeue(PQUEUE * pqueue) {
	if (pqueue->front == -1) {
		printf("Priority queue underflow\n");
		exit(EXIT_FAILURE);
	}
	GAME ret = pqueue->node[pqueue->front];
	pqueue->front++;
	return ret;
}

int isEmpty(PQUEUE pqueue) {
	return pqueue.front == pqueue.back;
}

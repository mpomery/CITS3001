/*---------------------------------------------------------------*
 * threebot.h                                                    *
 *                                                               *
 *     @author: Kieran Hannigan - 21151118                       *
 *---------------------------------------------------------------*
 *                                                               *
 * Please see the report for information about this project.     *
 *                                                               *
 *---------------------------------------------------------------*/

#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>
#include <sys/time.h>
#include <stdlib.h>


#define MAX_GAME_SIZE 20000		// Used to size the sequence appropriately.
#define MAX_LINE_SIZE 200 		// For when it comes to skipping the lines.

#define SEARCH_DEPTH 5 			// How deep the AI should look.


typedef enum {UP, DOWN, LEFT, RIGHT, NONE} DIRECTION;
typedef int** BOARD;		// Using uint8 for space savings.


typedef struct GAME {
	BOARD board;
	int* sequence;
	int turn;
	int turns;
	char* path;
	int utility;
} GAME;

typedef struct PQUEUE {
	GAME node[MAX_GAME_SIZE];
	int front, back;
} PQUEUE;

// Global variables
extern int moves;

// See function headers for details.

// gamestate.c function definitions.
GAME loadGame(FILE *);
GAME newGame();
void freeGame(GAME);
void copyGame(GAME *, GAME);
GAME peekTurn(GAME, DIRECTION);
void makeTurn(GAME *, DIRECTION, FILE *);

// utility.c function definitions.
int zero_count(BOARD board);
int score(BOARD board);

// helper.c function definitions.
void printUsage();
char directionToCharacter(DIRECTION);
DIRECTION intToDirection(int);
void printBoard(BOARD board);
void enqueue(PQUEUE * pq, GAME);
GAME dequeue(PQUEUE * pq);
int isEmpty(PQUEUE);

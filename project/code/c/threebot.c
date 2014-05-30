/*---------------------------------------------------------------*
* threebot.c                                                    *
*                                                               *
*     @author: Kieran Hannigan - 21151118                       *
*---------------------------------------------------------------*
*                                                               *
* Please see the report for information about this project.     *
*                                                               *
*---------------------------------------------------------------*/

#include "threebot.h"

int moves;
PQUEUE pqueue;
int nodes;

// Expands a node into the priority queue
void queueChildren(GAME game) {
	GAME up = peekTurn(game, UP);
	GAME down = peekTurn(game, DOWN);
	GAME left = peekTurn(game, LEFT);
	GAME right = peekTurn(game, RIGHT);
	up.utility = zero_count(up.board);
	down.utility = zero_count(down.board);
	left.utility = zero_count(left.board);
	right.utility = zero_count(right.board);
	enqueue(&pqueue, up);
	enqueue(&pqueue, down);
	enqueue(&pqueue, left);
	enqueue(&pqueue, right);
}

// Returns the move that maximises utility.
DIRECTION maxUtility(GAME game, GAME up, GAME down, GAME left, GAME right) {
	DIRECTION move = NONE;
	int value = 0;

	int upcount = zero_count(up.board);
	int downcount = zero_count(down.board);
	int leftcount = zero_count(left.board);
	int rightcount = zero_count(right.board);

	if((upcount >= value) && (up.turn != game.turn)) {
		value = upcount;
		move = UP;
	}
	if((downcount >= value) && (down.turn != game.turn)) {
		value = downcount;
		move = DOWN;
	}
	if((leftcount >= value) && (left.turn != game.turn)) {
		value = leftcount;
		move = LEFT;
	}
	if((rightcount >= value) && (right.turn != game.turn)) {
		value = rightcount;
		move = RIGHT;
	}

	return move;
}

// Returns the best move for a given game.
DIRECTION IDA_star(GAME game) {
	GAME up = peekTurn(game, UP);
	GAME down = peekTurn(game, DOWN);
	GAME left = peekTurn(game, LEFT);
	GAME right = peekTurn(game, RIGHT);

	if((game.turn == up.turn) && (game.turn == down.turn) && (game.turn == left.turn) && (game.turn == right.turn)) {
		freeGame(up);
		freeGame(down);
		freeGame(left);
		freeGame(right);
		return NONE;
	}

	DIRECTION move = maxUtility(game, up, down, left, right);
	freeGame(up);
	freeGame(down);
	freeGame(left);
	freeGame(right);
	return move;
}

// Play a game as best we can.
void play(GAME game, FILE * outputfile) {
	DIRECTION bestmove;
	while((bestmove = IDA_star(game))!= NONE) {
		printBoard(game.board);
		printf("%i\n", moves);
		printf("%c\n", directionToCharacter(bestmove));
		makeTurn(&game, bestmove, outputfile);
	}
}


// Program entry point.

int main(int argc, char *argv[]) {
// Check arguments.
	if(argc < 3) {
		printUsage();
	}

// Open files.
	FILE* inputfile;
	FILE* outputfile;
	if((inputfile = fopen(argv[1], "r")) == NULL) {
		printf("Error: Unable to open input file.");
		exit(EXIT_FAILURE);
	}
	if((outputfile = fopen(argv[2], "w+")) == NULL) {
		printf("Error: Unable to open output file.");
		exit(EXIT_FAILURE);
	}

// Load game.
	GAME game;
	game = loadGame(inputfile);

// Start play.
	fprintf(outputfile, "\n\n");

	struct timeval start, end;
	moves = 0;

	gettimeofday(&start, NULL);
	play(game, outputfile);
	gettimeofday(&end, NULL);

	int elapsed = 1+(end.tv_usec - start.tv_usec)/1000;

	printf("Game over. Finished %i moves in %ims (%imoves/sec).\nFinal board:\n", moves, elapsed, 1000*moves/elapsed);
	printBoard(game.board);
	printf("Score: %i\n", score(game.board));
	freeGame(game);
	fprintf(outputfile, "\n");
}

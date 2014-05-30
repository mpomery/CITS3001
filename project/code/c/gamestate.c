/*---------------------------------------------------------------*
 * gamestate.c                                                   *
 *                                                               *
 *     @author: Kieran Hannigan - 21151118                       *
 *---------------------------------------------------------------*
 *                                                               *
 * Please see the report for information about this project.     *
 *                                                               *
 *---------------------------------------------------------------*/

#include "threebot.h"

// Create an empty game.
GAME newGame() {
	GAME game;
	game.board = malloc(4*sizeof(int *));
	for(int i=0; i<4; ++i) { game.board[i] = calloc(4, sizeof(int)); }
	game.sequence = calloc(MAX_GAME_SIZE, sizeof(int));
	game.turn = 0;
	game.turns = 0;	
	return game;
}

// Free game
void freeGame(GAME game) {
	for(int i=0; i<4; ++i) {
		free(game.board[i]);
	}
	free(game.board);
	free(game.sequence);
}

// Create and return a new game based on the given input file.
GAME loadGame(FILE * inputfile) {
	// Initialise parts.
	GAME game = newGame();

	// Skip two lines.
	char line[MAX_LINE_SIZE];
	fgets(line, MAX_LINE_SIZE, inputfile);
	fgets(line, MAX_LINE_SIZE, inputfile);

	// Load next 4 lines into board.
	for(int i=0; i<4; ++i) {
		fgets(line, MAX_LINE_SIZE, inputfile);
		if(sscanf(line,"%i %i %i %i",
			&game.board[i][0],
			&game.board[i][1],
			&game.board[i][2],
			&game.board[i][3]) != 4) {
			printf("Error: Incorrectly formatted input board.\nCouldn't read the normal number of tiles.\n");
			exit(EXIT_FAILURE);
		}
		if((( game.board[i][0] != 0) &&
			 (game.board[i][0] != 1) &&
			 (game.board[i][0] != 2) &&
			 (game.board[i][0] != 3) &&
			 (game.board[i][0] != 6) &&
			 (game.board[i][3] != 12) &&
			 (game.board[i][3] != 24) &&
			 (game.board[i][3] != 48)) ||

			((game.board[i][1] != 0) &&
			 (game.board[i][1] != 1) &&
			 (game.board[i][1] != 2) &&
			 (game.board[i][1] != 3) &&
			 (game.board[i][1] != 6) &&
			 (game.board[i][3] != 12) &&
			 (game.board[i][3] != 24) &&
			 (game.board[i][3] != 48)) ||

			((game.board[i][2] != 0) &&
			 (game.board[i][2] != 1) &&
			 (game.board[i][2] != 2) &&
			 (game.board[i][2] != 3) &&
			 (game.board[i][2] != 6) &&
			 (game.board[i][3] != 12) &&
			 (game.board[i][3] != 24) &&
			 (game.board[i][3] != 48)) ||

			((game.board[i][3] != 0) &&
			 (game.board[i][3] != 1) &&
			 (game.board[i][3] != 2) &&
			 (game.board[i][3] != 3) &&
			 (game.board[i][3] != 6) &&
			 (game.board[i][3] != 12) &&
			 (game.board[i][3] != 24) &&
			 (game.board[i][3] != 48)))

			{
				printf("Error: Incorrectly formatted input board.\nStarting board tiles not in normal values (1, 2, 3, 6, 12, 24 or 48).\n");
				exit(EXIT_FAILURE);
		}
	}


	// Load remaining tiles into sequence.
	while(fscanf(inputfile, "%i", &game.sequence[game.turns]) != EOF) {
		if( (game.sequence[game.turns] != 1) && 
			(game.sequence[game.turns] != 2) && 
			(game.sequence[game.turns] != 3) && 
			(game.sequence[game.turns] != 6) && 
			(game.sequence[game.turns] != 12) && 
			(game.sequence[game.turns] != 24) && 
			(game.sequence[game.turns] != 48)) 
			{
				printf("Error: Incorrectly formatted input board.\nStarting sequence tiles not in normal values (1, 2, 3, 6, 12, 24 or 48).\n");
				exit(EXIT_FAILURE);
		}
		game.turns++;
	}

	// Housekeeping.
	fclose(inputfile);
	return game;
}

// Fill a game with the contents of another.
void copyGame(GAME * game, GAME newgame) {
	// Board.
	for(int i=0; i<16; ++i)
	{
		game->board[i/4][i%4] = newgame.board[i/4][i%4];
	}
	// Sequence.
	for(int i=0; i<MAX_GAME_SIZE; ++i) {
		game->sequence[i] = newgame.sequence[i];
	}
	// Stats.
	game->turn = newgame.turn;
	game->turns = newgame.turns;
}

// Preview a turn on a game.
GAME peekTurn(GAME game, DIRECTION direction) {
	// Initialise variables used.
	int newtile = game.sequence[game.turn];
	int shifts = 0;
	int shifted[4] = {0,0,0,0};
	int smallest[3] = {-1,-1,-1};
	int newplace;

	int better;
	int done;

	// Create a duplicate game for peeking on.
	GAME newgame = newGame();
	copyGame(&newgame, game);
	if(newtile == 0) { return newgame; }

	switch(direction) {
		case UP:
			// The shift.
			for(int r=0; r<3; ++r) {
				for(int c=0; c<4; ++c) {
					// Push 0s along.
					if(!newgame.board[r][c]) {
						if(newgame.board[r+1][c]) {
							newgame.board[r][c] = newgame.board[r+1][c];
							newgame.board[r+1][c] = 0;
							shifted[c]++;
						}
					// Combine 1s with 2s.
					} else if (newgame.board[r][c] == 1 || newgame.board[r][c] == 2) {
						if(newgame.board[r+1][c] == 3 - newgame.board[r][c]) {
							newgame.board[r][c] = 3;
							newgame.board[r+1][c] = 0;
							shifted[c]++;
						}
					// Merge duplicates.
					} else {
						if(newgame.board[r+1][c] == newgame.board[r][c]) {
							newgame.board[r][c] *= 2;
							newgame.board[r+1][c] = 0;
							shifted[c]++;
						}
					}
				}
			}
			// Count lines which changed.
			for (int c=0; c<4; ++c)
			{
				if(shifted[c]) {
					shifts++;
				}
			}
			// Exit if none did.
			if(!shifts) {
				return newgame;
			}
			// Place tile.
			for(int c=0; c<4; ++c) {
				better = 0;
				done = 0;
				if(shifted[c]) {
					if(smallest[0] == -1 && !done) {
						better = 1;
						done = 1;
					}
					if(newgame.board[2][c] > smallest[0] && !done) {
						done = 1;
					}
					if(newgame.board[2][c] < smallest[0] && !done) {
						better = 1;
						done = 1;
					}
					if(newgame.board[1][c] > smallest[1] && !done) {
						done = 1;
					}
					if(newgame.board[1][c] < smallest[1] && !done) {
						better = 1;
						done = 1;
					}
					if(newgame.board[0][c] < smallest[2] && !done) {
						better = 1;
						done = 1;
					}
				}
				if(better) {
					smallest[0] = newgame.board[2][c];
					smallest[1] = newgame.board[1][c];
					smallest[2] = newgame.board[0][c];
					newplace = c;
				}
			}
			newgame.board[3][newplace] = newtile;
			break;
		case DOWN:
			// The shift.
			for(int r=3; r>0; --r) {
				for(int c=0; c<4; ++c) {
					// Push 0s along.
					if(!newgame.board[r][c]) {
						if(newgame.board[r-1][c]) {
							newgame.board[r][c] = newgame.board[r-1][c];
							newgame.board[r-1][c] = 0;
							shifted[c]++;
						}
					// Combine 1s with 2s.
					} else if (newgame.board[r][c] == 1 || newgame.board[r][c] == 2) {
						if(newgame.board[r-1][c] == 3 - newgame.board[r][c]) {
							newgame.board[r][c] = 3;
							newgame.board[r-1][c] = 0;
							shifted[c]++;
						}
					// Merge duplicates.
					} else {
						if(newgame.board[r-1][c] == newgame.board[r][c]) {
							newgame.board[r][c] *= 2;
							newgame.board[r-1][c] = 0;
							shifted[c]++;
						}
					}
				}
			}
			// Count lines which changed.
			for (int c=0; c<4; ++c)
			{
				if(shifted[c]) {
					shifts++;
				}
			}
			// Exit if none did.
			if(!shifts) {
				return newgame;
			}
			// Place tile.
			for(int c=3; c>=0; --c) {
				better = 0;
				done = 0;
				if(shifted[c]) {
					if(smallest[0] == -1) {
						better = 1;
						done = 1;
					}
					if(newgame.board[1][c] > smallest[0] && !done) {
						done = 1;
					}
					if(newgame.board[1][c] < smallest[0] && !done) {
						better = 1;
						done = 1;
					}
					if(newgame.board[2][c] > smallest[1] && !done) {
						done = 1;
					}
					if(newgame.board[2][c] < smallest[1] && !done) {
						better = 1;
						done = 1;
					}
					if(newgame.board[3][c] < smallest[2] && !done) {
						better = 1;
						done = 1;
					}
				}
				if(better) {
					smallest[0] = newgame.board[1][c];
					smallest[1] = newgame.board[2][c];
					smallest[2] = newgame.board[3][c];
					newplace = c;
				}
			}
			newgame.board[0][newplace] = newtile;
			break;
		case LEFT:
			// The shift.
			for(int c=0; c<3; ++c) {
				for(int r=0; r<4; ++r) {
					// Push 0s along.
					if(!newgame.board[r][c]) {
						if(newgame.board[r][c+1]) {
							newgame.board[r][c] = newgame.board[r][c+1];
							newgame.board[r][c+1] = 0;
							shifted[r]++;
						}
					// Combine 1s with 2s.
					} else if (newgame.board[r][c] == 1 || newgame.board[r][c] == 2) {
						if(newgame.board[r][c+1] == 3 - newgame.board[r][c]) {
							newgame.board[r][c] = 3;
							newgame.board[r][c+1] = 0;
							shifted[r]++;
						}
					// Merge duplicates.
					} else {
						if(newgame.board[r][c+1] == newgame.board[r][c]) {
							newgame.board[r][c] *= 2;
							newgame.board[r][c+1] = 0;
							shifted[r]++;
						}
					}
				}
			}
			// Count lines which changed.
			for (int r=0; r<4; ++r)
			{
				if(shifted[r]) {
					shifts++;
				}
			}
			// Exit if none did.
			if(!shifts) {
				return newgame;
			}
			// Place tile.
			for(int r=3; r>=0; --r) {
				better = 0;
				done = 0;
				if(shifted[r]) {
					if(smallest[0] == -1) {
						better = 1;
						done = 1;
					}
					if(newgame.board[r][2] > smallest[0] && !done) {
						done = 1;
					}
					if(newgame.board[r][2] < smallest[0] && !done) {
						better = 1;
						done = 1;
					}
					if(newgame.board[r][1] > smallest[1] && !done) {
						done = 1;
					}
					if(newgame.board[r][1] < smallest[1] && !done) {
						better = 1;
						done = 1;
					}
					if(newgame.board[r][0] < smallest[2] && !done) {
						better = 1;
						done = 1;
					}
				}
				if(better) {
					smallest[0] = newgame.board[r][2];
					smallest[1] = newgame.board[r][1];
					smallest[2] = newgame.board[r][0];
					newplace = r;
				}
			}
			newgame.board[newplace][3] = newtile;
			break;
		case RIGHT:
			// The shift.
			for(int c=3; c>0; --c) {
				for(int r=0; r<4; ++r) {
					// Push 0s along.
					if(!newgame.board[r][c]) {
						if(newgame.board[r][c-1]) {
							newgame.board[r][c] = newgame.board[r][c-1];
							newgame.board[r][c-1] = 0;
							shifted[r]++;
						}
					// Combine 1s with 2s.
					} else if (newgame.board[r][c] == 1 || newgame.board[r][c] == 2) {
						if(newgame.board[r][c-1] == 3 - newgame.board[r][c]) {
							newgame.board[r][c] = 3;
							newgame.board[r][c-1] = 0;
							shifted[r]++;
						}
					// Merge duplicates.
					} else {
						if(newgame.board[r][c-1] == newgame.board[r][c]) {
							newgame.board[r][c] *= 2;
							newgame.board[r][c-1] = 0;
							shifted[r]++;
						}
					}
				}
			}
			// Count lines which changed.
			for (int r=0; r<4; ++r)
			{
				if(shifted[r]) {
					shifts++;
				}
			}
			// Exit if none did.
			if(!shifts) {
				return newgame;
			}
			// Place tile.
			for(int r=0; r<4; ++r) {
				better = 0;
				done = 0;
				if(shifted[r]) {
					if(smallest[0] == -1) {
						better = 1;
						done = 1;
					}
					if(newgame.board[r][1] > smallest[0] && !done) {
						done = 1;
					}
					if(newgame.board[r][1] < smallest[0] && !done) {
						better = 1;
						done = 1;
					}
					if(newgame.board[r][2] > smallest[1] && !done) {
						done = 1;
					}
					if(newgame.board[r][2] < smallest[1] && !done) {
						better = 1;
						done = 1;
					}
					if(newgame.board[r][3] < smallest[2] && !done) {
						better = 1;
						done = 1;
					}
				}
				if(better) {
					smallest[0] = newgame.board[r][1];
					smallest[1] = newgame.board[r][2];
					smallest[2] = newgame.board[r][3];
					newplace = r;
				}
			}
			newgame.board[newplace][0] = newtile;
			break;
		case NONE:
			break;
	}

	newgame.turn++;
	return newgame;
}

// Make the turn on a game, and write this to the output.
void makeTurn(GAME * game, DIRECTION direction, FILE * outputfile) {
	GAME newgame = peekTurn(*game, direction);
	copyGame(game, newgame);
	fputc(directionToCharacter(direction), outputfile);
	moves++;
	freeGame(newgame);
}


/*---------------------------------------------------------------*
 * utility.c                                                     *
 *                                                               *
 *     @author: Kieran Hannigan - 21151118                       *
 *---------------------------------------------------------------*
 *                                                               *
 * Please see the report for information about this project.     *
 *                                                               *
 *---------------------------------------------------------------*/

#include "threebot.h"

// Simple heuristic that counts the zeroes on the board
int zero_count(BOARD board) {
	int thisutility = 0;
	for(int i=0; i<16; i++) {
		thisutility += (board[i/4][i%4] == 0);
	}
	return thisutility;
}

// Scores game
int score(BOARD board) {
	int score = 0;
	for(int i=0; i<16; i++) {
		int tile = board[i/4][i%4];
		if(tile >= 3) {
			score += pow(3,(log2(tile/3) + 1));
		} else if (tile) {
			score ++;
		}
	}
	return score;
}
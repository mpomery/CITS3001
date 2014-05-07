base_dir = $(shell pwd)
flags = -std=c99 -funsigned-char -Wall -fstack-protector -Wformat-security \
	-Winit-self -Werror -Wl,-O1

all:
	gcc $(flags) threesbot.c -o threesbot
	threesbot testin.txt testout.txt
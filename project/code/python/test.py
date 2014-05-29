from os import listdir
from os.path import isfile, join
import threesbot

mypath = "in/"

def main():
	files = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
	for file in files:
		print("Input: " + file)
		threesbot.main(mypath + file, "out/" + file)

if __name__ == '__main__':
	main();
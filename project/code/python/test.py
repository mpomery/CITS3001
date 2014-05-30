from os import listdir
from os.path import isfile, join
import threesbot
import time

mypath = "in/"
functime = 1

def timing(f):
	def wrap(*args):
		global functime
		
		ret = f(*args)
		time2 = time.time()
		functime = (time2-time1)*1000.0
		print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
		return ret
	return wrap

def main():
	files = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
	for function in [threesbot.astarcurrent, threesbot.naive, threesbot.astarnaive]:
		for file in files:
			time1 = time.time()
			(score, moves) = threesbot.main(mypath + file, "out/" + file, function)
			time2 = time.time()
			functime = (time2-time1)*1000.0
			print(function.__name__ + "," + file + "," + str(functime) + "," + str(score) + "," + str(len(moves)))

if __name__ == '__main__':
	main();
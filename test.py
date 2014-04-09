import time
import sys
import os
import inspect

def runtest(functions, dataset):
	for function in functions:
		func = getattr(mod, function)
		success = 0
		failure = 0
		print "Test Of " + function
		starttime = time.clock()
		for data in dataset:
			value = func(*data[0])
			if value in data[1]:
					success += 1
			else:
				failure += 1
				print "Failure"
				print "Arguments: " + str(data[0])
				print "Expected:  " + str(data[1])
				print "Output:    " + str(value)
				print ""
		endtime = time.clock()
		print ""
		print "Successes: " + str(success)
		print "Failures:  " + str(failure)
		print "Accuracy:  " + str(success / (success + failure) * 100) + "%"
		print "Time :     " + str(endtime - starttime) + "s"
		print "-" * 40

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print "Usage: " + str(sys.argv[0]) + " <directory> <testfile>"
	else:
		os.chdir(sys.argv[1])
		sys.path.insert(0, os.getcwd())
		
		testfile = __import__(sys.argv[2], globals())
		mod = __import__(testfile.fname, globals())
		runtest(testfile.functions, testfile.dataset)

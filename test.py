import time
import sys
import os
import inspect

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print "Usage: " + str(sys.argv[0]) + " <directory> <testfile>"
	else:
		os.chdir(sys.argv[1])
		sys.path.insert(0, os.getcwd())
		
		testfile = __import__(sys.argv[2], globals())
		mod = __import__(testfile.fname, globals())

		for function in testfile.functions:
			func = getattr(mod, function)
			success = 0
			failure = 0
			print "Test Of " + function
			starttime = time.clock()
			for data in testfile.dataset:
				value = func(*data[0])
				if value == data[1]:
					success += 1
				else:
					failure += 1
					print "Failure " + str(data)
					print str(value)
					print ""
			endtime = time.clock()
			print ""
			print "Successes: " + str(success)
			print "Failures:  " + str(failure)
			print "Accuracy:  " + str(success / (success + failure) * 100) + "%"
			print "Time :     " + str(endtime - starttime) + "s"
			print "-" * 40

import time
import sys

from lcs_test import *

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print "Usage: " + str(sys.argv[0]) + " <testfile>"
	else:
		testfile = __import__(sys.argv[1], globals())
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
					print "Failure " + data
					print value
					print ""
			endtime = time.clock()
			print ""
			print "Successes: " + str(success)
			print "Failures:  " + str(failure)
			print "Accuracy:  " + str(success / (success + failure) * 100) + "%"
			print "Time :     " + str(endtime - starttime) + "s"
			print "-" * 40

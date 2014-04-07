from lcs_test import *
import time

mod = __import__(fname, globals())

print mod

for function in functions:
	func = getattr(mod, function)
	success = 0
	failure = 0
	starttime = time.clock()
	for data in dataset:
		value = func(*data[0])
		if value == data[1]:
			success += 1
		else:
			failure += 1
	endtime = time.clock()
	print "Test Of " + function
	print "Successes: " + str(success)
	print "Failures:  " + str(failure)
	print "Accuracy:  " + str(success / (success + failure) * 100) + "%"
	print "Time :     " + str(endtime - starttime) + "s"

import time

from sys import argv

script, first = argv
 
print "you entered %r seconds." % seconds

#calculate hours
start = time.time()
hours = int(seconds) / 60 / 60

minutes = int(seconds) / 60 % 60
stop = time.time()

print "Hours: %r." % hours
print "minutes: %r." % minutes

tot = stop - start
print "It took me %r seconds to process this calculation!" % tot

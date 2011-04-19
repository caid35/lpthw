# now.py
import datetime
now = datetime.datetime.now()
print "Now is", now.strftime("%d-%m-%Y"), "at", now.strftime("%H:%M")
print "or, more precisely, %s" % now

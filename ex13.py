from sys import argv

script, sporks, forks, straws, spoons, knives = argv

print "The script is called:", script
print "Your first variable is:", sporks
print "Your second variable is:", forks
print "Your third variable is:", straws
print "Your fourth variable is:", spoons
print "Your fifth variable is:", knives
sixth = raw_input("enter a sixth variable.")
print "You entered %r, wooo!." % sixth

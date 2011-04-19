from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you hate me %s?" % user_name
hate = raw_input(prompt)

print "Where did you die %s?" % user_name
die = raw_input(prompt)

print "What kind of cheese do you like?"
cheese = raw_input(prompt)

print """
Alright, so you said %r about hating me.
You died in %r. Not sure where that is.
And you like %r cheese. Nice.
""" % (hate, die, cheese)

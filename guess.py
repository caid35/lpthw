#!usr/bin/python

print "Guess the number!"

def test():
    x = int(raw_input("Please type a number: "))
    if x==4:
        print "You guessed correctly. The number is four."
    else:
        if x<4:
            print "A little higher maybe..."
            test()
        if x>4:
            print "A little lower maybe..."
            test()
        else:
            print "Try typing a number, hm?"
            test()

test()
    

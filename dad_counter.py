import time



count = raw_input("count to what? ")
start = time.time()
for i in range(int(count)):
    print "counter: %d", i
    time.sleep(1)

stop = time.time()

seconds = stop - start

print "it took this many seconds: %d", seconds

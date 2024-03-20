# print 1-100
# multiples of three print "Fizz"
# multiples of five print "Buzz"
# multiples of both three and five print "FizzBuzz"

for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
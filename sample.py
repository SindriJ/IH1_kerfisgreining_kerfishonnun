
#Fizzbuzz prógram
#Tekur inn int, skilar Buzz ef talan er deilanleg með 5, Fizz ef hún er deilanleg með 3. 
#Ef talan er bæði deilanleg með 3 og 5 skilar fallið FizzBuzz
#Ef talan deilist hvorki með 3 eða 5 þá skilar fallið tölunni til baka.


def fizzbuzz(int):
    if int %3 == 0 and int%5 == 0:
        return "FizzBuzz"
    elif int %5  == 0:       
        return "Buzz"
    else:
        return None

# prufa = fizzbuzz(12)
# print (prufa)


def func(x):
    return x + 1


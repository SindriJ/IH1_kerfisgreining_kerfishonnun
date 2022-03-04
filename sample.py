
#Fizzbuzz prógram
#Tekur inn int, skilar Buzz ef talan er deilanleg með 5, Fizz ef hún er deilanleg með 3. 
#Ef talan er bæði deilanleg með 3 og 5 skilar fallið FizzBuzz
#Ef talan deilist hvorki með 3 eða 5 þá skilar fallið tölunni til baka.


def fizzbuzz(int):
    if int == 0: 
        return int
    elif int %3 == 0 and int%5 == 0:
        return "FizzBuzz"
    elif int %5  == 0:       
        return "Buzz"
    elif int %3 == 0:
        return "Fizz"
    else:
        return int





#Geri test fyrir hvert req.
# 1. "FizzBuzz" if the input number is divisible by 5 and 3
# 2. "Buzz" if the input number is divisible by 5
# 3. "Fizz" if the input number is divisible by 3
# 4. The input number itself if none of the other statements are true.


from sample import fizzbuzz
from sample import func

def test_FizzBuzz():
    for i in [15,30]:
        assert fizzbuzz(i) == 'FizzBuzz'




# content of test_sample.py
# def func(x):
#     return x + 1


# def test_answer():
#     assert func(3) == 5

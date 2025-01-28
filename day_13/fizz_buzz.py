# Find the bug
# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        # mod for 3 and 5 was 3 OR 5
        if number % 3 == 0 and number % 5 == 0:
            print(f"FizzBuzz")
        elif number % 3 == 0:
            print(f"Fizz")
        elif number % 5 == 0:
            print(f"Buzz")
        else:
            # f print was not being used, and the number was in square brackets
            print(f"{number}")
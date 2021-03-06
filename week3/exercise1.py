# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""




def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from just using range()
    """
    Space = []
    while start<stop:
        Space.append(start)
        start = start + step
    return Space




def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    Space = []
    while start<stop:
        Space.append(start)
        start = start + step
    return Space



def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    Space = []
    while start<stop:
        Space.append(start)
        start = start + 2
    return Space


def gene_krupa_range(start, stop, even_step, odd_step):
    """Make a range that has two step sizes.

    make a list that instead of having evenly spaced steps
    has odd steps be one size and even steps be another.
    """
    Space = []
    while start<stop:
        Space.append(start)
        start = start + odd_step
    return Space



def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """
    print("Pick a number")
    while True:
        guess = int(input())
        if guess < low or guess > high: 
            print("Pick another number")
        else:
            return guess

def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    message = "give me a number: "
    while True:
        try:
            guess = int(input(message))
            print("{} is a number".format(guess))
            return guess
        except Exception as e:
            print("try again {}".format(e))


def super_asker(low, high):
    """Robust asking function.

    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
    """
    message = "Please enter a number: "
    while True:
        try:
            guess = int(input(message))
            print("{} is a number".format(guess))
            return guess
        except Exception as e:
            print("{} is not a number, please enter a number only".format(e))
    if guess < low or guess > high:
        print("{} is outside the bound".format(guess))
    else:
        return guess


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\ngene_krupa_range", gene_krupa_range(1, 20, 2, 5))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)

"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform 

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# I thinkk this will assign some_words to a set of 'chips'
some_words = ['what', 'does', 'this', 'line', 'do', '?'] 
#this will print all the strings in the sety 
for word in some_words:
    print(word)
#this will print all the strings in the set
for x in some_words:
    print(x)
# this will print all the strings in the set with square bracket
print(some_words)
#this will test if the set has more than 3 strings
if len(some_words) > 3:
    print('some_words contains more than 3 words')
#assign usefulFunction as a function
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    #prints six attributes
    print(platform.uname())
#calls the function
usefulFunction()

#Using the "input" method in Python, ask a user to input a sentence. Then develop a function that accepts a the user input and will tell you how many words are in that string. First write out your plan in Pseudo-code using comments. Then craft the function.
def setence_spliter():
    give = input('Give me a sentence: ')
    word = give.split()
    print(len(word))

setence_spliter()
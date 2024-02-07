""" a = ("Chan" "is" "cheating" "on" "Maria" "with" "Jason")
print(a) """

#Boolean
""" is_Chan_cheating_on_Maria = input("Is Chan cheating on Maria with Jason?")
if is_Chan_cheating_on_Maria == "Yes":
    print("Yes he is")
elif is_Chan_cheating_on_Maria == "No":
    print("You are wrong")
else:
    print("IT IS A YES OR NO QUESTION!") """

#odd or even
""" odd_or_even = int (input ("Give me a number:") )
if ((odd_or_even) % 2) == 0: 
    print ("I think the number is even")
else:
    print ("I hope the number is odd") """

#tip
""" def bill():
  global bill
  print("What is your bill?")
  bill = float(input("> $"))


def tip():
  print("How as the service?")
  service = input(">")
  if ((service) == "bad"):
    print("You broke! No tip.")
  elif ((service) == "okay"):
    print(f"The reccomended tip is {bill*float(0.15)}")
  elif ((service) == "good"):
    print(f"The reccomended tip is {bill*float(0.20)}")
  elif ((service) == "great"):
    print(f"Thank you. for the amazin tip of {bill*float(0.25)}")
bill()
tip()
 """

#factor
""" number = int(input("Give me a number:"))

def factor():
    for i in range (1, number + 1):
        if number % i == 0:
            print (i)

factor() """

#Greatest Common Factor
number1 = int(input("Give me your first number:"))
def greatest_common_factor1():
    for i in range (1, number1 + 1):
        if number1 % i == 0:
            print (i)
greatest_common_factor1()

number2 = int(input("Give me your second number:"))
def greatest_common_factor2():
    for x in range (1, number1 + 1):
        if number1 % x == 0:
            print (x)
greatest_common_factor2()


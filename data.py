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

def bill():
    global bill
    print ("What is your bill?")   
    bill = float(input("> $"))
    
def tip():
    print("How as the service?")
    service = input(">")
    if ((service) == "bad"):
        print("You broke! No tip.")
    elif((service) == "okay"):
        print(f"The reccomended tip is {bill*float(0.15)}")
bill()
tip()
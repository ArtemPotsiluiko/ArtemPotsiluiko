
People = {
    "1": "15",
    "2": "16",
    "3": "17",
    "4": "18",
    "5": "19"}
try:
    person = input("enter your person: ")
    print("your age:", People[person])
except KeyError:
    print("Error")


# Python
# In Football Terms

# declaring variables 
name = "martin"
surname = "odegaard"
age = 22
height = 1.78
preferred_foot = 'L'

# printing variables 
print("name:", name)
print("surname:", surname)
print("age:", age)
print("height(meters):", height)
print("preferred foot:", preferred_foot)

# declaring and printing multiple variables 
j = "gabriel jesus"
k = "eddie nketiah"
l = "gabriel martinelli"

print(j, k, l)

# types
print(type(name)) # str
print(type(height)) # flo
print(type(age)) # int

# list types
starting_eleven = ["nketiah", "saka", "martinelli", "odegaard", "xhaka", "partey", "tomiyasu", "tierney", "white", "gabriel", "ramsdale"]
print(starting_eleven)
print("forwards:", starting_eleven[0:3])
print("midfielders:", starting_eleven[3:6])
print("defenders:", starting_eleven[6:10])
print("goalkeeper:", starting_eleven[10])

a = "elneny"
b = "cedric"
c = "tavares"

substitutes = [a, b, c]
substitutes.append("balogun")
print(substitutes)

english_players = [starting_eleven[0], starting_eleven[1], starting_eleven[8]]
print(english_players)

# dictionaries
goals = {"nketiah": 17, "saka": 11, "martinelli": 8, "odegaard": 7}
print(goals)
print(goals.values())
print("Arsenal's top goal scorers were:", goals.keys())
print("Arsenal's attackers scored:", sum(goals.values()))

# tuples
kit_colors = ("red", "blue", "white")
days_of_the_week = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")
months_of_the_year = (
    "jan", 
    "feb", 
    "mar", 
    "apr",
    "may",
    "jun",
    "jul",
    "aug", 
    "sep", 
    "oct", 
    "nov",
    "dec",
)

# functions
def what_do_we_think_of_tottenham():
    print("sh*t")

what_do_we_think_of_tottenham()

def what_do_we_think_of_shit():
    print("tottenham")

what_do_we_think_of_shit()

def average_age(age):
    average_age = sum(age)/len(age)
    return average_age

avg_age = average_age([22, 23, 34, 24])
print(avg_age)



# conditional statements
def performance_index(goals_and_assists):
    if goals_and_assists > 20:
        return "good season"
    elif goals_and_assists > 25:
        return "great season"
    elif goals_and_assists > 30:
        return "superb season"

print(performance_index(22))

# user input 
# user_input = input("What team do you support? ")
# print(user_input.upper())

# loops
for players in starting_eleven:
    print(players)

i = 0
while i < 5:
    print("Arsenal are the biggest club in london")
    i=i+1


# list comprehensions 
squad_ages = [22, 34, 21, 37, 40, 20, 19, 17, 18]
even_ages = [age % 2 == 0 for age in squad_ages]
print(even_ages)






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





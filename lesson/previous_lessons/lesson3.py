#Dictionary
users = ["Tom", "Alice", "Bod"] # simple list

users_dictionary = {1: "Tom", 2: "Alice", 3: "Bod", 4:  "Tom"}

# creating empty list
l = []
l = list()

#creating emty dictionary
d = {}
d = dict()

print(user_dict[45])
print(user_dict[56])


print(l[3])


# get items
# add items
# set items
# delete items 

#CRUD - create, read, update, delete
#=========================================
user_dict[474] = "Meerim" # add data t dictionary

res = 474 in user_dict


item = user_dict[3463] #exception KeyError

item = user_dict.get(34634) # None

item = user_dict.get(56432134654, "Unknown")

#=========================================
del user_dict[2466]
pop user_dict[2466]




 
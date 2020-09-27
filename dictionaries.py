# A dictionary is a container/collection that stores ordered data.
# supports indexed;
# It maps the key -> value pair
# It is mutable, or changeable
# * It does not allow duplicate members.
# * represented by {}
# stores a (key, value) pair.


# car = {
#   'name' : 'Audi',
#   'model': 'A8L',
#   'Country' : 'germany'
# }
# Key -> name, model, country
# Values -> Audi, A8L, germany
# print(car)


# get the length of dictionaries: Number of keys!
# print(len(car))


# Copying dictionary into another dictionary:
# car_collections = car.copy()
# print(car_collections)

# Get a value of a key: dict[key] -> value
# .get('key') method:
# print(car['name'])
# print(car.get('model'))

# Add another (key,value) pair;
# car['tagline'] = "Vorsprung durch tecnik"
# print(car)

# It does not allow duplicate items:
# car['name'] : "BMW"
# print(car)

# To remove (key, value) pair:
# del(car['model'])
# print(car)

# car.pop('name')
# print(car)

# To delete the entire key, value: .clear()
# car.clear()
# print(car)


# tuple of dictionary:
# tu_dict = ({'name' : None},{'country' : "USA", 'license': "LAX31423"},{'Fav-Place': "California", 'partner': "Akanksha"})
# print(tu_dict)

# list of dictionaries
# list = [{'name' : "Sanatan", 'Age': 22, 'Gender': 'M'}]
# print(list[0].get('name'))
# print(list[0]['name'])

'''
special functions:
'''
# to get the items (keys and values):
dict = {
  'name' : "Cassandra",
  'App' : "DB",
  'Dev' : 'Facebook',
  'year' : 2004
}
# Returns a list containing a tuple for each key, value pair
# print(dict.items())

# to get all the keys:
# Returns a list containing the dictionary's keys
# print(dict.keys())

# to get all the values
# Returns a list containing the dictionary's values
# print(dict.values())

# to remove the last inserted key, pair: popitem();
# dict.popitem()
# print(dict)


# Update the value of a specific key: if key is present, it will update the value, if not present it will create key that we give.
# dict.update({'year' : 2006})
# print(dict)

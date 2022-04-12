#Complete methods of Dictionary from w3schools

#clear() 
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.clear()
print("clear(): \n", car)


#copy()
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.copy()
print("copy(): \n", x)


#fromkeys()
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)
print("fromkeys(): \n", thisdict)


#get()
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.get("model")

print("get(): \n", x)


#items()
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.items()

print("items(): \n", x)


#keys()
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.keys()

print("keys(): \n", x)


#pop()
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.pop("model")

print("pop(): \n", car)


#popitem()
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.popitem()

print("popitem(): \n", car)


#setdefault()
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.setdefault("model", "Bronco")

print("setdefault(): \n", x)


#update()
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.update({"color": "White"})

print("update(): \n", car)


#values()
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.values()

print("values(): \n", x)



# creating 
my_dict1 = {
        
        "name": "vinay", "age": 24, "weight": 65
};

print(my_dict1)

my_dict2 = dict(name="Alice", age = 25);
print(my_dict2)

# Accessing
print(my_dict1["name"])
print(my_dict1.get("name"))

# adding
my_dict1["email"] = "vinayyalla@gmail.com";
print(my_dict1)

my_dict2.update({"City":"Bangalore"})
print(my_dict2)


# Remove or delete application

del my_dict1["email"];
print(my_dict1);

result = my_dict2.pop("name");
print(result);

print(my_dict2); 
my_dict1.popitem();

my_dict1.clear()


# information

print(my_dict1.keys())
print(my_dict1.values());

print(my_dict1.items());

# copy
my_dict1 = my_dict1.copy();




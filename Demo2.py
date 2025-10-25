# Below is example of list datatype in python
values = [1, 2, "Mrinmoy", 4, 5]
print(values)
print(values[0])
print(values[1])
print(values[2])
print(values[3])
print(values[4])
print(values[-1])
print(values[2:4])
values.insert(3, "Biswas")
print(values)
values.append("End")
print(values)
values[2] = "Kumar"
print(values)
del values[2]
print(values)

# ==============================
# Below is example of tuple datatype in python
val = (1, 2, "Mrinmoy", 4.5)
print(val)
print(type(val))
# ==============================
# ==============================
# Below is example of dictionary datatype in python
dic = {"a": 2, 4: "bcd", "c": "Hello World"}
print(dic)
print(dic[4])
print(dic["c"])

# Below is example of creating a dictionary at runtime and add values to it
dict = {}
dict["first_Name"] = "Mrinmoy"
dict["last_Name"] = "Biswas"
print(dict["first_Name"])
print(dict["last_Name"])

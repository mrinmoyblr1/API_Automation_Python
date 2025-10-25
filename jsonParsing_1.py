import json

# tuple, List and Dictionary will be used in JSON parsing
courses = '{"name":"Mrinmoy","languages":["Java","Python"]}'  # loads() method parse JSON string and it returns dictionary object
dict_courses = json.loads(courses)  # It will convert to dictionary
print(type(dict_courses))
print(dict_courses)

print(dict_courses["name"])

list_language = dict_courses["languages"]
print(list_language)
print(type(list_language))
print(list_language[0])  # It will print first value from the LIST

print(dict_courses["languages"][0])  # It will print first value from Dictionary
print(dict_courses["languages"][1])  # It will print second value  rom Dictionary

# Output
# => python3 jsonParsing.py
# <class 'dict'>
# {'name': 'Mrinmoy', 'languages': ['Java', 'Python']}
# Mrinmoy
# ['Java', 'Python']
# <class 'list'>
# Java
# Java
# Python
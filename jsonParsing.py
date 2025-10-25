import json

# ***** Parse content present in the JSON file
with open('course.json') as f:
    # It wil open the JSON file
    # Here if we do not mention anything then by default it will open in READ mode!
    data = json.load(f)
    # It will store in dictionary
    # In case of loads() we need to provide direct JSON string but in case of load() we need to provide external file object.
    print(type(data))
    print(data)

    print(data['courses'][1]['title'])

    print(data['dashboard']['website'])

    # Print Price of course RPA
    print("")
    print("Print Price of course RPA.....")
    print("")
    print(type(data['courses']))
    print(data['courses'])

    for course in data['courses']:
        if course['title'] == 'RPA':
            print(course['price'])
            assert course['price'] == 45


# Compare two JSON file and check the deference:
with open('course.json') as f1:
    data1 = json.load(f1)

# Opening the second json file
with open('course1.json') as f2:
    data2 = json.load(f2)
    # Compare both the JSON files
    print(data1 == data2)  # It will true if both the JSON are same
    assert data1 == data2

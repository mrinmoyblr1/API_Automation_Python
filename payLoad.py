from utilities.configurations import *


def addBookPayload(isbn, aisle):
    body = {
        "name": "Learn Appium Automation with Java 8",
        "isbn": isbn,
        "aisle": aisle,
        "author": "MKB"
    }
    # It returns a Dictionary
    return body


def buildPayloadFromDB(query):
    addBody = {}  # It is a Dictionary
    tp = getQuery(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    print("The newly created dictionary payload is: ")
    print(addBody)

    return addBody

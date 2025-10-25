import requests

from utilities.configurations import getConfig
from utilities.resources import ApiResources


def after_scenario(context, scenario):
    if "library" in scenario.tags:
        # Like this we can control after hook invocation based on the tags under feature file
        url2 = getConfig()['API']['endpoint'] + ApiResources.deleteBook
        response_deleteBook = requests.post(url2, json={"ID": context.bookID}, )

        print(response_deleteBook.status_code)
        assert response_deleteBook.status_code == 200
        res_json = response_deleteBook.json()
        print(res_json['msg'])
        assert res_json['msg'] == "book is successfully deleted"

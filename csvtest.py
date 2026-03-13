import csv


reader = csv.DictReader(open('categories.csv', 'r', newline=''))
categories = list(reader)


def SearchCategory(category):
    for item in categories:
        if item['name'] == category:
            return item['category']


print(SearchCategory('Fence'))

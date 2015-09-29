# your code goes here

def compile_restaurant_data(restaurant_data):
    restaurants = {}

    open_file = open(restaurant_data)

    for line in open_file:
        strip_line = line.rstrip()
        split_line = strip_line.split(":")

        restaurants[split_line[0]] = split_line[1]

    return restaurants

def format(ratings):
    for item in sorted(ratings.items()):
        print '{} is rated at {}'.format(item[0], item[1])

get_data = compile_restaurant_data("scores.txt")

format(get_data)
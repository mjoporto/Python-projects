capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nested List in Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

travel_log = {
   "France": {
       "num_times_visited": 8,
       "cities_visited" : ["Paris", "Lille", "Dijon"],
       "Total_visits": 12
   },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}


#print Lille


nested_list = ["A", "B", ["C", "D"]]
print(travel_log["Germany"]["cities_visited"][2])

starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

# for key in dict:
#     dict[key] +=1



#print(dict)
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
print(order["main"][2][0])
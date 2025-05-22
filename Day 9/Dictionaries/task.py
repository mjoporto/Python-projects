programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
#Add things to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

#creating empty dictionary
empty_dictionary = {}
#wipe existing dictionary
programming_dictionary = {}
#edit item in dictionary
programming_dictionary["Bug"] = "replaced data"
#loop through dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

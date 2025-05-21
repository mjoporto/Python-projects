# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

#functions with more than one input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Jack Bauer", "Nowhere")

#To specify parameters without need for order
greet_with(location="Nowhere", name="Jack Bauer")




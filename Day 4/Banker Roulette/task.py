
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#1st option
print(random.choice(friends))

#2nd option
random_index = random.randint(0,len(friends)-1)
print(friends[random_index])
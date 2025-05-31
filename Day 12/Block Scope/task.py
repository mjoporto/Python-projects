game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

#coding challenge

#def is_prime(num):
    # prime = ""
    # if num != 0 and num != 1:
    #     if num ==2:
    #         return True
    #     for i in range(2, num):
    #         if (num % i) == 0:
    #             print(num, "is not a prime number")
    #             print(f"{i}, times, {num}//{i}, is , {num}")
    #             print("inside")
    #             return False
    #         else:
    #             return True
    #
    # else:
    #     return False
    #
     def is_prime(num):

        if num != 0 and num != 1:
            if num == 2:
                return True
            for i in range(2, num):
                if (num % i) == 0:
                    print(num, "is not a prime number")
                    print(f"{i}, times, {num}//{i}, is , {num}")
                    return False

                else:
                    flag = True
        else:
            return False
        return flag
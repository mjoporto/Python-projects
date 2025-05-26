def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AnGEla", "YU"))

#leap year test
# def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    # leap_year = ""
    # divisible_by_4 = year % 4
    # if divisible_by_4 == 0:
    #     divisible_by_100 = year % 100
    #     if divisible_by_100 == 0:
    #         divisible_by_400 = year % 400
    #         if divisible_by_400 == 0:
    #             leap_year = True
    #             return leap_year
    #         else:
    #             leap_year = False
    #             return leap_year
    #     else:
    #         leap_year = True
    #         return leap_year
    # else:
    #     leap_year = False
    #     return leap_year
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AnGEla", "YU"))
def is_leap_year(year):
    """
    Take a year and return True if it is a leap year
    :param year: int - year to check
    :return: bool - True if it is a leap year, else False
    """

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

is_leap_year(2006)
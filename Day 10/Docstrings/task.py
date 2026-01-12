def format_name(f_name, l_name):
    """"
    Formats adds first and last name into a string with correctly formatted name
    :param f_name: string
    :param l_name: string
    :return: string with formatted name
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)




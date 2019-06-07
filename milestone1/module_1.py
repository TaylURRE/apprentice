def cap_name(name):
    """
    ==========
    takes one argument
    ==========
    Takes 1 argument in string format
    Indexes the first letter and formats it to uppercase
    Slices name removing index 0 and formats to lowercase
    Concatenates the uppercase first letter and sliced lowercase of name

    """
    try:
        if type(name) is str:
            clean_name = (name[0].upper() + name[1:].lower())
            return(clean_name)
        else:
            return(name, "Invalid input; please enter a string.")
    except Exception as e:
        return('unable to capitalize', e)


def cap_many_names(names):
    """
    ==========
    takes one argument, a string with multiple words
    ==========

    Takes a string with multiple words
    Splits the arguments at a space
    Iterates through each name and performs cap_name function
    Adheres clean names to an array
    Joins the array and returns clean names in string format.

    """
    clean_names = []
    wrong_type_msg = ("Invalid, format name using string ie 'taylor dennis' ")
    try:
        if type(names) is str:
            names = names.split(' ')
            for name in names:
                clean_names.append(cap_name(name))
            return(' '.join(clean_names))
        else:
            return(names, wrong_type_msg)
    except Exception as e:
        return(wrong_type_msg, e)

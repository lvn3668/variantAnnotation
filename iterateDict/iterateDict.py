

def get_all_values(nested_dictionary):
try:
    dict_values = dict()
    # print ("Inside function that prints all values from nested dict")
    for key, value in nested_dictionary.items():
        if type(value) is dict:
            get_all_values(value)
        else:
            print(key, ":", value)
            dict_values[key] = value

 except Error:
    raise Error
 finally:
    return dict_values


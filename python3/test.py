"""
def to_jaden_case(string):
    list_of_word = string.split(" ")
    list_result = []
    for item in list_of_word:
        item = item.capitalize()
        list_result.append(item)
    result = " ".join(list_result)
    return result


quote = "How can mirrors be real if our eyes aren't real"

print(to_jaden_case(quote))

"""


def narcissistic(value):
    if type(value) != int or value < 0:
        raise Exception("function parameter must be a positive integer")

    result = 0
    array_of_value = str(value)
    print(array_of_value)
    for item in array_of_value:
        result += int(item) ** len(array_of_value)

    return value == result


print(narcissistic(371))

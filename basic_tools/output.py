def roman_numbers(value):
    # Conversion of int into a roman number (works correctly to a max number of 39)
    if value == 0:
        return "0"
    result = ""
    if value < 0:
        result += "-"
        value = abs(value)

    size = [1000, 500, 100, 50, 10]
    name = ["M", "D", "C", "L", "X"]
    smaller = [900, 400, 90, 40, 9]
    for index in range(len(size)):
        while value >= size[index]:
            value -= size[index]
            result += name[index]
        '''if value >= smaller[index]:
            result += name[index]'''

        '''for next in range(index, len(size)):
            if abs(value - size) < bigger_size:
                #subtraction
                result'''

    rome = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX"}
    if value > 0:
        result += rome[value]
    return result


def percent(value, space=""):
    print("{:2.2%}".format(value), end=space)

'''
we have a number x
if this x would be increased by y


lets write down each occurrence of those subtractions
9
40
90
400
900



'''

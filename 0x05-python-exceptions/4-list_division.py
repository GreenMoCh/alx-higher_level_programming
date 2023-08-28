#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    try:
        for i in range(list_length):
            try:
                value_1 = my_list_1[i]
                value_2 = my_list_2[i]
                if not isinstance(value_1, (int, float)) or not isinstance(value_2, (int, float)):
                    raise TypeError("wrong type")
                if value_2 == 0:
                    raise ZeroDivisionError("division by 0")
                division_result = value_1 / value_2
                result.append(division_result)
            except IndexError:
                print("out of range")
                result.append(0)
            except (TypeError, ZeroDivisionError) as e:
                print(e)
                result.append(0)
    finally:
        return (result)

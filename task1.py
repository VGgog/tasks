# Дан список целых чисел по возрастанию [1, 2, 3, 4, 6, 8, 9, 10].
# Надо превратить подряд идущие числа в строку описывающую диапазон.
# То есть в данном случаи ["1-4", "6", "8-10"]


def solving_the_task(list_of_numbers):
    """
    Дан список целых чисел по возрастанию [1, 2, 3, 4, 6, 8, 9, 10].
    Надо превратить подряд идущие числа в строку описывающую диапазон.
    То есть в данном случаи ["1-4", "6", "8-10"].
    """
    result = []
    first_number = list_of_numbers[0]

    for i in range(len(list_of_numbers)):

        number = list_of_numbers[i]
        try:
            next_number = list_of_numbers[i + 1]
        except IndexError:
            appending_in_result(result, first_number, number)
            break

        if number == next_number - 1:
            continue

        else:
            appending_in_result(result, first_number, number)
            first_number = next_number
     
    return result


def appending_in_result(result, first_number, last_number):
    """
    Функция для добавления диапазона чисел в list.
    Функция изменяет list result  динамически.
    """
    if first_number == last_number:
        result.append(str(last_number))
    else:
        result.append("{0}-{1}".format(first_number, last_number))


if __name__ == "__main__":
    print(solving_the_task([1, 2, 3, 4, 6, 8, 9, 10])) # Должен вернуть ["1-4", "6", "8-10"]
    print(solving_the_task([12, 13, 14, 15, 67, 78, 79, 80, 95, 97, 98, 99])) # Должен вернуть ['12-15', '67', '78-80', '95', '97-99']
    print(solving_the_task([9, 10, 11, 12, 14, 15, 16, 17, 19, 20, 21])) # Должен вернуть ["1-4", "6", "8-10"]
    print(solving_the_task([1, 2, 3, 4, 6, 8, 9, 10, 11, 12, 13, 15, 17, 19])) # Должен вернуть ["1-4", "6", "8-10"]
    print(solving_the_task([5, 6, 7, 8, 10, 11, 12, 14, 15])) # Должен вернуть ["1-4", "6", "8-10"]


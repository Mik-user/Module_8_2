def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in range(len(numbers)):
        try:
            result+=numbers[i]
        except TypeError:
            print(f'В numbers записан некорректный тип данных "{numbers[i]}"')
            incorrect_data +=1
    _tuple = (result, incorrect_data)
    return _tuple

def calculate_average(numbers):
    try:
        _tuple=personal_sum(numbers)
        arithmetic_mean = _tuple[0]/(len(numbers)-_tuple[1])
        return arithmetic_mean
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

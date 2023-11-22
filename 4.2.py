def check(index, x_arr, height_arr, flag, count_houses):
    all_count = 0

    count_houses = 0  # Обнуление переменной счетчиков снесенных домов на данной рекурсии

    # НАЧАЛО ЦИКЛА ----------------
    while

    # следующий дом, смотрим куда падает текущий дом (флаг влево вправо)
    if not flag:
        if flag == 1:
            if index != len(x_arr) - 1:  # проверка на конец массива
                next_house = x_arr[index + 1]
            else:
                pass  # рекурсия обратно сделать
        elif flag == 2:
            if index != len(x_arr) - 1:  # проверка на конец массива при падении дома налево (обратная рекурсия)
                next_house = x_arr[index + 1]
            else:
                return count_houses  # возвращаем кол-во снесенных домов, если рекурсия достигла левого края массива

        now_house = x_arr[index]

        # куда упадет дом (смотрим куда он падает через флаг влево или вправо)
        if flag == 1:
            next_index = now_house + height_arr[index]
        elif flag == 2:
            next_index = next_house - height_arr[index]

        # Проверка, достанет ли дом до следующего
        if flag == 1:
            if next_index < next_house:
                count_houses_another = check(index, x_arr, height_arr, 2)
                # СДЕЛАТЬ ПРОВЕКУ НА ТО, КАКАЯ РЕКУРСИЯ ВЫГОДНЕЕ
            elif next_index == next_house:
                pass  # +1 УПАВШИЙ ДОМ
            elif next_index > next_house:
                pass  # УЧЕСТЬ ЗАПАС
        else:
            pass  # СДЕЛАТЬ ТО ЖЕ САМОЕ ЧТО И В ФЛАГ 1

        # НАЧАЛО ЦИКЛА ----------------

        return all_count


def main():
    n = int(input())
    arr_x = list(map(int, input().split()))
    arr_h = list(map(int, input().split()))
    check(0, arr_x, arr_h, 1, 0)


if __name__ == "__main__":
    main()

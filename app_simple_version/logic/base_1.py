# Проверка по первому базису
# Мне лень оптимизировать нахождение нулевого базиса, так что пока мы его передаем сами, ручками ))
def check_base(arr, basis):
    return find_z(arr, basis)


# Более-менее красиво выводит рассчитанные коэффициенты
def print_basis_1(answer_array):
    count = 1
    for i in answer_array:
        print(count)
        for j in i:
            print(j)
        count += 1


# рассчитывает коэффициенты-решения
def find_z(arr, basis):
    arr_z = [[[0]*4 for i in range(4)]for i in range(len(arr))]
    # заполнение данного базиса
    count = 1
    for i in basis:
        arr_z[i][-count][-count] = 1
        count += 1

    bas_z = [3, 2, 1, 0]
    for e in range(len(arr)):
        if e in basis:
            continue
        else:
            z = [[0]*4 for i in range(4)]
            for i in basis:
                value = arr[i][e]
                if value != 0:
                    for j in value:
                        z[bas_z[basis.index(j[1])]][bas_z[basis.index(i)]] = j[0]
            arr_z[e] = z
    # можно вызвать посмотреть, что она рассчитала ))
    # print_basis_1(arr_z)
    # answer_for_read(arr_z)
    return arr_z


def answer_for_read(arr_z):
    m = {
         0: "A",
         1: "B",
         2: "C",
         3: "D"
    }
    arr_answer = []
    for i in arr_z:
        count = 0
        ss = ""
        for k in i:
            s = ""
            for j in range(4):
                if k[j] != 0:
                    if k[j] == 1:
                        s += "z"
                    elif k[j] == -1:
                        s += "-z"
                    else:
                        s += str(k[j])
                        s += "z"
                    s += str(j+1)
                    s += " + "
                if j == 3:
                    s += m[count]
                    s += str(arr_z.index(i)+1)
            count += 1
            ss += s
            if count < 4:
                ss += ", "
        arr_answer.append(ss)
    for i in arr_answer:
        print(i)
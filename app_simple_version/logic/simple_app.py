# чтение данных из файла
def read_file(file):
    f = open(f'{file}', 'r')
    arr = []
    for line in f:
        arr2 = []
        for i in line.split(" "):
            arr2.append(i.rstrip())
        arr.append(arr2)
    f.close()
    return arr


# преобразование данных в удобный вид для дальнейшей работы
def comparison_of(arr):
    new_arr = []
    aw = []
    for i in arr:
        ay = []
        w = []
        for j in i:
            if j != '0':
                e, r = rrr(j)
                ay.append(e)
                w.append(r)
            else:
                ay.append(0)
                w.append(0)
        aw.append(w)
        new_arr.append(ay)
    return new_arr, aw


# вспомогательная функция дробящая e3-4e2 -> [[1, e3], [-4, e2]] - переменные ar, a
#                                  e3-4e2 -> [[1, 2], [-4, 1]] - переменные aw, w -
#                                  именно это используется в дальнейших рассчетах (сразу используются индексы)
def rrr(j):
    map = {
        'e1': 0,
        'e2': 1,
        'e3': 2,
        'e4': 3,
        'e5': 4,
        'e6': 5,
        'e7': 6
    }
    ar = []
    aw = []
    l = len(j)
    k = 0
    while k < l:
        a = []
        w = []
        s_int = ''
        q = j[k]
        h = 0
        if q == "e":
            w.append(1)
            w.append(map[j[k:k+2]])
            a.append(1)
            a.append(j[k:k+2])
            k += 1
        elif q == "-" or q == "+":
            s_int += q
            k += 1
            q = j[k]
            h = 0
            while '0' <= q <= '9':
                s_int += q
                k += 1
                h += 1
                if k < l:
                    q = j[k]
                else:
                    break
            # k += 1
            if h != 0:
                w.append(int(s_int))
                a.append(int(s_int))
            else:
                s_int += '1'
                w.append(int(s_int))
                a.append(int(s_int))
            if q == "e":
                w.append(map[j[k:k + 2]])
                a.append(j[k:k + 2])
                k += 1
        else:
            h = 0
            while '0' <= q <= '9':
                s_int +=q
                k += 1
                h +=1
                if k < l:
                    q = j[k]
                else:
                    break
            if h != 0:
                w.append(int(s_int))
                a.append(int(s_int))
            else:
                s_int += '1'
                w.append(int(s_int))
                a.append(int(s_int))
            if q == "e":
                w.append(map[j[k:k + 2]])
                a.append(j[k:k + 2])
                k += 1
        aw.append(w)
        ar.append(a)
        k += 1
    return ar, aw


# проверка на удовлетворение тождеству Якобы
# [[x,y],z] + [[y,z],x] + [[z,x],y] = 0
def check_yakobi(arr):
    ch = []
    for i in range(7):
        for j in range(i+1, 7):
            for k in range(j+1, 7):
                ch.append([i, j, k])
                print(i, j, k)
                q1 = check(arr, i, j)
                q2 = check(arr, q1, k)
                print(q2)
                e1 = check(arr, j, k)
                e2 = check(arr, e1, i)
                print(e2)
                o1 = check(arr, k, i)
                o2 = check(arr, o1, j)
                print(o2)


# вспомогательная функция для Якоби
# считает для двух значений
def check(arr, i, j):
    a = []
    if type(i) != int:
        l = len(i)
        k = 0
        while k < l:
            if arr[i[k][1]][j] != 0:
                ll = len(arr[i[k][1]][j])
                kk = 0
                while kk < ll:
                    b = []
                    b.append(i[k][0]*arr[i[k][1]][j][kk][0])
                    b.append(arr[i[k][1]][j][kk][1])
                    # print(b)
                    a.append(b)
                    kk += 1
            else:
                a.append(-1)
                # return -1
            k += 1
    elif i != -1:
        if arr[i][j] != 0:
            return arr[i][j]
        else:
            # a.append(-1)
            # return a
            return -1
    else:
        return -1
    return a


# def check_sum(a, b, c):
#


if __name__ == '__main__':
    comp_map = {
        'e1': 0,
        'e2': 1,
        'e3': 2,
        'e4': 3,
        'e5': 4,
        'e6': 5,
        'e7': 6
    }
    file1 = 'data/ex1.txt'
    data_file1 = read_file(file1)
    arr1, aw1 = comparison_of(data_file1)
    print('Проверка алгубры 1 на тождество Якоби')
    check_yakobi(aw1)

    print("new")
    file2 = 'data/ex2.txt'
    data_file2 = read_file(file2)
    print('Проверка алгубры 2 на тождество Якоби')
    arr2, aw2 = comparison_of(data_file2)
    check_yakobi(aw2)

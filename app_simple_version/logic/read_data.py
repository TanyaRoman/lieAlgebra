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

# чтение данных из файла
def read_file(file):
    f = open(f'{file}', 'r')
    arr = []
    for line in f:
        arr2 = []
        for i in line.split(" "):
            arr2.append(i.rstrip())
        arr.append(arr2)
    print(arr)
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
    print(new_arr)
    return new_arr, aw


# вспомогательная функция дробящая e3-4e2 -> [[1, e3], [-4, e2]]
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


def check(arr, i, j):
    a = []
    if type(i) != int:
        l = len(i)
        k = 0
        # print(i)
        while k < l:
            # print(i, i[k], i[k][1])
            # print(l, k, i[k][0], arr[i[k][1]][j])
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
    # if i != -1:
    #     if arr[i][j] != 0:
    #         # a.append(arr[i][j])
    #         return arr[i][j]
    #     else:
    #         # a.append(0)
    #         return -1
    # else:
    #     return -1
    elif i != -1:
        if arr[i][j] != 0:
            # a.append(arr[i][j])
            return arr[i][j]
        else:
            # a.append(0)
            return -1
    else:
        return -1
    return a


# def check_sum(a, b, c):
#


if __name__ == '__main__':
    file1 = 'data/ex1.txt'
    data_file = read_file(file1)
    # print(rrr('-e4+5e6'))
    arr, aw = comparison_of(data_file)
    print(aw)
    comp_map = {
        'e1': 0,
        'e2': 1,
        'e3': 2,
        'e4': 3,
        'e5': 4,
        'e6': 5,
        'e7': 6
    }
    check_yakobi(aw)
    # for i in range(7):
    #     for j in range (i+1, 7):
    #         print(check(aw, i, j))
    # print(check(aw, i, j))
    # print(type([[2, 'e3']]) != int)
    # print(check(aw, 1, 2))
    # m = check(aw, 2, 6)
    # print(m)
    # print(check(aw, m, 5))
    # print(check(aw, [[1, 2], [-1, 3]], 1))

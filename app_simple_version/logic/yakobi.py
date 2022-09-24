# class for check Yakobi

# проверка на удовлетворение тождеству Якобы
# [[x,y],z] + [[y,z],x] + [[z,x],y] = 0
def check_yakobi(arr):
    ch = []
    for i in range(7):
        for j in range(i+1, 7):
            for k in range(j+1, 7):
                ch.append([i, j, k])
                # print(i, j, k)
                q1 = check(arr, i, j)
                q2 = check(arr, q1, k)
                # print(q2)
                e1 = check(arr, j, k)
                e2 = check(arr, e1, i)
                # print(e2)
                o1 = check(arr, k, i)
                o2 = check(arr, o1, j)
                # print(o2)


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



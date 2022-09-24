import read_data as rd
import yakobi as y
import base_1 as b1


def work_with_algebra(file_name, basis):
    print("Алгебра из", file_name)
    data_file = rd.read_file(file_name)
    array_for_check, array_for_work = rd.comparison_of(data_file)
    print("Считаны данные из алгебры:")
    for i in data_file:
        print(i)
    # print("Для работы данные преобразованы в вид:")
    # for i in array_for_work:
    #     print(i)
    y.check_yakobi(array_for_work)
    arr_answer = b1.check_base(array_for_work, basis)
    print()
    print("Рассчитанное решение:")
    b1.answer_for_read(arr_answer)
    print()
    print()


if __name__ == '__main__':

    file1 = 'data/ex1.txt'
    basis1 = [1, 2, 3, 4]  # делаю сразу смещение на 1, для кофициентов
    work_with_algebra(file1, basis1)

    file2 = 'data/ex2.txt'
    basis2 = [0, 1, 2, 3]
    work_with_algebra(file2, basis2)

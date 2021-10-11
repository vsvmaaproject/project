def mySort(scList, fl):    # объявляем функцию mysort, который сортирует список; scList - список учеников, fl - параметр порядка сортировки
    n = len(scList)    # инициализируем n длиной списка scList
    for i in range(n - 1):    # запускаем цикл; i от 0 до n-1 (не включительно)
        for j in range(n - i - 1):  # запускаем вложенный цикл; j от 0 до n-i-1 (не включительно)
            if (scList[j][-2] > scList[j + 1][-2]) and fl == 1 or (scList[j][-2] < scList[j + 1][-2]) and fl == -1:   # сравнение соседних элементов зависимо от требуемого порядка
                scList[j], scList[j + 1] = scList[j + 1], scList[j] # меняем местами текущий и следующий элементы списка
    return (scList)   # возвращаем список


finame = 'input.txt' # записываем название файла c входными данными
foname = 'output.txt' # записываем название файла куда вставим уже отсортированный список
f = open(finame, 'r') # открываем файл на чтение
scoreList = []  # объявляем список учеников

n = int(f.readline())  # считываем кол-во элементов базы данных
flag = int(f.readline()) # вносим параметр порядка чисел после сортировки

for i in range(n): # цикл для внесения всех строк в список
    t = str((f.readline())) # записываем в промежуточную переменную строку
    scoreList.append(t) # заносим в список записи каждого ученика
    
f.close()   # закрываем файл

scoreList = mySort(scoreList, flag)   # сортируем список

f = open(foname, 'w')   # открываем файл на запись с именем foname и форматом данных .txt
f.write(str(n) + ' \n')  # записываем кол-во элементов базы данных в новый файл

for i in range(n):  # запускаем цикл; i от 0 до n (не включительно)
    f.write(scoreList[i])   # записываем отсортированные элементы массива  в новый файл

f.close()   # закрываем файл

if flag == 1:    # если flag == 1(true), то
    print('Ваш файл упорядочен в порядке возрастания')
else:   # иначе (flag == -1)
    print('Ваш файл упорядочен в порядке убывания')


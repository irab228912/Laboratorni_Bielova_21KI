x = [3,1,2,3,4,5,6,3,4,5,7,6,5,4,3,4,5,4,3, 'Привіт', 'анаконда']
mass = []

def sort():
    global x, mass
    n = len(x)
    for i in range(n-1):  # n-1 ітер. по фул лісту БЕЗ ласт ел-та для того, щоб оптимізувати сортування
        j = 0  # Ініціал. j поза внутрішнім циклом, щоб уникнути проблем з індексами
        while j < (n-i-1):  # Ітер. від початку масиву до ласт НЕВІДСОРТ. ел-та
            if type(x[j]) != str and type(x[j+1]) != str:
                if x[j] > x[j+1]:
                    x[j], x[j+1] = x[j+1], x[j]
                j += 1
            elif type(x[j]) == str:
                mass.append(x[j])
                x.pop(j)  # Видал. ел-т за індексом j(перший з порівню-х)
                n -= 1  # Оновл. n бо ел-т видалений
            elif type(x[j+1]) == str:
                mass.append(x[j+1])
                x.pop(j+1)  # Видал. ел-т за індексом j+1(другий з порівню-х)
                n -= 1  # Оновлюємо n бо елемент видалений
                # Оновл. j щоб уникн. пропуск ел-та після видалення
            else:
                j += 1

sort()
#print("Глобальний список x після сортування та видалення рядків:", x)
#print("Глобальний список mass з видаленими рядками:", mass)

def cleaning():
    global x
    i = 0
    while i < len(x) - 1:
        if  x[i] == x[i+1]:
            x.pop(i+1)
        else:
            i += 1

cleaning()
#print("Cleaned mass x:", x)

def sort_mass(): #n
    global mass
    mass.sort()

sort_mass()
print(mass)

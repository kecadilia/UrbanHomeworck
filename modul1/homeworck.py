grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразуем множество студентов в отсортированный список, чтобы соответствовать порядку оценок
students_list = sorted(students)

# Создаем словарь для хранения средних баллов
average_grades = {}

# Вычисляем средний балл для каждого студента
for i in range(len(students_list)):
    student = students_list[i]
    student_grades = grades[i]
    average_grade = sum(student_grades) / len(student_grades)  # Вычисляем средний балл
    average_grades[student] = average_grade  # Добавляем в словарь

# Выводим результаты на экран
for student, avg in average_grades.items():
    print(f"{student}: {avg:.2f}")
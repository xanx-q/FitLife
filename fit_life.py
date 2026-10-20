import time

WATER_PER_KG = 30  # Переменная для расчета мл воды на кг веса
ML_PER_LITER = 1000  # Переменная для расчета мл воды на литр
Interval_for_loader = 0.1  # Интервал для вывода анимации

# Проект FitLife - MVP версия 1.0

# 1. Знакомство
print('Здравствуйте, уважаемый пользователь')
user_name = input('Введите свое имя: ')
user_name = user_name.title()

# 2. Сбор данных
while True:  # Проверка на ввод целого числа и адекватный возраст
    try:
        user_age = int(input('Введите свой возраст: '))

        if 0 <= user_age <= 100:
            break
        else:
            print('Введите корректный возраст (от 0 до 100 лет)')
    except ValueError:
        print('Возникла ошибка, пожалуйста введите целое число лет.')

while True:  # Проверка на ввод числа с плавающей точной и адекватный вес
    try:
        weight_str = input('Введите свой вес (в кг): ').replace(',', '.')
        user_weight = float(weight_str)  # разделено на две строки для pep8

        if 35. <= user_weight <= 150.:
            break
        else:
            print('Введите корректный вес (от 35 до 150 кг)')
    except ValueError:
        print('Возникла ошибка, пожалуйста введите число с точкой ', end='')
        print('или целое(например 80.5 или 80:)')

while True:  # Проверка на ввод числа с точкой и адекватный рост
    try:
        height_str = input('Введите свой рост (в метрах): ').replace(',', '.')
        user_height = float(height_str)  # разделено на две строки для pep8

        if 1. <= user_height <= 2.3:
            break
        else:
            print('Введите корректный рост (от 1 до 2.3 метра)')
    except ValueError:
        print('Возникла ошибка, пожалуйста введите число с точкой ', end='')
        print('(например 1.5 или 1.85)')
#  Проверки через while true и try/except подсказал ai(Пришлось их изучить)
#  И так же видел подобные решение в чате модуля курса


# 3. Логика расчетов


def bmi(weight, height):
    """Вычисляем индекс массы тела функцией"""
    result_bmi = weight / (height ** 2)
    print(f'Ваш ИМТ: {round(result_bmi, 1)}')
    return result_bmi


def water_norm(weight, water_per_kg):
    """Вычисляем норму воды функцией"""
    water_ml = weight * water_per_kg
    water_liter = water_ml / ML_PER_LITER
    print(f'Ваша норма воды в день: {round(water_liter, 2)}')
    return water_liter


# 5. Вывод красивого результата
Loading = ['0%', '10%', '20%', '30%', '40%', '50%',
           '60%', '70%', '80%', '90%', '100%']  # список для анимации загрузки

print('Ваш расчет готовится, подождите.')

for loader in Loading:  # цикл для анимации
    print(loader)
    time.sleep(Interval_for_loader)
print('Ваш расчет готов.')

print('Расчет для пользователя:', user_name, user_age, 'г.')
# Выводим данные пользователя
bmi(user_weight, user_height)
# Вызываем функцию ИМТ
water_norm(user_weight, WATER_PER_KG)
# Вызываем функцию нормы воды
print('Расчет окончен. Будьте здоровы!')
# Выводим уведомление о том что расчет окончен
# Конец программы.

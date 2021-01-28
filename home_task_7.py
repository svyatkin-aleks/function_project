def inch_to_cm(a):
    cm = a * 2.54
    print(f'{a} inches is {cm} centimeters.')
    return cm


def cm_to_inch(a):
    inch = a / 2.54
    print(f'{a} centimeters is {inch} inches.')
    return inch


def mi_to_km(a):
    km = a * 1.609
    print(f'{a} miles is {km} kilometers.')
    return km


def km_to_mi(a):
    mi = a / 1.609
    print(f'{a} kilometers is {mi} miles')
    return mi


def lb_to_kg(a):
    kg = a / 2.2046
    print(f'{a} pounds is {kg} killograms.')
    return kg


def kg_to_lb(a):
    lb = a * 2.2046
    print(f'{a} killograms is {lb} pounds.')
    return lb


def oz_to_g(a):
    g = a / 0.035274
    print(f'{a} ounces is {g} gramms.')
    return g


def g_to_oz(a):
    oz = a * 0.035274
    print(f'{a} gramms is {oz} ounces.')
    return oz


def gal_to_l(a):
    l = a * 3.785
    print(f'{a} gallons is {l} liters.')
    return l


def l_to_gal(a):
    gal = a / 3.785
    print(f'{a} liters is {gal} gallons.')
    return gal


def pint_to_l(a):
    l = a / 2.113
    print(f'{a} pints is {l} liters.')
    return l


def l_to_pint(a):
    pint = a * 2.113
    print(f'{a} litres is {pint} pints.')
    return pint


def programm():
    for i in range(1, 13):
        i = int(input(
            'Выбирете нужный вам вариант: \n1. Дюймы в сантиметры 2. Сантиметры в дюймы 3. Мили в километры\n4. Километры в мили 5. Фунты в килограммы 6. Килограммы в фунты\n7. Унции в граммы 8. Граммы в унции 9. Галлон в литры \n10. Литры в галлоны 11. Пинты в литры 12. Литры в пинты \n'))
        if i == 0:
            break
        if i > 12:
            print('Please choose any one from 1 to 12.')
            continue
        n = int(input('Введите значение '))
        list = [0, inch_to_cm(n), cm_to_inch(n), mi_to_km(n), km_to_mi(n), lb_to_kg(n), kg_to_lb(n), oz_to_g(n),
                g_to_oz(n), gal_to_l(n), l_to_gal(n), pint_to_l(n), l_to_pint(n)]
        n = list[i]

    return 'You are exit programm'


programm()
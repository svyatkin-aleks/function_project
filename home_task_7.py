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

while True:
    choise = int(input('Выбирете нужный вам вариант: \n1. Дюймы в сантиметры 2. Сантиметры в дюймы 3. Мили в километры\n4. Километры в мили 5. Фунты в килограммы 6. Килограммы в фунты\n7. Унции в граммы 8. Граммы в унции 9. Галлон в литры \n10. Литры в галлоны 11. Пинты в литры 12. Литры в пинты \n'))
    if choise == 0:
        print('You are out of programm')
        break
    elif choise > 12:
        print('Please choose any one from 1 to 12.')
        continue
    value = int(input('Please insert value\n'))
    if choise == 1:
        inch_to_cm(value)
    elif choise == 2:
        cm_to_inch(value)
    elif choise == 3:
        mi_to_km(value)
    elif choise == 4:
        km_to_mi(value)
    elif choise == 5:
        lb_to_kg(value)
    elif choise == 6:
        kg_to_lb(value)
    elif choise == 7:
        oz_to_g(value)
    elif choise == 8:
        g_to_oz(value)
    elif choise == 9:
        gal_to_l(value)
    elif choise == 10:
        l_to_gal(value)
    elif choise == 11:
        pint_to_l(value)
    elif choise == 12:
        l_to_pint(value)
    else:
        pass
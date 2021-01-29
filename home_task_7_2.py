def inch_to_cm(a):
    cm = a * 2.54
    return cm

def cm_to_inch(a):
    inch = a / 2.54
    return inch

def mi_to_km(a):
    km = a * 1.609
    return km

def km_to_mi(a):
    mi = a / 1.609
    return mi

def lb_to_kg(a):
    kg = a / 2.2046
    return kg

def kg_to_lb(a):
    lb = a * 2.2046
    return lb

def oz_to_g(a):
    g = a / 0.035274
    return g

def g_to_oz(a):
    oz = a * 0.035274
    return oz

def gal_to_l(a):
    l = a * 3.785
    return l

def l_to_gal(a):
    gal = a / 3.785
    return gal

def pint_to_l(a):
    l = a / 2.113
    return l

def l_to_pint(a):
    pint = a * 2.113
    return pint

def programm():
    while True:
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
        print(n)



programm()
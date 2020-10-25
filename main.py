import random as rd

k = 3 # пороговое значение
s = 42 # секрет
keys = 4 # число ключей
a, b = 10, 99 # диапазон случайных чисел

# результат уравнения для формирования точек
def equationResult(x, rand, k, s):
    result = s
    for i in range(k - 1):
        result += rand[i] * (x ** (i + 1))
    return result

# нахождение интерполяционного полинома Лагранжа:
def polynomialLagrange(x, y):
    z = 0
    for i in range(len(y)):
        p1, p2 = 1, 1
        for j in range(len(x)):
            if i != j:
                p1 *= -x[j]
                p2 *= (x[i] - x[j])
        z += y[i] * p1 / p2
    return int(round(z))

# случайные коэффициенты для составления точек секрета
rand = []
for i in range(k - 1):
    rand.append(rd.randint(a, b))

# формирование исходного уравнения
equation = 'f(x) = ' + str(s)
for i in range(k - 1):
    equation += (' + ' + str(rand[i]) + '*x^' + str(i + 1))
print(equation)

# формирование исходных точек случайным образом
x,y = [], []
for i in range(keys):
    rdTemporary = rd.randint(a, b)
    x.append(rdTemporary)
    y.append(equationResult(rdTemporary, rand, k, s))
print('x :', x, '\ny :', y)

print('Полученный секрет :', polynomialLagrange(x[:3], y[:3]))

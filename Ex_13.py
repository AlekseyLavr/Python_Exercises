TOONIE = 200
LOONIE = 100
QWERTY = 25
TEN = 10
FIVE = 5
ONE = 1

n = int(input("Введите сумму в центах: "))
print(f"{n // TOONIE} двухдолларовых монет")
n = n % TOONIE
print(f"{n // LOONIE} однодолларовых монет")
n = n % LOONIE
print(f"{n // QWERTY} 25-центовых монет")
n = n % QWERTY
print(f"{n // TEN} 10-центовых монет")
n = n % TEN
print(f"{n // FIVE} 5-центовых монет")
n = n % FIVE
print(f"{n // ONE} 1-центовых монет")
n = n % ONE
print(f'{n} центов')
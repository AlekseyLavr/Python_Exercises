print('Введите сумму заказа: ')
summa = float(input())
RENT = 0.2
TIPS = 0.1
summa_rent = summa * RENT
summa_tips = summa * TIPS
total_summa = summa + summa_rent + summa_tips
print("Сумма налога: %.2f" % summa_rent)
print("Сумма чаевых: %.2f" % summa_tips)
print("Итог: %.2f = %.2f + %.2f + %.2f" % (total_summa, summa, summa_rent, summa_tips))
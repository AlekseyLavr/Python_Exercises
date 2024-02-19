COST_BREAD = 3.49
sum_bread = int(input('Введите количество приобретенных вчерашних буханок: '))
cost_yesterday_bread = 0.6 * COST_BREAD
total_price = cost_yesterday_bread * sum_bread
print('Цена за буханку - %.2f $.\nЦена со скидкой - %.2f $.\nОбщая стоимость хлеба - %.2f $.' % (COST_BREAD,\
      cost_yesterday_bread, total_price))
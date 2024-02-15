sum_orig_dep = float(input('Введите сумму первоначального депозита: '))
percent = 0.04
summa_1_your = sum_orig_dep + sum_orig_dep * percent
summa_2_your = summa_1_your + summa_1_your * percent
summa_3_your = summa_2_your + summa_2_your * percent
print('Сумма депозита:\nв конце первого года - %.2f,\nв конце второго года - %.2f,\nв конце третьего года - %.2f'\
       % (summa_1_your, summa_2_your, summa_3_your))
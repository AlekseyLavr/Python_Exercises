PRICE_1L = 0.10
PRICE_1_MORE = 0.25
print("Введите количество бутылок, 1л и меньше: ")
smoller = int(input())
print("Введите количество бутылок, более 1л: ")
larger = int(input())
sale = smoller * PRICE_1L + larger * PRICE_1_MORE
print("Ваша выручка составит $ %.2f" % sale)

d = { 'cake': ['biscuit', 10, 700],
      'cookies': ['chocolate', 15, 800],
      'waffles': ['creamy', 20, 800],
      'bread': ['wheat', 5, 650]}
while True:
    n = input ('введите товар, приступить к покупке или выход:')
    if n in d:
        m = input(' введите сведения о товаре, которые хотите узнать (description, price, quantity or inf): ')
        if m == 'description':
            print(n, d[n][0])
        if m == 'price':
            print(n, d[n][1])
        if m == 'quantity':
            print(n, d[n][2])
        if m == 'inf':
            print(n, 'состав', d[n][0], 'цена', d[n][1], 'количество', d[n][2]  )
    if n=='выход':
        break
    elif n== 'приступить к покупке':
        while True:
            a = input("Введите товар, который хотите купить или введите n для выхода: ")
            if a =='n' or a not in d:
                print ('у нас нет такого товара! до свидания!')
                break
            e = int(input("Сколько Вы хотите купить?"))
            if e>d[a][2]:
                print("У нас столько нет, выберите другое количество или товар")
                continue
            b = e*(d[a][1]/100)
            d[a][2] = d[a][2] - e
            print(f"Вам надо заплатить {b} р., осталось {d[a][2]} грамм товара")
print('До свидания!')

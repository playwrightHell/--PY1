money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
# TODO Оформить решение

while money_capital >= 0:
    salary -= spend
    money_capital += salary
    spend * increase
    month += 1

print(month)

salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение

for money in range(1, months + 1):
    spend = spend * increase + 1
    money = salary - spend
    need_money += money

print(round(need_money))

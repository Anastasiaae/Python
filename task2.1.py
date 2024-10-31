money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0

while True:
    money_capital += salary

    if money_capital >= spend:
        money_capital -= spend
        month += 1

        spend *= (1 + increase)
    else:
        break


print("Количество месяцев, которое можно протянуть без долгов:", month)

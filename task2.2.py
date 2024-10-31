salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев
increase = 0.03  # Ежемесячный рост цен


required_cushion = 0

for _ in range(months):
    deficit = max(0, spend - salary)
    required_cushion += deficit
    spend *= (1 + increase)


print(f"Подушка безопасности, чтобы протянуть 10 месяцев без долгов:", round(required_cushion))
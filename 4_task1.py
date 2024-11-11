# TODO решите задачу
def task() -> float:
    total = 0
    score_value = 0
    aggregated_sum = 0
    weight_value = 0

    with open("input.json", "r") as file:
        lines = file.readlines()

    for line in lines:
        if "score" in line:
            score_value = float(line[line.find("score") + 8:line.rfind(",")].strip())
        elif "weight" in line:
            weight_value = float(line[line.find("weight") + 9:line.rfind("}")].strip())

        if score_value != 0 and weight_value != 0:
            aggregated_sum += score_value * weight_value
            score_value, weight_value = 0, 0  # Сброс значений после использования

    return round(aggregated_sum, 3)


print(task())

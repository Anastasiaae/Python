# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


def find_common_participants(group1, group2, separator=','):
    # Разделяем строки на списки участников
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))

    # Находим общие участники
    common_participants = participants1.intersection(participants2)

    # Приводим список общих участников в алфавитном порядке
    sorted_common_participants = sorted(common_participants)

    return sorted_common_participants



# Вызываем функцию
common_participants = find_common_participants(participants_first_group, participants_second_group, '|')
print(find_common_participants(participants_first_group, participants_second_group, "|"))
# TODO Провеьте работу функции с разделителем отличным от запятой

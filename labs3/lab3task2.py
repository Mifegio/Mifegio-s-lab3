# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, separator=','):
    participants1 = set(first.split(separator))
    participants2 = set(second.split(separator))
    participants = list(participants1.intersection(participants2))
    participants.sort()
    return participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
participants = find_common_participants(participants_first_group, participants_second_group, '|')
print("Количество общих участников:", participants)

import json

def load_candidates():
    """
        Функция получает json - файл и выгружает из него данные
    """
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_all():
    """
      Функция показывает всех кандидатов
    """
    return load_candidates()


def get_by_pk(pk):
    """
    Функция возвращает кандидата по pk
    """
    for i in load_candidates():
        if i['pk'] == pk:
            return i

    return "Mistake"


def get_by_skill(skill_name):
    """
        Функция возвращает кандидата по навыкам
    """
    candidate_with_skill = []
    for i in load_candidates():
        if skill_name.lower() in i['skills'].lower().split(', '):
            candidate_with_skill.append(i)

    return candidate_with_skill

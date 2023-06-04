import json


class Func:
    """Класс для работы с json"""
    def __init__(self, keyword, vacancies_json):
        self.__filename = f'{keyword.title()}.json'
        self.insert(vacancies_json)

    def insert(self, vacancies_json):
        with open(self.__filename, "w", encoding='utf-8') as f:
            json.dump(vacancies_json, f, ensure_ascii=False, indent=4)

    def select(self):
        with open(self.__filename, "r", encoding='utf-8') as f:
            data = json.load(f)
        vacancies = [Vacancy(x['id'], x['title'], x['url'], x['salary_from'], x['salary_to'], x['employer'], x['api'])
                     for x in data]
        return vacancies


class Vacancy:
    """Класс для работы с вакансиями"""
    __slots__ = ('id', 'title', 'url', 'salary_from', 'salary_to', 'employer', 'api')

    def __init__(self, vacancy_id, title, url, salary_from, salary_to, employer, api):
        self.id = vacancy_id
        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.employer = employer
        self.api = api

    def __gt__(self, other):
        if not other.salary_from:
            return True
        elif not self.salary_from:
            return False
        return self.salary_from >= other.salary_from

    def __str__(self):
        salary_from = f'От {self.salary_from}' if self.salary_from else ''
        salary_to = f'До {self.salary_to}' if self.salary_to else ''
        if self.salary_from is None and self.salary_to is None:
            self.salary_from = 'Не указана'
        return f'Вакансия \"{self.title}\" \nКомпания: \"{self.employer}\" \nЗарплата: {salary_from} {salary_to} \nURL:{self.url}'

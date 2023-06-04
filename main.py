from vacancies_from_HH_SJ import HeadHunterAPI, SuperJobAPI
from func import Func


def main():
    vacancies_json = []
    keyword = input('Введите ключевые слова для фильтрации вакансий: ')
    num_pages = input('Укажите количество страниц для поиска: ')

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI(keyword)
    superjob_api = SuperJobAPI(keyword)

    for api in (hh_api, superjob_api):
        api.get_vacancies(pages_count=int(num_pages))
        vacancies_json.extend(api.get_formatted_vacancies())

    func = Func(keyword=keyword, vacancies_json=vacancies_json)

    while True:
        command = input(
            "1 - вывести список вакансий;\n"
            "2 - завершение поиска.\n"
        )
        if command.lower() == '2':
            break
        elif command == '1':
            vacancies = func.select()

        for vacancy in vacancies:
            print(vacancy, end='\n\n')


if __name__ == '__main__':
    main()
from faker import Faker
import random as rd
from faker.providers import BaseProvider
import csv


# мой провайдер для отдела, очень сложный я писать не стал
class MyProvider(BaseProvider):
    def department(self):

        dep_lv_1 = ["Департамент разработки", "Департамент обсулживания клиентов"]
        dep_dev = ["Отдел тестирования", "Отдел програмистов", "Отдел адиминистрирования"]
        dep_client = ["Отдел качества", "Отдел подарков клиентам", "Отдел Еще отдел"]
        team = [" Команда Паши Актенова", "Команда Жени Кудрявцева", "Команда Насти Безруковой"]

        dep_1  = dep_lv_1[rd.randint(0, 1)] + " -> "
        if dep_1 == dep_lv_1[0]:
            dep_1 += dep_dev[rd.randint(0, 2)] + " -> "
        else:
            dep_1 += dep_client[rd.randint(0, 2)] + " -> "
        dep_1 += team[rd.randint(0, 2)]
        return dep_1


fake = Faker(['ru_RU'])
fake.add_provider(MyProvider)


def make_fake_data(size: int = 100) -> list:
    """
    Создает искусственные данные для задания
    да работы полностью рандомные
    специально для IT не нашлось провайдера у
    faker библиотеки
    """
    fake_list = list()
    for _ in range(size):
        fake_row = dict()
        fake_row['name'] = fake.name()
        fake_row['position'] = fake.job()
        fake_row['department'] = fake.department()
        fake_row['coef'] = round(rd.uniform(0.0, 5.0), 1)
        fake_row['salary'] = rd.randint(30000, 250000)
        fake_list.append(fake_row)
    return fake_list


def fake_csv_file(file_to_save: str, size: int = 100) -> None:
    """
    Создает фейковые файл для задания
    стандартное кол-во строк - 100
    """
    fake_data = make_fake_data(size)
    try:
        file  = open(file_to_save, 'w')
        filednames = ["name", "position", "department", "coef", "salary"]
        writer = csv.DictWriter(file, filednames, lineterminator='\n')
        #writer.writeheader()
        for data in fake_data:
            writer.writerow(data)
    except IOError:
        print("Can't create file")
        return 1
    finally:
        file.close()


if __name__ == "__main__":
    file = "data.csv"
    fake_csv_file(file)

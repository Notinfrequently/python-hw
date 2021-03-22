import csv
import argparse

parser = argparse.ArgumentParser(description='Make summary other csv file')
parser.add_argument("--command", required=True, choices=['print_deps', 'print_sum', 'save_sum'],
                    help="""Options: print_deps - print all departments,
                    print_sum - print summary,
                    save_sum - save summary to a csv file
                    """)

args = parser.parse_args()

def read_data_from_csv(file: str) -> list:
    """
    Читает данные из csv файла
    """
    try:
        csv_file = open(file, encoding='utf-8')
    except IOError:
        print("File not accessible")

    data = list()
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        data.append(line)
    if len(data) == 0:
        print("File is empty!")
        return 1
    return data


def get_dep_size(data: list, dep_name: str) -> int:
    """
    Возвращает кол-во сотрудников в отделе
    """
    size = 0
    for dep in data:
        if dep[2] == dep_name:
            size += 1
    return size


def get_all_dep_sizes(data: list) -> dict:
    """
    Возвращает кол-во сотрудников во всех отделах
    """
    uniq_deps = get_all_departments(data)
    deps = dict()
    for uniq_dep in uniq_deps:
        deps[uniq_dep] = get_dep_size(data, uniq_dep)
    return deps


def get_min_max_salary(data: list) -> dict:
    """
    Возвращает словарь со значениями минимальной зарпалты
    максимальной и средней по отделу
    """
    salarys = dict()
    temp_salarys = list()
    uniq_deps = get_all_departments(data)
    for u_dep in uniq_deps:
        for row in data:
            if row[2] == u_dep:
                temp_salarys.append(int(row[4]))
        salarys[u_dep] = {'min': None, 'max' : None, 'avg' : None}
        salarys[u_dep]['min'] = min(temp_salarys)
        salarys[u_dep]['max'] = max(temp_salarys)
        salarys[u_dep]['avg'] = round((sum(temp_salarys)/len(temp_salarys)), 4)
        temp_salarys.clear()
    return salarys


def get_summary_report_by_department(data: list) -> list:
    """
    Возвращает отчет по отделам
    """
    summary = list()
    u_deps = get_all_departments(data)
    deps_sizes= get_all_dep_sizes(data)
    min_max_avg_salary = get_min_max_salary(data)
    for u_dep in u_deps:
        temp_sum = dict()
        #temp_sum = {'size' : None, 'min': None,
        #                                'max' : None, 'avg' : None}
        temp_sum['dep'] = u_dep
        temp_sum['size'] = deps_sizes[u_dep]
        temp_sum['min'] = min_max_avg_salary[u_dep]['min']
        temp_sum['max'] = min_max_avg_salary[u_dep]['max']
        temp_sum['avg'] = min_max_avg_salary[u_dep]['avg']
        summary.append(temp_sum)
    return summary

def print_summary_report_by_department(data) -> None:
    """
    Выводит отчет на экран
    """
    summary = get_summary_report_by_department(data)
    print("Сводный отчет по отделам:\n")
    for dep in summary:
        print(dep['dep'])
        print('Численность отдела: {}'.format(dep['size']))
        print('Минимальная зар.плата: {}'.format(dep['min']))
        print('Максимальная зар.плата: {}'.format(dep['max']))
        print('Средняя зар.плата: {}'.format(dep['avg']))
        print('\n')


def save_summary_as_csv(data: list, file_to_save: str) -> int:
    """
    Сохраняет отчет в csv файл
    """
    summary = get_summary_report_by_department(data)
    try:
        file  = open(file_to_save, 'w')
        filednames = ["dep", "size", "min", "max", "avg"]
        writer = csv.DictWriter(file, filednames, lineterminator='\n')
        for data in summary:
            writer.writerow(data)
    except IOError:
        print("Can't create file")
        return 1
    finally:
        file.close()


def get_all_departments(data: list) -> set:
    """
    Выводит все уникальные отделы на экран
    """
    not_unique_departments = list()
    for department in data:
        #department = department[2].split(" -> ")
        not_unique_departments.append(department[2])
    return set(not_unique_departments)

def print_all_departments(data: list) -> None:
    """
    Выводит все отделы
    """
    deps = get_all_departments(data)
    for dep in deps:
        print(dep, end='\n')


def main():
    """
    def_file - файл по которому будет составляться отчет по отделам
    """
    def_file = 'data.csv'
    data = read_data_from_csv(def_file)
    if args.command == "print_deps":
        print_all_departments(data)
    elif args.command == "print_sum":
        print_summary_report_by_department(data)
    elif args.command == "save_sum":
        save_summary_as_csv(data, "summary.csv")

if __name__ == '__main__':
    main()

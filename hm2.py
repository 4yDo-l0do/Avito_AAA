import csv


def print_hierarchy_of_command(name_file:str='Corp_Summary.csv'):
    '''функция выводит все департаменты и команды, которые содержатся в файле'''
    with open(name_file, 'r', encoding = 'utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        hierarchy_of_comand = {}
        for line in reader:
            if line[1] not in hierarchy_of_comand.keys():
                hierarchy_of_comand[line[1]] = [line[2]]
            elif line[2] not in hierarchy_of_comand[line[1]]:
                hierarchy_of_comand[line[1]].append(line[2])
        for key, value in hierarchy_of_comand.items():
            print(key, ': ', ', '.join(str(team) for team in value))


def make_a_report(name_file:str='Corp_Summary.csv'):
    '''функция создает сводный отчет в виде словоря'''
    with open(name_file, 'r', encoding = 'utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        report={}
        for line in reader:
            if line[1] not in report.keys():
                report[line[1]] = [1, int(line[5])]
            else:
                report[line[1]][0]+=1
                report[line[1]].append(int(line[5]))
        final_report={}
        for key, value in report.items():
            final_report[key] = [value[0], max(value[1::]) - min(value[1::]), round(sum(value[1::]) / value[0])]
    return final_report


def print_report():
    '''функция печатает отчет'''
    report = make_a_report()
    for key, value in report.items():
        print(f'{key} : численность - {value[0]}, вилка зарплат - {value[1]}, средняя зп - {value[2]}')


def save_report():
    '''функция сохраняет отчет в виде csv'''
    report = make_a_report()
    with open('report.csv','w',newline="", encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['Название', 'Численность', 'Вилка зарплат', 'Средняя зарплата'])
        for key, value in report.items():
            writer.writerow([key, value[0], value[1], value[2]])


def step():
    '''функция выбора пункта меню'''
    print(
        '1) Вывести в понятном виде иерархию команд, т.е. департамент и все команды, которые входят в него',
        '2) Вывести сводный отчёт по департаментам: название, численность, "вилка" зарплат в виде мин – макс, среднюю зарплату',
        '3) Сохранить сводный отчёт из предыдущего пункта в виде csv-файла', sep='\n')
    option = ''
    options = {'1': 1, '2': 2, '3': 3}
    while option not in options:
        print('Выберите: {}/{}/{}'.format(*options))
        option = input(str())

    if options[option] == 1:
        print_hierarchy_of_command()
    elif options[option] == 2:
        print_report()
    else:
        save_report()


if __name__ == '__main__':
    step()

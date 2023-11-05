import csv


def get_hierarchy():
    hierarchy = {}
    with open("./Corp_Summary.csv", encoding='utf-8', newline='') as file:
        csvreader = csv.reader(file)
        next(csvreader, None)  # пропустить заголовки
        for row in csvreader:
            data = row[0].split(';')
            if data[1] not in hierarchy.keys():
                hierarchy[data[1]] = {data[2]}
            else:
                hierarchy[data[1]].add(data[2])
    for department in hierarchy.keys():
        print(department)
        for team in hierarchy[department]:
            print(f'\t{team}')


def decorator_printing(get_report):
    def wrapper():
        report = get_report()
        for department in report.keys():
            print(department)
            print(f'\tчисленность: {report[department][0]}')
            print(
                f'\tвилка зп: {min(report[department][1])} - {max(report[department][1])}')
            print(
                f'\tсредняя зп: {round(sum(report[department][1])/len(report[department][1]), 2)}')
    return wrapper


def decorator_saving_csv(get_report):
    def wrapper():
        report = get_report()
        fields = ['Название', 'Численность', 'Вилка зп', 'Средняя зп']
        with open('report.csv', 'w', encoding='utf8', newline='') as state_file:
            writer = csv.writer(state_file)
            writer.writerow(fields)
            for department in report.keys():
                writer.writerow([department, report[department][0], f'{min(report[department][1])} - {max(report[department][1])}',
                                 round(sum(report[department][1])/len(report[department][1]), 2)])
    return wrapper


def get_report():
    report = {}
    with open("./Corp_Summary.csv", encoding='utf-8', newline='') as file:
        csvreader = csv.reader(file)
        next(csvreader, None)  # пропустить заголовки
        for row in csvreader:
            data = row[0].split(';')
            if data[1] not in report.keys():
                # начали отсчет численности, а список для зарплат
                report[data[1]] = [1, [int(data[5])]]
            else:
                report[data[1]][0] += 1
                report[data[1]][1].append(int(data[5]))
    return report


def menu():
    print(
        'Выберите функцию:\n'
        '1)Иерархия команд в компании.\n'
        '2)Сводный отчет по департаментам.\n'
        '3)Сохранить сводный отчет по департаментам.')
    option = input()
    if option == '1':
        get_hierarchy()
    elif option == '2':
        get_report_print = decorator_printing(get_report)
        get_report_print()
    elif option == '3':
        get_report_csv = decorator_saving_csv(get_report)
        get_report_csv()
    else:
        print('Вы ввели некоректное значение. Попробуйте еще.')
        menu()


if __name__ == '__main__':
    menu()

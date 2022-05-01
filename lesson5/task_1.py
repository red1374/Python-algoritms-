# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно
# вывести наименования предприятий, чья прибыль ниже среднего.
from collections import defaultdict


def print_companies(companies_list, sort_list=False, is_desc=False):
    """
    Print companies list sorted by annual profit value
    :param companies_list: dict with companies
    :param sort_list: True if it sorting is needed
    :param is_desc: sortin direction
    :return:
    """
    if sort_list:
        companies_list = dict(sorted(companies_list.items(), key=lambda x: x[1][4], reverse=is_desc))

    for company_name, profits in companies_list.items():
        print(f'\t{company_name}\t{profits[4]}')


company = defaultdict()
less_avg = dict()
grater_avg = dict()

while True:
    company_count = input('Input company count:\n')
    if not company_count.isdigit() or int(company_count) <= 0:
        print('Wrong company count value!')
        continue

    for n in range(1, int(company_count) + 1):
        name = input(f'What\'s a name of company № {n}\n')
        company[name] = []
        for i in range(4):
            while True:
                profit = input(f'Input company profit for quarter № {i + 1}\n')
                if not profit.isdigit() or int(profit) < 0:
                    print('Wrong value type. Input correct value')
                    continue
                company[name] += [int(profit)]
                break

        company[name] += [sum(company[name])]
    avg_profit = sum(i[4] for i in company.values()) / int(company_count)
    # company = sorted(company.items(), key=lambda x: x[1][4])

    for key, value in company.items():
        if value[4] < avg_profit:
            less_avg[key] = value
        elif value[4] > avg_profit:
            grater_avg[key] = value

    print(f'Average profit is "{avg_profit}"')
    print('Companies with profit less than average:')
    print_companies(less_avg, True)
    print('\nCompanies with profit grater than average:')
    print_companies(grater_avg, True, True)
    break

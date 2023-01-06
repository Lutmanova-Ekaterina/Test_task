import json
from datetime import datetime

with open('operations.json', 'r', encoding='utf-8') as file:
    input_file = json.load(file)

data = []
for item in input_file:
    try:
        if item['date']:
            data.append(item)
    except KeyError:
        pass

data_sorted = sorted(data, key=lambda x: (x['date']), reverse=True)

number_operation = 5
last_operation = []

for item in data_sorted:
    if item['state'] == 'EXECUTED':
        last_operation.append(item)
        number_operation -= 1
    if number_operation == 0:
        break

def hide_number(account):
    account_number = account.split(' ')[-1]
    if len(account_number) == 20:
        return f'Счёт **{account_number[16:]}'
    else:
        return f'{" ".join(account.split(" ")[:-1])}' \
               f'{account_number[0:4]} {account_number[4:6]}' \
               f'** **** {account_number[12:]}'

for operation in last_operation:
    date = datetime.strptime(operation['date'][0:10], '%Y-%m-%d')
    print(f'{date.strftime("%d.%m.%Y")} {operation["description"]}')
    try:
        print(f'{hide_number(operation["from"])} -> ', end='')
    except KeyError:
        pass

print(f'{hide_number(operation["to"])}')
print(f'{operation["operationAmount"]["amount"]}' \
      f'{operation["operationAmount"]["currency"]["name"]}')
print()
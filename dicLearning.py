# xinhua = {
#     '麓': '山脚下',
#     '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
#     '蕗': '甘草的别名',
#     '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
# }
# print(xinhua)
# person = dict(
#     name =  '王大锤',
#     age = 55,
#     height = 168,
# )
# print(person)
#
# items1 = dict(zip('ABCDE', '12345'))
# print(items1)  # {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'}
# items2 = dict(zip('ABCDE', range(1, 10)))
# print(items2)  # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
#
# items3 = {x: x ** 3 for x in range(1, 6)}
# print(items3)  # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}


# person = {
#     'name': '王大锤',
#     'age': 55,
#     'height': 168,
#     'weight': 60,
#     'addr': ['成都市武侯区科华北路62号1栋101', '北京市西城区百万庄大街1号'],
#     'car': {
#         'brand': 'BMW X7',
#         'maxSpeed': '250',
#         'length': 5170,
#         'width': 2000,
#         'height': 1835,
#         'displacement': 3.0
#     }
# }
# print(person)
# print(len(person))
# print(person['name'])
# person['age'] = 23
# print(person['age'])

# del person['age']
#
# for key, value in person.items():
#     print(f'{key}:\t{value}')

# sentence = input('输入一句话： ')
# counter = {}
# for ch in sentence:
#     counter[ch] = counter.get(ch, 0) + 1
# sorted_keys = sorted(counter, key=counter.get, reverse=True)
# for key in sorted_keys:
#     print(f'{key}出现了{counter[key]}次。')

stocks = {
    'APPL':192.32,
    'GOOG':1404.34,
    'MSFT': 51.23,
    'FB': 76.45,
    'AMZN': 306.78

}
stocks2 = {key: value for key, value in stocks.items() if value > 100}
print(stocks2)
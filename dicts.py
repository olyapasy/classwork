import pprint
# # initialization
# dict_en_es = {'world': 'mundo',
#               'language': 'idioma',
#               'See you later': 'Hasta la vista'}
# print(dict_en_es)
#
# print(dict_en_es['world'])
#
# dict_en_es['hi'] = 'hola'
# pprint.pprint(dict_en_es)
#
# print(dict_en_es['hi'])
#
#
# capitals = {'UA':'Kiev'}
#
# capitals['US'] = 'Washington'
# capitals['FR'] = 'Paris'
# capitals['EN'] = 'London'
# capitals['JP'] = 'Tokyo'
# #print(capitals)
#
#
#
# # streets = {}
# #
# # streets['Odessa'] = ['Deribasovskaya','Greece','Gayadara']
# # streets['Kiev'] = ['Khrichatik','Volodymirska']
# # pprint.pprint(streets)
# #
#
#
# companys = {}
#
# companys['Apple'] = ['IPhone', 'MacBook', 'Ipad']
# companys['Samsung'] = ['GalaxyS8', 'GalaxyS3','GalaxyS5']
# companys['Logitech'] = ['Mouse', 'Keybord','Microphone']
# pprint.pprint(companys)
#
# #
# # comp = input('Choose company(Apple,Samsung or Logitech):')
# # while comp!='Apple' or comp!='Samsung' or comp!='Logitech':
# #     comp = input('Choose company(Apple,Samsung or Logitech):')
# #
# #
# # print(companys[comp])
#
# companys['Apple'].append('IPod')
# print(companys['Apple'])
#
# del companys['Samsung']
# pprint.pprint(companys)
#
#
# if 'Apple' in companys:
#     del companys['Apple']
#     print("Foubded and deleted")
# else:
#     print("Not found")
#
#
# print(companys)
#
#
# print('*************************************')
# for key in dict_en_es.keys():
#     # print(key,'->',dict_en_es[key])
#     print("%-15s -> %s" % (key,dict_en_es[key]))
#
#
#
# for word_es in dict_en_es.values():
#     print("%s" % (word_es))
#
#
# for k,v in dict_en_es.items():
#     print("%-15s -> %s" % (k,v))
#
#
#
#
# # real examples-2
# person_1 = {'name':'Richard Feynman',
#             'age': 99,
#             'birth_place': 'USA',
#             'birth_date': "1918-01-01",
#             'awards':['Nobel Prize in Phisics', 'USA Science Medal']}
#
# person_2 = {'name':'Albert Einstein',
#             'age': 138,
#             'birth_place': 'Germany',
#             'birth_date': "1879-03-14",
#             'awards':['Nobel Prize in Physics', 'Planck Medal']}
#
# person_3 = {'name':'Nicola Tesla',
#             'age': 161,
#             'birth_place': 'Croatia',
#             'birth_date': "1856-07-10",
#             'awards':['Edison Medal']}
#
# physicits = [person_1, person_2,person_3]
# pprint.pprint(physicits)
#
# person_1['hobby'] = "painting"
# person_2['hobby'] = "violin"
# person_3['hobby'] = "pigeons"
# person_3['hobby'] = "electricity" # second assignment overrides the 1st one
# pprint.pprint(physicits)

print("*******************************************************************************************")

employee_1 = {"name":"Alex", "salary": 10000, "dep": "Sales", "bonus":200}
employee_2 = {"name":"Nick", "salary": 20000, "dep": "Sales"}
employee_3 = {"name":"Sue",  "salary": 50000, "dep": "IT", "bonus":500}
employee_4 = {"name":"Phil", "salary": 5000,  "dep": "BoardOfDirectors", "bonus":10000}

employees = [employee_1, employee_2, employee_3, employee_4]

pprint.pprint(employees)

for i in range(len(employees)):
    current_salary = employees[i]['salary']
    new_salary = current_salary*2
    employees[i]['salary'] = new_salary


pprint.pprint(employees)

for i in range(len(employees)):
    if 'bonus' in employees[i]:
        employees[i]['bonus'] *=2
    else:
        employees[i]['bonus'] = 1000

pprint.pprint(employees)

employees.sort(key=lambda elem: elem['dep'],reverse=True)
pprint.pprint(employees)

employees.sort(key=lambda elem: elem['dep'],reverse=True)
pprint.pprint(employees)

unicodes = {i:chr(i) for i in range(10000) }

pprint.pprint(unicodes)
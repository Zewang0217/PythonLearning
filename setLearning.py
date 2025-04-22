# # 创建
# set1 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
# set2 = set('hello')
# set3 = set([1, 2, 3])
# set4 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
# # print(set1, set2, set3, set4)
#
# # for elem in set1:
# #   print(elem)
#
# # print('Python' in set1, 'python' not in set1)
#
# # print(set1 & set2)
# # print(set1.union(set2))
# # print(set1 - set2)
# # print(set1 ^ set2)
#
# s = {1, 3, 5}
# s.add(2)
# s.add(4)
# s.add(3)
# print(s)
# s.discard(4)
# s.remove(1)
# print(s)
# s.clear()
# print(s)

a, b, *c = range(1, 10)
print(a, b, c)
a, b, c = [1, 10, 100]
print(a, b, c)
a, *b, c = 'hello'

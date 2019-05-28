import mylib

deuces = [2 ** i for i in range(100)]
found = dict()
found_deuces = dict()
for i in range(210, 100000000, 210):
    if not i % 210000:
        print(i)
    dd = mylib.find_composite_dividers(i)
    s = len(dd)
    if s not in found:
        found[s] = True
        if s in deuces:
            found_deuces[s] = i

for s in sorted(found_deuces):
    n = found_deuces[s]
    print(s, n, mylib.gather_dividers(n), mylib.find_composite_dividers(n))
# # data = dict()
# #
# # for i in range(1, 2000000):
# #     dd = mylib.find_composite_dividers(i)
# #     s = len(dd)
# #     if s not in data:
# #         print(s, i, dd)
# #         data[s] = []
# #     if len(data[s]) < 5:
# #         data[s].append(i)
# #
# # for s in sorted(data):
# #     print(s, '>', data[s])
#
# numbers = (1, 2, 6, 24, 120, 840, 7560, 83160, 1081080)
#
# for n in numbers:
#     print(n, mylib.gather_dividers(n))

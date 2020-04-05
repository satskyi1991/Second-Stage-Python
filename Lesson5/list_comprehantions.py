import time
result_list = []

start_loop = time.time()
for i in range(100000):
    result_list.append(i)

end_loop = time.time() - start_loop


start_compr = time.time()
result_list_2 = [i if not i%2 else i**2 for i in range(100000)]

set_compr = {i for i in range(100000)}
print(set_compr)
end_compr = time.time() - start_compr

print(result_list_2)
print(f' Just loop - {end_loop}, Comprehension - {end_compr} ')


a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

compr_dict = {k: v for k, v in enumerate(a)}
print(compr_dict)
© 2020 GitHub, Inc.

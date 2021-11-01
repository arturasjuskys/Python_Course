import time
gen_start_time = time.time()
print(sum(n for n in range(50000000)))
gen_time = time.time() - gen_start_time


list_start_time = time.time()
print(sum([n for n in range(50000000)]))
list_time = time.time() - list_start_time

print(f"generator expresion took: {gen_time} to run 50 000 000")
print(f"list comprehension took: {list_time} to run 50 000 000")
# generator expresion took: 5.6446990966796875 to run 50 000 000
# list comprehension took: 5.23059606552124 to run 50 000 000

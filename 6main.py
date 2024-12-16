import time # импортируем модуль

def binary_search_recursive(func, interval, log_filename, epsilon=1e-5, start_time=None):
        start_time = time.time() # устанавливаем текущее время работы программы с помощью time.time()

    a, b = interval 
    f_a, f_b = func(a), func(b) 

    with open(log_filename, "a") as log:
        log.write(f"Interval: [{a}, {b}], f(a)={f_a}, f(b)={f_b}\n")

    if f_a * f_b > 0:
        with open(log_filename, "a") as log:
            log.write("Корней нет.\n")
        return None

  
    mid = (a + b) / 2
    f_mid = func(mid) 
    elapsed_time = time.time() - start_time

    with open(log_filename, "a") as log:
        log.write(f"Midpoint: {mid}, f(mid)={f_mid}, Time elapsed: {elapsed_time:.5f} sec\n")

   
    if abs(f_mid) < epsilon:
        
        with open(log_filename, "a") as log:

            log.write(f"Корень: {mid}, f(mid)={f_mid}")
        return mid

     if f_a * f_mid < 0:  
        return binary_search_recursive(func, [a, mid], log_filename, epsilon, start_time)
    else: 
        return binary_search_recursive(func, [mid, b], log_filename, epsilon, start_time)

def example_func(x):
    return x**5 - 16*x - 28
with open(log_file, "w") as file:
    pass
log_file = "binary_search_recursive_log.txt"

with open(log_file, "w") as file:
    pass
root = binary_search_recursive(example_func, [2, 3], log_file)
print(f"корень: {root}")

import time
def binary_search_iterative(func, interval, log_filename, epsilon=1e-5):
    start_time = time.time()
    a, b = interval
    f_a, f_b = func(a), func(b)

    with open(log_filename, "w") as log:
        log.write(f"Интервал: [{a}, {b}], f(a)={f_a}, f(b)={f_b}\n")
    if f_a * f_b > 0:
        with open(log_filename, "a") as log:
            log.write("Корней нет.\n")
        return None

   
    while abs(b - a) > 1e-5:
        mid = (a + b) / 2 
        f_mid = func(mid)
        elapsed_time = time.time() - start_time
        with open(log_filename, "a") as log:
            log.write(f"Interval: [{a}, {b}], Midpoint: {mid}, f(mid)={f_mid}, Elapsed: {elapsed_time:.5f} sec\n")

        if abs(f_mid) < tolerance:
            with open(log_filename, "a") as log:
                log.write(f"Корень: {mid}, f(mid)={f_mid},\n")
            return mid
        if func(a) * f_mid < 0:
            b = mid
        else:
            a = mid
return (a + b) / 2
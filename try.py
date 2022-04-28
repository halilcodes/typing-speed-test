import time

input("press enter when ready")

start_time = time.perf_counter()

input("press enterto finish")
finish_time = time.perf_counter()

print(f"time elapsed: {finish_time - start_time:.3}")
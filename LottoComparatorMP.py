import random
from multiprocessing import Pool, Process, Manager, cpu_count

# Static numbers and the function to generate random numbers remain the same
staticNumbers = [4, 6, 12, 19, 22, 27, 31]

def rndNums(size, min_value, max_value):
    array = []
    while len(array) < size:
        new_element = random.randint(min_value, max_value)
        if new_element not in array:
            array.append(new_element)
    array.sort()
    return array

def areArraysIdentical(array1, array2):
    if len(array1) != len(array2):
        return False
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True

def compare_lotto_numbers(seed, result_queue):
    x = 0
    y = 0

    for _ in range(seed):
        lottoNumbersDraw = rndNums(7, 1, 32)
        lottoNumbersPlay = rndNums(7, 1, 32)

        rndResult = areArraysIdentical(lottoNumbersDraw, lottoNumbersPlay)
        if rndResult:
            x += 1

        staticResult = areArraysIdentical(staticNumbers, lottoNumbersDraw)
        if staticResult:
            y += 1

    result_queue.put((x, y))

def print_results(x_total, y_total):
    print("Total numbers of wins for random play:", x_total.value)
    print("Total numbers of wins for static play:", y_total.value)

if __name__ == "__main__":
    try:
        num_simulations = 4000000
        num_processes = cpu_count()  # This will use all available CPU Cores. You can adjust the number of processes as needed

        # Use a Manager to share results across processes
        with Manager() as manager:
            x_total = manager.Value('i', 0)
            y_total = manager.Value('i', 0)
            result_queue = manager.Queue()

            with Pool(num_processes) as pool:
                seeds = [num_simulations // num_processes] * num_processes
                pool.starmap(compare_lotto_numbers, zip(seeds, [result_queue] * num_processes))

            # Create a separate process for printing
            print_process = Process(target=print_results, args=(x_total, y_total))
            print_process.start()
            print_process.join()

    except KeyboardInterrupt:
        pass
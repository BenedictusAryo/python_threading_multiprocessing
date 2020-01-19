# 4 Combine Multiprocessing with Loop
import time
import multiprocessing

# Create simple function that sleep in 1 second
def do_something(seconds):
    print(f'Sleeping {seconds} second(s) ..')
    time.sleep(seconds)
    print('Done Sleeping..')

if __name__ == '__main__':
    # Start counting
    start = time.perf_counter()

    # Create List for each processing
    processes = []
    # Loop n times, for creating multiproces then add to list
    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[2])
        p.start()
        processes.append(p)

    # Loop for processes then join each process
    for process in processes:
        process.join()

    # Finish counting and show script runtime
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} second(s)")

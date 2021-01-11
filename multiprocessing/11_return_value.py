import multiprocessing

def sum_up_to(number):
    return sum(range(1, number + 1))
    
if __name__ == '__main__':
    # Create pool object
    pool = multiprocessing.Pool(4)

    # Run `sum_up_to` 10 times simultaneously
    result = pool.map(sum_up_to, range(10))

    print(result)
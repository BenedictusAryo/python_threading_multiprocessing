import multiprocessing

def sum_up_to(number):
    return sum(range(1, number + 1))
    
if __name__ == '__main__':
    # Create pool object
    pool = multiprocessing.Pool(4)

    # Run `sum_up_to` 10 times simultaneously
    result = [pool.apply_async(sum_up_to,args=(x,)) for x in range(10)]

    # Get output from Result
    output = [p.get() for p in result]

    print(output)
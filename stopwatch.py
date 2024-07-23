import time

def start_stopwatch():
    return time.time()

def end_stopwatch(start_time):
    """
    Function to calculate time difference
    """
    return time.time() - start_time

if __name__ == "__main__":
    input("Please Enter to start the stopwatch ")
    start_time = start_stopwatch()
    input("stop the stopwatch ")
    total_time = end_stopwatch(start_time)
    print(f"the total time: {total_time:.2f} seconds")
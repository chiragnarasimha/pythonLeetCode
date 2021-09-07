import time


def print_execution_time(start_time: int):
    '''
    Will print the time it took to run the code

    :param start_time: start_time = time.time_ns()
    :return: None
    '''
    print("It took {} ms time taken to run the code was"
          .format((time.time_ns() - start_time) * 1e-6))
    print()


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next

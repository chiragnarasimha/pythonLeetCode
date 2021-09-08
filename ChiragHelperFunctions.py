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
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_node_to_array(list_node: ListNode):
    """
    This method will return the existing list as a array
    :return: List is returned as an array
    """
    if list_node is None:
        return []
    return_list = []
    current_node = list_node
    while current_node is not None:
        return_list.append(current_node.val)
        current_node = current_node.next

    return return_list

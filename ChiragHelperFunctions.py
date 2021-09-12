import time


def print_execution_time(start_time: int, message=""):
    """
    Will print the time it took to run the code

    :param message: Custom message if any
    :param start_time: start_time = time.process_time_ns()
    :return: None
    """
    print("It took {time_taken} ms to run the code. {custom_message}"
          .format(time_taken
                  =(time.process_time_ns() - start_time) * 1e-6,
                  custom_message=message)
          )
    print()


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


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


class CustomException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

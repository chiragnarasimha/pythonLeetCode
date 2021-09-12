from ChiragHelperFunctions import ListNode


class LinkedList:
    def __init__(self, val):
        """
        Initialise the list with head  node to start of with
        :param val: The value to be stored in the head
        """
        self.head = ListNode(val, None)
        self.tail = self.head
        self.length = 1

    def __len__(self):
        return self.length

    def __str__(self):
        message = """The Contents of your linked list are
        Head: {}
        Tail: {}
        List: {}
        Length: {}
        """
        return message.format(self.head, self.tail, self.to_str(),
                              len(self))

    def get_node(self, index) -> ListNode:
        """
        Specify the index till which you want to keep traversing to
        :param index: index of the node to traverse to
        :return:
        """
        curr_node = self.head
        # while curr_node.next is not None:
        for _ in range(index):
            curr_node = curr_node.next
        return curr_node

    def to_str(self):
        curr_node = self.head
        res = "[ "
        while curr_node is not None:
            res += ("{} ".format(curr_node.val))
            curr_node = curr_node.next
        return res + "]"

    def append(self, val):
        """
        This method will append the value to the tail of the linked list
        :param val: Value to insert at the end of the list
        """
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        self.length += 1
        # print(self.__list_to_str())

    def prepend(self, val):
        """
        Attach to the start of the linked list
        :param val: Value to attach at the start
        """
        new_node = ListNode(val, self.head)
        self.head = new_node
        self.length += 1

    def insert(self, val, index):
        """
        Insert the value at the specified index
        :param val:
        :param index:
        """
        # Check if we are attaching at index 0
        if index == 0:
            raise SyntaxError('To insert at index 0, use prepend method '
                              'instead')
        # Get the previous node that was stored in this index
        new_node = ListNode(val)
        prev_node = self.get_node(index - 1)
        current_node = prev_node.next
        prev_node.next = ListNode(val, current_node)
        new_node.next = current_node
        self.length += 1

        # Check if we need to update the tail
        if current_node.next is None:
            self.tail = current_node

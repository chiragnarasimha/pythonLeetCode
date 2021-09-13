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
        Head: {} -> {}
        Tail: {} -> {}
        List: {}
        Length: {}
        """
        return message.format(self.head, self.head.next, self.tail,
                              self.tail.next,
                              self.__to_str(),
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

    def __to_str(self):
        curr_node = self.head
        res = "[ "
        while curr_node is not None:
            res += ("\n\t\t\t\t{} -> {} ".format(curr_node.val, curr_node.next))
            curr_node = curr_node.next
        return res + "\n\t\t\t  ]"

    def to_arr(self):
        curr_node = self.head
        res = []
        while curr_node is not None:
            res.append(curr_node.val)
            curr_node = curr_node.next
        return res

    def append(self, val):
        """
        This method will append the value to the tail of the linked list
        :param val: Value to insert at the end of the list
        """
        new_node = ListNode(val, None)
        self.tail.next = new_node
        self.tail = new_node
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

    def reverse(self):
        # The very first thing to do is to check if the head node even has a
        # next
        if self.head.next is None:
            return self

        # We need these nodes to go through the list
        # [ 1 2 3 4 5 6 7 8 ]
        prev_node = None
        current_node = self.head
        next_node = current_node.next

        # Swap the head and tail before modifying the list
        self.head, self.tail = self.tail, self.head
        while next_node is not None:
            # Store the next node in the list first
            next_node = current_node.next
            # The current node should be pointing to the previous node
            current_node.next = prev_node
            prev_node = current_node
            # Traverse through the list
            current_node = next_node

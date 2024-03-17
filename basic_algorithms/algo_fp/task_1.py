class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("The previous node does not exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sorted_lists(self, other_list):
        merged_list = LinkedList()
        current_self = self.head
        current_other = other_list.head

        while current_self is not None and current_other is not None:
            if current_self.data < current_other.data:
                merged_list.insert_at_end(current_self.data)
                current_self = current_self.next
            else:
                merged_list.insert_at_end(current_other.data)
                current_other = current_other.next

        while current_self is not None:
            merged_list.insert_at_end(current_self.data)
            current_self = current_self.next

        while current_other is not None:
            merged_list.insert_at_end(current_other.data)
            current_other = current_other.next

        return merged_list

    def sorted_insert(self, sorted_head, new_node):
        if sorted_head is None or sorted_head.data >= new_node.data:
            new_node.next = sorted_head
            return new_node

        current = sorted_head
        while current.next is not None and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return sorted_head

    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_head = None

        current = self.head
        while current:
            next_node = current.next
            sorted_head = self.sorted_insert(sorted_head, current)
            current = next_node

        self.head = sorted_head



if __name__ == "__main__":
    llist_1 = LinkedList()

    llist_1.insert_at_beginning(2)
    llist_1.insert_at_beginning(5)
    llist_1.insert_at_beginning(6)
    llist_1.insert_at_beginning(8)

    llist_1.insert_at_end(13)

    print("llist 1")
    llist_1.print_list()

    # reverce
    print("Reverce llist")
    llist_1.reverse()
    llist_1.print_list()

    # insertion sort
    print("Insertion sort")
    llist_1.insertion_sort()
    llist_1.print_list()


    # llist 2
    llist_2 = LinkedList()
    llist_2.insert_at_beginning(4)
    llist_2.insert_at_beginning(1)
    llist_2.insert_at_beginning(6)
    llist_2.insert_at_end(9)
    llist_2.insert_at_end(12)

    print("===" * 10)
    print("llist 2")
    llist_2.insertion_sort()
    llist_2.print_list()



    # merge
    print("===" * 10)
    print("merge llist")
    merged_list = llist_1.merge_sorted_lists(llist_2)
    merged_list.print_list()
class Element:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def Print(self, times=0):
        """ Print Element and continue for number of times

        Parameters:
            times: int, number of element to print, 0 would print all
        """
        if type(times) is not int or times < 0:
            raise TypeError("times must be an int larger or equal to 0.")
        output = []
        node = self
        all = 0 == times
        while node and (all or times > 0):
            output.append(node.value)
            node = node.next
            times -= 1
        print(" -> ".join(output))

    def Next(self):
        """ Return next element of self"""
        return self.next

    def Previous(self):
        """ Return previous element of self"""
        return self.previous

    def First(self):
        """ Return the first element of self """
        node = self
        while node.previous:
            node = node.previous
        return node

    def Last(self):
        """ Return the last element of self """
        node = self
        while node.next:
            node = node.next
        return node

    def Nth(self, n):
        """ Get the N-th element relative to self

        Parameters:
            n: int, the N-th element to return
        Returns:
            node: Element, the N-th element
        """
        if type(n) is not int or n < 0:
            raise ValueError("n must be an int larger or equal to 0.")
        node = self
        while node and n > 0:
            node = node.next
            n -= 1
        if not node:
            raise ValueError("n is larger than the size of LinkedList.")
        return node

    def Append(self, item):
        """ Append item to the end of the linked list

        Parameters:
            item: Element or str, item to append
        """
        node = self.Last()
        node.next = item if isinstance(item, Element) else Element(item)
        node.next.previous = node

    def Insert(self, item, index=0):
        """ Insert item at index 0 relative to self

        Parameters:
            item: Element or str: item to insert
            index: index to insert relative to self
        """
        nth = self.Nth(index)
        previous = nth.previous
        node = item if isinstance(item, Element) else Element(item)
        # update next and previous of the tail of inserted node
        last = node.Last()
        last.next = nth
        nth.previous = last
        # update next and previous of the head of inserted node
        if previous:
            node.previous = previous
            previous.next = node

    def Remove(self):
        """ Remove pointers to self"""
        if self.next: self.next.previous = self.previous
        if self.previous: self.previous.next = self.next

    def TearDown(self):
        """ Remove pointers to self and after self"""
        node = self
        if node.previous: node.previous.next = None
        while node:
            temp = node.next
            del node
            node = temp

    def BruteSearch(self, value):
        """ Brute force search value in linked list

        Parameters:
            value: str, value to search
        """
        node = self
        while node:
            if node.value == value:
                return node
            node = node.next

    def GetMiddle(self, last=None):
        """ Get the middle element in an linked list relatively to self

        Parameters:
            last (optional): Element, the last element to search for middle
        Returns:
            slow: Element, the middle element
        """
        slow = fast = self
        while fast and fast.next and (not last or last is not fast):
            fast = fast.next
            if fast and (not last or last is not fast):
                fast = fast.next
                slow = slow.next
        return slow

    def Merge(self, left, right):
        """ Merge and sort two linked lists

        Parameters:
            left: Element, head Element of the first linked list
            right: Element, head Element of the second linked list
        Returns:
            sorted: Element, head Element of the sorted linked list
        """
        if not left and not right:
            return None
        sorted = node = Element('temp')
        while left and right:
            if left.value < right.value:
                node.next = left
                left.previous = node
                left = left.next
            else:
                node.next = right
                right.previous = node
                right = right.next
            node = node.next

        if not left:
            node.next = right
            right.previous = node
        if not right:
            node.next = left
            left.previous = node

        sorted.next.previous = None
        return sorted.next

    def Sort(self, head=None):
        """ Sort linked list from head

        Parameters:
            head: Element, element to sort, None to start sorting from root
        Returns:
            sorted: Element, root of the sorted linked list
        """
        # get root of LinkedList
        root = head if head else self.First()
        if not root or not root.next:
            return root
        # get middle element
        mid = root.GetMiddle()
        mid.previous.next = None
        mid.previous = None
        left = mid.Sort(head=root)
        right = mid.Sort(head=mid)

        sorted = root.Merge(left, right)

        return sorted

    def BinarySearch(self, value):
        """ Binary search in linked list for value

        Parameters:
            value: str, value to search
        Returns:
            node: Element, the elemenet with value
        """
        if self.value == value:
            return self
        start = self
        end = None
        while not end or start.next is not end:
            mid = start.GetMiddle(last=end)
            if mid.value == value:
                return mid
            elif mid.value < value:
                start = mid
            else:
                end = mid
        return None


def main():
    # construct list
    root = Element("Hello")

    root.Append(Element("World"))
    root.Append(Element("This"))
    root.Append(Element("Is"))
    root.Append(Element("a"))
    root.Append(Element("Linked"))
    root.Append(Element("List"))
    root.Append(Element("of"))
    root.Append(Element("Strings"))
    root.Print(0)

    # test finding nodes
    nth = root.Nth(3)
    nth.Print(1)
    nth.Previous().Print(1)
    nth.Next().Print(1)
    nth.First().Print(1)
    nth.Last().Print(1)

    # test appending and inserting
    nth.Append(Element("."))
    nth.Last().Print()

    nth.Insert(Element("Definitely"))
    root.Print(0)

    secondList = Element("Second")
    secondList.Append(Element("List"))

    nth.Insert(secondList.Last())
    root.Print(0)

    nth.Remove()
    del nth
    root.Print(0)

    # check brute, sort and binary search
    found = root.BruteSearch("of")
    found.Print(1)

    found = root.BinarySearch("List")
    if found:
        found.Print(1)

    root = root.Sort()
    root.Print(0)

    found = root.BinarySearch("List")
    found.Print(1)

    # tear down
    found.TearDown()
    root.Print(0)
    root.TearDown()
    del root


if __name__ == "__main__":
    main()

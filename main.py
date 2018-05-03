class Element:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def Print(self, times=0):
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
        return self.next

    def Previous(self):
        return self.previous

    def First(self):
        node = self
        while node.previous:
            node = node.previous
        return node

    def Last(self):
        node = self
        while node.next:
            node = node.next
        return node

    def Nth(self, n):
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
        node = self.Last()
        node.next = item if isinstance(item, Element) else Element(item)
        node.next.previous = node

    def Insert(self, index, item):
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
        if self.next: self.next.previous = self.previous
        if self.previous: self.previous.next = self.next

    def TearDown(self):
        pass

    def BruteSearch(self, value):
        node = self
        while node:
            if node.value == value:
                return node
            node = node.next

    def GetMiddle(self, last=None):
        slow = fast = self
        while fast and fast.next and (not last or last is not fast):
            fast = fast.next
            if fast and (not last or last is not fast):
                fast = fast.next
                slow = slow.next
        return slow

    def Merge(self, left, right):
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
        if self.value == value:
            return self
        start = self
        end = None
        while not end or end.next is not start:
            mid = start.GetMiddle(end)
            if mid.value == value:
                return mid
            elif mid.value < value:
                start = mid
            else:
                end = mid
        return None


if __name__ == "__main__":
    # node = Element("Hello")
    # nodes = ["World", "a", "Linked", "List"]
    # for i in nodes:
    #     node.Append(i)
    # print("all")
    # node.Print(times=0)
    # print("\nnext 1")
    # node.Next().Print(times=1)
    # print("\nlast all")
    # node.Last().Print(times=0)
    # print("\nlast first 1")
    # node.Last().First().Print(times=1)
    # print("\n3rd all")
    # node.Nth(3).Print(times=0)
    # node.Append(Element("Last"))
    # node.Print(times=0)
    # node.Insert(1, "Insert")
    # node.First().Print(times=0)
    # nodes = ["Third", "Fourth"]
    # second = Element("Second")
    # for i in nodes:
    #     second.Append(i)
    # node.Insert(1, second)
    # node.Print(times=0)
    # print("remove")
    # node.Nth(1).Remove()
    # node.Print(times=0)
    node = Element("5")
    nodes = ["4", "3", "2", "1"]
    for i in nodes:
        node.Append(i)
    node.Print()
    sorted = node.Sort()
    sorted.Print()
    found = sorted.BinarySearch("2")
    if found:
        found.Print()

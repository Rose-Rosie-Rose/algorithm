# 원형연결리스트의 구현
# 단순연결리스트와의 차이점은 마지막에서 첫번째를 가리킬 수 있음.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # 리스트의 끝에 노드를 추가
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    # 리스트의 시작에 노드를 추가
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    # 특정 값의 노드를 삭제
    def delete_node(self, key):
        if self.head:
            if self.head.data == key:
                if self.head.next == self.head:  # 리스트에 노드가 하나만 있는 경우
                    self.head = None
                else:
                    temp = self.head
                    while temp.next != self.head:
                        temp = temp.next
                    temp.next = self.head.next
                    self.head = self.head.next
            else:
                prev = None
                temp = self.head
                while temp.next != self.head:
                    if temp.data == key:
                        break
                    prev = temp
                    temp = temp.next

                if temp.data == key:
                    prev.next = temp.next

    # 리스트를 출력
    def print_list(self):
        temp = self.head
        if self.head:
            while True:
                print(temp.data, end=" -> ")
                temp = temp.next
                if temp == self.head:
                    break
            print("HEAD")
        else:
            print("리스트가 비어 있습니다")

    # 리스트의 길이를 반환
    def length(self):
        count = 0
        temp = self.head
        if self.head:
            while True:
                count += 1
                temp = temp.next
                if temp == self.head:
                    break
        return count

    # 리스트에서 특정 값을 검색
    def search(self, key):
        temp = self.head
        if self.head:
            while True:
                if temp.data == key:
                    return True
                temp = temp.next
                if temp == self.head:
                    break
        return False
# 단순연결리스트의 구현
# 노드를 만들기 위하여 파이썬의 클래스를 사용하여 노드를 정의함
# 이 자료에서 노드는 연결리스트에서 데이터 하나를 담는 한 칸

class Node:
    def __init__(self, data):
        self.data = data   # 데이터 필드
        self.next = None   # 링크 필드

class LinkedList:
    def __init__(self):
        self.head = None   # Head는 제일 첫번째

    # 리스트의 끝에 노드를 추가
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # 리스트의 시작에 노드를 추가
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 특정 값의 노드를 삭제
    def delete_node(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None

    # 리스트를 출력
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # 리스트의 길이를 반환
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # 리스트에서 특정 값을 검색
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

# 실행부
# 연결 리스트 객체 생성
llist = LinkedList()

# 노드 추가
llist.append(1)
llist.append(2)
llist.append(3)
llist.prepend(0)

# 리스트 출력
llist.print_list()

# 특정 값 검색
print("3을 찾았나요?", llist.search(3))    # 출력: True
print("5를 찾았나요?", llist.search(5))    # 출력: False

# 특정 값 삭제
llist.delete_node(2)
llist.print_list()

# 리스트 길이 출력
print("리스트의 길이:", llist.length())

# 실행 결과
# 0 -> 1 -> 2 -> 3 -> None
# 3을 찾았나요? True
# 5를 찾았나요? False
# 0 -> 1 -> 3 -> None
# 리스트의 길이: 3
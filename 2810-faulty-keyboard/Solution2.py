# https://leetcode.com/problems/faulty-keyboard/submissions/1018020966/
class Solution:
    def finalString(self, s: str) -> str:
        response = MyString()

        for letter in s:
            if letter != "i":
                response.addLetter(letter)
            else:
                response.reverse()

        return response.toString()

class MyString:
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(None, None, None)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.normal = True
    
    def addLetter(self, letter):
        node = Node(letter, None, None)
        if self.normal:
            node.next = self.tail
            node.prev = self.tail.prev
            self.tail.prev.next = node
            self.tail.prev = node
        else:
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
    
    def reverse(self):
        self.normal = False if self.normal else True
        
    def toString(self):
        res = ""
        if self.normal:
            curr = self.head.next
            while curr != self.tail:
                res = res + curr.val
                curr = curr.next
        else:
            curr = self.tail.prev
            while curr != self.head:
                res = res + curr.val
                curr = curr.prev

        return res


class Node:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev

    

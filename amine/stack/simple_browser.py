"""
@File    :   simple_browser.py
@Time    :   2024/8/13 10:54
@Author  :   LinLi6
@Desc    :   

@usage   :
    
"""
from algo.amine.linkedlist.single_linked_list import Node
from algo.amine.stack.linked_stack import LinkedStack


class NewLinkedStack(LinkedStack):
    def is_empty(self):
        return not self.top


class Browser:
    def __init__(self):
        self.forward_stack = NewLinkedStack()
        self.back_stack = NewLinkedStack()

    def can_forward(self):
        return not self.forward_stack.is_empty()

    def can_back(self):
        return not self.back_stack.is_empty()

    def open(self, url):
        print(f"Open new url : {url} \n")
        self.forward_stack.push(url)

    def back(self):
        if self.forward_stack.is_empty():
            return
        top = self.forward_stack.pop()
        self.back_stack.push(top)
        print(f"Back to {top}\n")

    def forward(self):
        if self.back_stack.is_empty():
            return

        top = self.back_stack.pop()
        self.forward_stack.push(top)
        print(f"Forward to {top}\n")


if __name__ == '__main__':

    browser = Browser()
    browser.open('a')
    browser.open('b')
    browser.open('c')
    if browser.can_back():
        browser.back()

    if browser.can_forward():
        browser.forward()

    browser.back()
    browser.back()
    browser.back()

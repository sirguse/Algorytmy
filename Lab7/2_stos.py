class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self): 
        return  self.items[len(self.items)-1]
    def size(self):
        return len(self.items)


def sprawdzanie(znak):
    s = Stack()
    poprawny = True
    index = 0
    while index < len(znak) and poprawny:
        a = znak[index]
        if a == "(": s.push(a)
        else:
            if s.size()==0:
                poprawny=False
            else:
                s.pop()

        index += 1

    if s.size()==0 and poprawny:
        return True
    else:
        return False


znak = "((()))"
print(sprawdzanie(znak)) 

znak2 = "((())))"
print(sprawdzanie(znak2)) 
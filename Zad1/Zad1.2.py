from Stack import Stack


def read(name):
    file = open(name, "r")
    list = file.read().splitlines()
    file.close()
    print(list)
    return list


def clear_stack(stack, temp):
    for i in range(stack.Size()):
        if stack.Top() == '(':
            stack.Pop()
            break
        else:
            if stack.Top() != '(':
                temp += stack.Top()
            stack.Pop()
    return temp


def ONP(list):
    stack= Stack()
    output = []
    temp =""
    dictionary ={
        '^': 3,
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
        '(': 0
    }
    for item in list:
        for char in item:
            if char in dictionary and char != '(':
                if stack.isEmpty():
                    stack.Push(char)
                elif dictionary.get(char) <= dictionary.get(stack.Top()):
                    temp += stack.Top()
                    stack.Pop()
                    stack.Push(char)
                elif dictionary.get(char) > dictionary.get(stack.Top()):
                    stack.Push(char)
            elif char == '(':
                stack.Push(char)
            elif char == ')':
                temp = clear_stack(stack, temp)
            elif char == '=':
                temp = clear_stack(stack, temp)
                output.append(temp)
                temp = ""
            else:
                temp += char
    print(output)



ONP(read("Zad1.2(INF).txt"))

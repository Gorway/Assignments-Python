def merge(succession):
    result = []
    while succession:
        for element in succession:
            head = element[0]
            if not any(head in s[1:] for s in succession):
                break
        else:
            raise TypeError("Unable to resolve inheritance order")

        result.append(head)
        for element in succession:
            if element and element[0] == head:
                element.pop(0)

        succession = [element for element in succession if element]

    return result

def c3_mro(cls):
    return merge([[cls]] + [c3_mro(base) for base in cls.__bases__] + [list(cls.__bases__)])

class O: pass
class F(O): pass
class E(O): pass
class D(O): pass
class C(D, F): pass
class B(D, E): pass
class A(B, C): pass


print([cls.__name__ for cls in c3_mro(A)])

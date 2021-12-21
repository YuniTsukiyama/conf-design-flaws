#!/usr/bin/python3

def compute_value(a: int, b: int, c:int) -> int:
    """ return result of compilation or error message if failed *screams*
    """
    if a:
        res = a + b
    else:
        res = a + c
    if not(res):
        return "computation failed"
    return res

if __name__ == "__main__":

    print(compute_value(1, 2, 5))
    print(compute_value(1, 2, "hello"))
    print(compute_value(0, 2, 5))

    print(compute_value("a", "b", 1238576))

    print(compute_value(0, 1, "hello"))

def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def sub(a,b):
    return a-b
def div(a,b):
    try:
        return a/b
    except Exception:
        return "Infinity"

print(div(1,-1))


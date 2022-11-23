a = 1
b = 0
try:
    print(a/b)
except Exception:
    print("Infinite")
finally:
    print("I am not obeying try and except block")

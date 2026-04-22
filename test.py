def cap(n):
    sep=n.split()
    cap=[word.capitalize() for word in sep]
    return " ".join(cap)

a="hello world"
print(cap(a))
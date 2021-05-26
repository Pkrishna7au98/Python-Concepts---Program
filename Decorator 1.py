def div(a,b):
    return a/b

def ofun(fn):
    def fn2(a,b):
        if a<b:
            a,b=b,a
        return fn(a,b)
    return fn2

abc = ofun(div)

print(abc(2,6))


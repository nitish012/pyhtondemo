def generate():
    yield 1
    yield 2
    yield 3

for x in generate():
    print(x)

def generating(values):
    yield values*2
    yield values /2

for x in generating(12):
    print (x)

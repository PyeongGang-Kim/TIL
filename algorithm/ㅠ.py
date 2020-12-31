def coro():
    hello = yield "Hello"
    print(hello)
    print(1)
    yield hello


c = coro()
print(next(c))
print(c.send("hihi"))

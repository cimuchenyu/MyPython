def foo():
    print("starting...")
    while True:
        print("start while...")
        res = yield 4
        print("res:",res)


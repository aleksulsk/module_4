def test_function():
    print("Как дела?")
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()
    return


test_function()

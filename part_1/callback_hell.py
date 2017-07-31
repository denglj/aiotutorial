#!/usr/bin/env python
# encoding: utf-8

# def callback_1():
    # # processing ...
    # def callback_2():
        # # processing.....
        # def callback_3():
            # # processing ....
            # def callback_4():
                # #processing .....
                # def callback_5():
                    # # processing ......
                # async_function(callback_5)
            # async_function(callback_4)
        # async_function(callback_3)
    # async_function(callback_2)
# async_function(callback_1)


def a(result):
    result = result + 'a'
    print(result)
    return result

def b(result):
    1/0
    result = result + 'b'
    print(result)
    return result

def c(result):
    result = result + 'c'
    print(result)
    return result


a(b(c('1')))

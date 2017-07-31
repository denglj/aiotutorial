#!/usr/bin/env python
# encoding: utf-8

import socket
from concurrent import futures


def blocking_way():
    sock = socket.socket()
    # blocking
    sock.connect(('example.com', 80))
    request = 'GET / HTTP/1.0\r\nHost: example.com\r\n\r\n'
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        # blocking
        chunk = sock.recv(4096)
    return response


def thread_way():
    workers = 10
    with futures.ThreadPoolExecutor(workers) as executor:
        futs = {executor.submit(blocking_way) for i in range(10)}
    return len([fut.result() for fut in futs])


def sync_way():
    res = []
    for i in range(10):
        res.append(blocking_way())
    return len(res)


def main():
    start = time.time()
    print(thread_way())
    print(time.time() - start)


if __name__ == '__main__':
    import time
    main()

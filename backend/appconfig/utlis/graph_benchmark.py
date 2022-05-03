# Copyright 2022 the author Rodney Sostras. All rights reserved.

import time
import heapq
from collections import deque

SIZE = 1000000

def test_list():
    l = list(range(SIZE))
    tick = time.time()

    while l:
        l.pop(0)

    return "[LIST] time: %.2f sec"%( time.time() - tick)

def test_dict():
    d = {i: i ** 3 for i in range(SIZE)}
    tick = time.time()

    while d:
        d.popitem()

    return "[DICT] time: %.2f sec"%( time.time() - tick)

def test_deque():
    dq = deque(range(SIZE))
    tick = time.time()
    while dq:
        dq.popleft()

    return "[DEQUE] time: %.2f sec"%( time.time() - tick)

def test_heapq():
    pq = list(range(SIZE))
    tick = time.time()
    while pq:
        heapq.heappop(pq)
        
    return "[HEAPQ] time: %.2f sec"%( time.time() - tick)

def test_set():
    s = set(range(SIZE))
    tick = time.time()
    while s:
        s.pop()
        
    return "[SET] time: %.2f sec"%( time.time() - tick)

def test_set_search():
    s = set(range(SIZE))
    tick = time.time()
    for _ in s:
        if 100 in s:
            pass
        
    return "[SET-SEARCH] time: %.2f sec"%( time.time() - tick)

def test_deque_search():
    d = deque(range(SIZE))
    tick = time.time()
    for _ in d:
        if 100 in d:
            pass
        
    return "[DEQUE-SEARCH] time: %.2f sec"%( time.time() - tick)

# python -m timeit "import dijkstra_benchmark; dijkstra_benchmark.test_deque_search()"

#!/usr/bin/env python3

"""
A function that takes in 2 int arguments n and max_delay,
measures the total excecution time for wait_n(n, max_delay),
and returns total_time / n
"""


import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Takes 2 int arguments n and max_delay and returns a float
    measuring the average execution time per task
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()
    return (end_time - start_time) / n

#!/usr/bin/env python3

"""
An async routine that takes in 2 int arguments n and max_delay
and returns the list of n delays (in ascending order)
"""


import asyncio
from heapq import heappush, heappop
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Takes 2 int argumentsn and man_delay and returns a list of n
    delays in ascending order
    """
    delays: List[float] = []
    tasks: List[asyncio.task] = [
        asyncio.create_task(wait_random(max_delay)) for _ in range(n)
    ]
    for task in asyncio.as_completed(tasks):
        delay: float = await task
        heappush(delays, delay)
    return [heappop(delays) for _ in range(len(delays))]

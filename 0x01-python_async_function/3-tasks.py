#!/usr/bin/env python3


"""
A function that takes an integer max_delay and returns an
asyncio.Task
"""


import asyncio
from typing import Type

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task
    that runs the wait_random coroutine
    """

    return asyncio.create_task(wait_random(max_delay))

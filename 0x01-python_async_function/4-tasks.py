#!/usr/bin/env python3
"""
task 4
"""

import typing
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    anything
    """

    upcoming = []
    for _ in range(n):
        upcoming.append(task_wait_random(max_delay))

    output = []
    for u in asyncio.as_completed(upcoming):
        output.append(await u)

    return output

# n = 5
# max_delay = 6
# print(asyncio.run(task_wait_n(n, max_delay)))

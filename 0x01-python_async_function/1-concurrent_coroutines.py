#!/usr/bin/env python3
"""
task 1
"""


import typing
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    anything
    """
    upcoming = []
    for _ in range(n):
        upcoming.append(wait_random(max_delay))

    output = []
    for u in asyncio.as_completed(upcoming):
        output.append(await u)

    return output

# print(asyncio.run(wait_n(5, 5)))
# print(asyncio.run(wait_n(10, 7)))
# print(asyncio.run(wait_n(10, 0)))

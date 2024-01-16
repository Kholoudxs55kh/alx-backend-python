#!/usr/bin/env python3
"""
task 0
"""

import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    anything
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


# async def print_yielded_values():
#     result = []
#     async for i in async_generator():
#         result.append(i)
#     print(result)

# asyncio.run(print_yielded_values())

#!/usr/bin/env python3
"""
task 1
"""

import typing
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    anything
    """
    output = []
    async for value in async_generator():
        output.append(value)

    return output

# async def main():
#     print(await async_comprehension())

# asyncio.run(main())

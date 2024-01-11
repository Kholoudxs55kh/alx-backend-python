#!/usr/bin/env python3
"""
type annotated task 9
"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    takes a float and return it multiblied by multiblier
    """
    return lambda x: x * multiplier

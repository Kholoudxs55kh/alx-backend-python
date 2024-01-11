#!/usr/bin/env python3
"""
type annotated task 8
"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    takes a str and float/int and returns a tuple
    """
    return (k, v**2)

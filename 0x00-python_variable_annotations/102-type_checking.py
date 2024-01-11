#!/usr/bin/env python3
"""
type annotated task adv 3
"""
import typing


def zoom_array(lst: typing.Tuple, factor: int = 2) -> typing.List:
    """
    fixing its type annotation
    """
    factor = int(factor)
    zoomed_in: typing.List = [
        item for item in list(lst)
        for i in range(factor)
    ]
    return zoomed_in

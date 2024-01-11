#!/usr/bin/env python3
"""
type annotated task adv 2
"""
import typing
T = typing.TypeVar('T')


def safely_get_value(dct: typing.Mapping, key: typing.Any, default:
                     typing.Union[T, None] = None) -> \
                     typing.Union[typing.Any, T]:
    """
    fixing its type annotation
    """
    if key in dct:
        return dct[key]
    else:
        return default

# -*- coding:utf-8 -*-
from __future__ import print_function
import time
import logging


def timing(func):
    def wrapper(*args, **kwargs):
        tic = time.time()
        print("=" * 40)
        print("> %s, {%s} start" % (time.strftime("%X", time.localtime()), func.__name__))
        back = func(*args, **kwargs)
        print("> %s, {%s} end" % (time.strftime("%X", time.localtime()), func.__name__))
        print("> %.5fs taken for {%s}" % (time.time() - tic, func.__name__))
        print("-" * 40)
        return back
    return wrapper


def timing_log(func):
    def wrapper(*args, **kwargs):
        tic = time.time()
        back = func(*args, **kwargs)
        logging.info("Elapsing time of <%s> is %.3fs" % (func.__name__, time.time() - tic))
        return back
    return wrapper





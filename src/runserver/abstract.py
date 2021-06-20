"""
This is a abstract class that should use in all applications
"""

import threading

from abc import ABC, abstractmethod


class AbstractProtocol(ABC):
    def __init__(self, *args, **kwargs):
        t = threading.Thread(target=self.protocol, args=(args, kwargs))
        t.start()

    @abstractmethod
    def protocol(self, *args, **kwargs):
        pass

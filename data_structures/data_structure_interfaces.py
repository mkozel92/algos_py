from abc import ABC, abstractmethod
from typing import Any


class Queue(ABC):

    @abstractmethod
    def enqueue(self, data: Any):
        """
        add new element to the back of the queue
        :param data: data to enqueue
        """
        pass

    @abstractmethod
    def dequeue(self) -> Any:
        """
        return element from the front of the queue
        """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """
        Check if the queue is empty
        """
        pass


class Stack(ABC):

    @abstractmethod
    def push(self, data: Any):
        """
        add new element to the top of the stack
        :param data: data to put on the stack
        """
        pass

    @abstractmethod
    def pop(self) -> Any:
        """
        return element from the top of the
        """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """
        Check if the stack is empty
        """
        pass

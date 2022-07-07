"""This module contains an abstract BaseHost class."""
from abc import ABC, abstractmethod


class BaseHost(ABC):
    """
    An abstract method to initialize a host OS type
    """

    @property
    @abstractmethod
    def distribution(self):
        """It is an abstract method which describes host OS type."""
        pass

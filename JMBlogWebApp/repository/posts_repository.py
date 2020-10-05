import abc
from abc import ABCMeta

class PostsRepository(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, sub):
        if cls is PostsRepository:
            if any('__iter__' in Q.__dict__ for Q in sub.__mro__):
                return True
            return False
        return NotImplemented

    @abc.abstractmethod
    def add_post(self, item):
        pass

    @abc.abstractclassmethod
    def update_post(self, item):
        pass

    @abc.abstractmethod
    def get_all(self):
        pass

    @abc.abstractmethod
    def get_by_id(self, index):
        pass

    @abc.abstractmethod
    def remove(self, index):
        pass

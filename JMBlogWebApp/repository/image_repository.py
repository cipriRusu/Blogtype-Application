import abc
from abc import ABCMeta

class ImageRepository(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, sub):
        if cls is ImageRepository:
            if any('__iter__' in Q.__dict__ for Q in sub.__mro__):
                return True
            return False
        return NotImplemented

    @abc.abstractmethod
    def add_image(self, blog_post, added_image):
        pass

    @abc.abstractmethod
    def remove_image(self, blog_post):
        pass

    @abc.abstractmethod
    def get_image(self, blog_post):
        pass

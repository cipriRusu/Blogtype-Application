import abc
from abc import ABCMeta

class UsersRepository(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, sub):
        if cls is UsersRepository:
            if any('__iter__' in Q.__dict__ for Q in sub.__mro__):
                return True
            return False
        return NotImplemented

    @abc.abstractmethod
    def add_user(self, user):
        pass

    @abc.abstractclassmethod
    def update_user(cls, user):
        pass

    @abc.abstractmethod
    def get_users(self):
        pass

    @abc.abstractmethod
    def get_user_by_id(self, user_id):
        pass

    @abc.abstractclassmethod
    def get_by_name_and_pass(cls, username, password):
        pass

    @abc.abstractmethod
    def remove_user(self, user_id):
        pass

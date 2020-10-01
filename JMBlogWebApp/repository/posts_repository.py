import abc

class PostsRepository(abc.ABC):
    @abc.abstractmethod
    def add_post(self, item):
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
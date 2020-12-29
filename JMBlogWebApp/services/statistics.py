from models.user_statistics import UserStatistics

class Statistics():
    def __init__(self, posts_repository):
        self._posts = posts_repository
        self._stats = UserStatistics()

    def get_statistics(self, selected_user):
        username = None if selected_user in (None, 'All Users') else selected_user
        self._stats.set_name(username)
        self._stats.set_posts(self._posts.get_all(username))
        return self._stats

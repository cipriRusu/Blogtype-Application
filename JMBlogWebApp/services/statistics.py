class Statistics():
    def __init__(self, posts_repository):
        self._posts = posts_repository

    def get_statistics(self, selected_user):
        username = None if selected_user in (None, 'All Users') else selected_user

        total_stats = {}

        for post in self._posts.get_all(username):
            total_stats.setdefault(post.stamp.creation_time.year, [])
            (total_stats[post.stamp.creation_time.year]
             .append(post
                     .stamp
                     .creation_time
                     .strftime('%B')))

        for year, yearly_data in total_stats.items():
            total_stats[year] = None
            monthly_data = {}
            for month in yearly_data:
                if month in monthly_data:
                    monthly_data[month] += 1
                else:
                    monthly_data[month] = 1
            total_stats[year] = monthly_data
        return total_stats

class UserStatistics():
    def __init__(self):
        self._all_posts = None
        self._username = None

    def set_posts(self, all_posts):
        self._all_posts = all_posts

    def set_name(self, username):
        self._username = username

    def total_stats(self):
        total_stats = {}

        for post in self._all_posts:
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

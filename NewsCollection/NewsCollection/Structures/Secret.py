class Secret:
    __secret = {
        'host': 'localhost',
        'port': '3306',
        'user': 'username',
        'password': 'password',
    }

    def __str__(self):
        s = 'mysql+pymysql://{}:{}@{}:{}/'.format(
            self.__secret['user'],
            self.__secret['password'],
            self.__secret['host'],
            self.__secret['port'],
        )
        return s

    def ods_db(self):
        return '%sods_news_db' % self

    def dwd_db(self):
        return '%sdwd_news_db' % self

    def ads_db(self):
        return '%sads_news_db' % self



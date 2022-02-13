import yaml


class Secret:
    with open('./secret.yaml', 'r') as f:
        secret = yaml.load(f, Loader=yaml.FullLoader)
    __secret = {
        'host': secret['mysql']['host'],
        'port': secret['mysql']['port'],
        'user': secret['mysql']['user'],
        'password': secret['mysql']['password']
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

a = Secret().ods_db()
print(a)
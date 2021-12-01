from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

#######################################################
# when create a new table, inside the table class should not have metadata
# from sqlalchemy import create_engine
# #
# from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Eastmoney(Base):
    # Define table name and meta
    __tablename__ = 'ods_news_eastmoney'
    # metadata = MetaData()

    # Define columns in table
    newsid = Column(String(50), primary_key=True, comment='distinct eastmoney news id')
    showtime = Column(String(50), comment='news first show time')
    title = Column(String(500), comment='news headlines')
    digest = Column(String(2048), comment='news brief content')
    content = Column(String(12000), comment='news body')
    url_unique = Column(String(200), comment='news body url')
    editor_name = Column(String(10), comment='editor name')
    newstype = Column(String(5), comment='news type 1:normal, 3: highlighted')
    commentnum = Column(String(5), comment='news comment count')
    topic = Column(String(100), comment='news topic. usually None')


class Snowball(Base):
    # Define table name and meta
    __tablename__ = 'ods_news_snowball'
    # metadata = MetaData()

    # Define columns in table
    snowball_id = Column(String(20), primary_key=True, comment='distinct snowball news id')
    text = Column(String(3000), comment='news body')
    mark = Column(String(5), comment='news level')
    target = Column(String(150), comment='news url')
    created_at = Column(String(50), comment='news showtime')
    view_count = Column(String(10), comment='news detail page visit count')
    status_id = Column(String(15), comment='Not sure what it is')
    reply_count = Column(String(5), comment='news reply count')
    share_count = Column(String(5), comment='news share count')


class Jiemian(Base):
    # Define table name and meta
    __tablename__ = 'ods_news_jiemian'
    # metadata = MetaData()

    # Define columns in table
    date_time = Column(String(50), comment='news showtime')
    news_id = Column(String(50), primary_key=True, comment='distinct jiemian news id')
    title = Column(String(3000), comment='news title')
    content_url = Column(String(150), comment='news url')

# from Secret import Secret
# a = Secret().ods_db()
# engine = create_engine(a, echo=True, future=True)
#
#
# Base.metadata.create_all(engine)

#
# #

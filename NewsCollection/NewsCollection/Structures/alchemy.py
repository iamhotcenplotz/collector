from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from NewsCollection.Structures.Secret import Secret


def engine(level):
    if level == 'ods':
        s = Secret().ods_db()
    elif level == 'dwd':
        s = Secret().dwd_db()
    elif level == 'ads':
        s = Secret().ads_db()
    else:
        raise NameError('Database Does Not Exist')

    e = create_engine(s, echo=True, future=True)
    Session = sessionmaker(bind=e)
    session = Session()
    return session



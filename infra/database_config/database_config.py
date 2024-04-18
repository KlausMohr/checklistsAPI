from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL
from sqlalchemy import create_engine

Base = declarative_base()

class DBConnection:

    def __init__(self) -> None:
        self.__conection_string = URL.create(
            "postgresql+psycopg2",
            username="postgres",
            password="@dmin1234",
            host="127.0.0.1",
            database="checklist_app",
        )
        self.__engine = self.__create_db_engine()
        self.session = None

    def __create_db_engine(self):
        engine = create_engine(self.__conection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

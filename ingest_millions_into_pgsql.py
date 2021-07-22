#!/usr/bin/python3

"""ingest millions of rows in a table."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError  # base exception class

from models.employee import Base, Employee
from names import get_first_name

N = 1000000  # million


class IngestDataInDB:
    """ingest millions of rows in a table."""

    def __init__(self, user, password, host, database):

        self.setup_postgres(user, password, host, database)
        # create employee table in database
        Base.metadata.create_all(self.postgres_engine)

    def setup_postgres(self, user, password, host, database):
        """Generates a connection to the Postgres database"""

        self.postgres_engine = create_engine(
            "postgresql://{user}:{password}@{host}/{database}".format(
                user=user,
                password=password,
                host=host,
                database=database,
            ),
            echo=False,
        )

    def get_postgres_session(self):
        """return sql session."""

        session = sessionmaker(bind=self.postgres_engine)
        return session()

    @staticmethod
    def build_model(item):
        """build Employee DB Model"""

        return Employee(
            name=item.get("name"),
        )

    def build_model_and_write_to_db(self):
        """build model and write to databse table"""

        # get db session
        sql_session = self.get_postgres_session()

        # generate bulk employee names list
        employee_list = []
        for _ in range(N):
            employee_list.append(self.build_model({"name": get_first_name()}))

        try:
            sql_session.bulk_save_objects(employee_list)
            sql_session.commit()
            print("Successfully added employee record into database!!!")
        except SQLAlchemyError as err:
            print("Unable to add new user session to db. Database error: {}".format(err))
            sql_session.rollback()
        finally:
            # Close postgres session
            sql_session.close()


if __name__ == '__main__':
    db_ingest_obj = IngestDataInDB(
        user="my_user",
        password="password123",
        host="localhost",
        database="my_database",
    )
    db_ingest_obj.build_model_and_write_to_db()

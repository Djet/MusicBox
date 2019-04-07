from playhouse.postgres_ext import *

user = 'postgres'
password = 'Pasd@1234'
db_name = 'musicbox'

db = PostgresqlDatabase(
    db_name, user=user,
    password=password,
    host='localhost'
)


class musicbox(Model):
    publish_in = DateField()
    published_in = DateField()
    publish_data = JSONField()
    class Meta:
        database = db  # This model uses the "people.db" database.

musicbox.create_table(True)


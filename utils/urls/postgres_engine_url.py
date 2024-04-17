from sqlalchemy.engine import URL


url_object = URL.create(
    "postgresql+psycopg2",
    username="postgres",
    password="@dmin1234",
    host="127.0.0.1",
    database="checklist_app"
    
)
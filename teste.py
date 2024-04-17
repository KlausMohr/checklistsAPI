from infra.database.idatabase_config import IDBConfig
from sqlalchemy import create_engine
from utils.urls.postgres_engine_url import url_object



engine = create_engine(url_object)
conn = engine.connect()
response = conn.exec_driver_sql("SELECT * FROM checklist_app.tb_owner;")
        
for row in response:
    print(row)
    print(row.name)
    
    #connect_args={'options': '-csearch_path={}'.format()}
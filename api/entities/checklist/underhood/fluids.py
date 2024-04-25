from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.utils.database.database import db

class Fluids(db.Model):
    __tablename__ = "tb_fluids"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)

    created_at = db.Column(TIMESTAMP(timezone=True),
                           nullable=False, server_default=text("now()"))

    def __repr__(self):
        return f""""""
    
    def to_json(self):
        return{
            
        }
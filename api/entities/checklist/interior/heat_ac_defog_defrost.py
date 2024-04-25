from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from api.utils.database.database import db


class HeatACDefogDefrost(db.Model):
    __tablename__ = "tb_heat_ac_defog_defrost"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    ac_system = db.Column(db.SmallInteger(), nullable=False)
    heating_system = db.Column(db.SmallInteger(), nullable=False)
    defog_defrost = db.Column(db.SmallInteger(), nullable=False)
    create_at = db.Column(TIMESTAMP(timezone=True),
                          nullable=False, server_default=text("now()"))

    def __repr__(self):
        return f"""Head, AC, Defog and Defrost [id={self.id},
                                                ac_system={self.ac_system},
                                                heating_system={self.heating_system},
                                                defog_defrog={self.defog_defrost}]"""

    def to_json(self):
        return {
            "id": self.id,
            "ac_system": self.ac_system,
            "heating_system": self.heating_system,
            "defog_defrost": self.defog_defrost
        }

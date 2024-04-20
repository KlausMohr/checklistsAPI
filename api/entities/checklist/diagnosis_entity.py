from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.utils.database.database import db


class Diagnosis(db.Model):
    __tablename__ = "tb_diagnostic"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    module_system_test = db.Column(db.SmallInteger(), nullable=False)
    created_at = db.Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )

    def __repr__(self):
        return f"Diagnosis [id={self.id}, module_system_test={self.module_system_test}]"

    def to_json(self):
        return {
            "id": self.id,
            "module_system_test": self.module_system_test
        }

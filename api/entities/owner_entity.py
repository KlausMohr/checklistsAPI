from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from api.utils.database.database import db


class Owner(db.Model):
    __tablename__ = "tb_owner"

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    name = db.Column(db.String(), nullable=False)
    cpf = db.Column(db.String())
    birthday = db.Column(db.String())
    telephone = db.Column(db.String())
    email = db.Column(db.String())
    address = db.Column(db.String())
    created_at = db.Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )

    __table_args__ = {"schema": "checklist_app"}

    def __repr__(self):
        return f"Owner [name={self.name}, cpf={self.cpf}, birthday={self.birthday}, telephone={self.telephone}, email={self.email}, address={self.address}]"

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "cpf": self.cpf,
            "birthday": self.birthday,
            "telephone": self.telephone,
            "email": self.email,
            "address": self.address,
        }

from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from api.entities.address_entity import Address
from api.utils.aplication.config import db


class Owner(db.Model):
    __tablename__ = "tb_owner"

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    name = db.Column(db.String(), nullable=False)
    cpf = db.Column(db.String())
    birthday = db.Column(db.String())
    telephone = db.Column(db.String())
    email = db.Column(db.String())
    address_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_address.id", ondelete="CASCADE"))
    created_at = db.Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    
    address = db.relationship(Address)

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

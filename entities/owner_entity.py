from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from dataclasses import dataclass
from infra.database_config.database_config import Base


@dataclass
class Owner(Base):
    __tablename__ = "tb_owner"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)
    cpf = Column(String)
    birthday = Column(String)
    telephone = Column(String)
    email = Column(String)
    address = Column(String)
    created_at = Column(
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

from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from api.utils.aplication.config import db

class Address(db.Model):
    __tablename__ = "tb_address"
    __table_args__ = {"schema": "checklist_app"}
    
    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    cep = db.Column(db.Integer(), nullable=False)
    logradouro = db.Column(db.String(), nullable=False)
    complemento = db.Column(db.String(), nullable=True)
    bairro = db.Column(db.String(), nullable=False)
    localidade = db.Column(db.String(), nullable=False)
    uf = db.Column(db.String(), nullable=False)
    country = db.Column(db.String())
    
    def __repr__(self):
        return f"Address [cep={self.cep}, logradouro={self.logradouro}, complemento={self.complemento}, bairro={self.bairro}, localidade={self.localidade}, uf={self.uf}, country={self.country}]"

    def to_json(self):
        return {
            "cep": self.cep,
            "logradouro": self.logradouro,
            "complemento": self.complemento,
            "bairro": self.bairro,
            "localidade": self.localidade,
            "uf": self.uf,
            "country": self.country,
        }
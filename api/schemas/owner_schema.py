from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from api.utils.aplication.config import Marshmallow as ma
from api.entities.owner_entity import Owner


class OwnerSchema(SQLAlchemyAutoSchema):
    model = Owner
    load_instance=True
    
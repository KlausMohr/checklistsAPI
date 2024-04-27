from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.utils.aplication.config import db


class Fluids(db.Model):
    __tablename__ = "tb_fluids"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    engine_oil_filter = db.Column(db.SmallInteger(), nullable=False)
    engine_oil = db.Column(db.SmallInteger(), nullable=False)
    coolant = db.Column(db.SmallInteger(), nullable=False)
    brake_fluid = db.Column(db.SmallInteger(), nullable=False)
    automatic_transmission_fluid = db.Column(db.SmallInteger(), nullable=False)
    transfercase_fluid = db.Column(db.SmallInteger(), nullable=False)
    driveaxle_fluid = db.Column(db.SmallInteger(), nullable=False)
    powersteering_fluid = db.Column(db.SmallInteger(), nullable=False)
    manual_transmission_fluid = db.Column(db.SmallInteger(), nullable=False)
    hydraulic_clutch_fluid = db.Column(db.SmallInteger(), nullable=False)
    washer_fluid = db.Column(db.SmallInteger(), nullable=False)
    created_at = db.Column(TIMESTAMP(timezone=True),
                           nullable=False, server_default=text("now()"))

    def __repr__(self):
        return f"""Fluids [id={self.id},
                           engine_oil_filter={self.engine_oil_filter},
                           engine_oil={self.engine_oil},
                           coolant={self.coolant},
                           brake_fluid={self.brake_fluid},
                           automatic_transmission_fluid={self.automatic_transmission_fluid},
                           transfercase_fluid={self.transfercase_fluid},
                           driveaxle_fluid={self.driveaxle_fluid},
                           powersteering_fluid={self.powersteering_fluid},
                           manual_transmission_fluid={self.manual_transmission_fluid},
                           washer_fluid={self.washer_fluid}]"""

    def to_json(self):
        return {
            "id": self.id,
            "engine_oil_filter": self.engine_oil_filter,
            "engine_oil": self.engine_oil,
            "coolant": self.coolant,
            "brake_fluid": self.brake_fluid,
            "automatico_transmission_fluid": self.automatic_transmission_fluid,
            "transfercase_fluid": self.transfercase_fluid,
            "driveaxle_fluid": self.driveaxle_fluid,
            "powersteering_fluid": self.powersteering_fluid,
            "manual_transmission_fluid": self.manual_transmission_fluid,
            "hydraulic_clutch_fluid": self.hydraulic_clutch_fluid,
            "washer_fluid": self.washer_fluid

        }

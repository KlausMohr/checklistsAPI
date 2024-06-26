from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.utils.aplication.config import db

from api.entities.checklist.underbody.frame import Frame
from api.entities.checklist.underbody.exhaust import Exhaust
from api.entities.checklist.underbody.trans_differential_transfer import TransDiffTransfer
from api.entities.checklist.underbody.tires_wheels import TiresWheels
from api.entities.checklist.underbody.brake import Brake


class Underbody(db.Model):
    __tablename__ = "tb_underbody"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    frame_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_frame.id", ondelete="CASCADE"))
    exhaust_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_exhaust.id", ondelete="CASCADE"))
    trans_diff_transfer_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_transmission_differential.id", ondelete="CASCADE"))
    tires_wheels_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_tires_wheels.id", ondelete="CASCADE"))
    brake_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_brake.id", ondelete="CASCADE"))

    created_at = db.Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )

    frame = db.relationship(Frame)
    exhaust = db.relationship(Exhaust)
    trans_diff_transfer = db.relationship(TransDiffTransfer)
    tires_wheels = db.relationship(TiresWheels)
    brake = db.relationship(Brake)

    def __repr__(self):
        return f"""Underbody [id = {self.id},
                                 frame_id = {self.frame_id},
                                 exhaust_id= {self.exhaust_id},
                                 trans_diff_transfer_id= {self.trans_diff_transfer_id},
                                 tires_wheels_id= {self.tires_wheels_id},
                                 brake_id= {self.brake_id}]"""

    def to_json(self):
        return {
            "id": self.id,
            "frame_id": self.frame_id,
            "exhaust_id": self.exhaust_id,
            "trans_diff_transfer_id": self.trans_diff_transfer_id,
            "tires_wheels_id": self.tires_wheels_id,
            "brake_id": self.brake_id
        }

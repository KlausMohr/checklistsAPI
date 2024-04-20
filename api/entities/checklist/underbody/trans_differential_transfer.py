"""Transmission, Transaxle, Differential and Transfer Case Entity"""

from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from api.utils.database.database import db


class TransDiffTransfer(db.Model):
    __tablename__ = "tb_transmission_differential"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    automatic_transmission = db.Column(db.SmallInteger(), nullable=False)
    manual_transmission = db.Column(db.SmallInteger(), nullable=False)
    four_by_four_operation = db.Column(db.SmallInteger(), nullable=False)
    universal_cv_joints_boots = db.Column(db.SmallInteger(), nullable=False)
    transmission_mounts = db.Column(db.SmallInteger(), nullable=False)
    differential_drive_axle = db.Column(db.SmallInteger(), nullable=False)

    def __repr__(self):
        return f"Transmission related [id= {self.id},
                                       automatic_transmission = {self.automatic_transmission},
                                       manual_transmission= {self.manual_transmission},
                                       four_by_four_operation= {self.four_by_four_operation},
                                       universal_cv_joints_boots= {self.universal_cv_joints_boots},
                                       tranmission_mounts= {self.transmission_mounts},
                                       differential_drive_axle = {self.differential_drive_axle}]"

    def to_json(self):
        return {
            "id": self.id,
            "automatic_transmission": self.automatic_transmission,
            "manual_transmission": self.manual_transmission,
            "four_by_four_operation": self.four_by_four_operation,
            "universal_cv_joints_boots": self.universal_cv_joints_boots,
            "transmission_mounts": self.transmission_mounts,
            "differential_drive_axle": self.differential_drive_axle
        }

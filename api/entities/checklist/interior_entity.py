from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.utils.database.database import db
from api.entities.checklist.interior.airbag_safety_belts import AirbagSafetyBelts
from api.entities.checklist.interior.audio_alarm import AudioAlarm
from api.entities.checklist.interior.heat_ac_defog_defrost import HeatACDefogDefrost
from api.entities.checklist.interior.interior_amenities import InteriorAmenities
from api.entities.checklist.interior.carpet_trim_mats import CarpetTrimMats
from api.entities.checklist.interior.seats import Seats
from api.entities.checklist.interior.sunroof_convertible_top import SunroofConvertibleTop
from api.entities.checklist.interior.windows_doors_locks import WindowsDoorsLocks
from api.entities.checklist.interior.luggage_compartment import LuggageCompartment


class Interior(db.Model):
    __tablename__ = "tb_interior"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    airbag_safety_belts_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_airbag_safety_belts.id", ondelete="CASCADE"))
    audio_alarm_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_audio_alarm.id", ondelete="CASCADE"))
    heat_ac_defog_defrost_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_heat_ac_defog_defrost.id", ondelete="CASCADE"))
    interior_amenities_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_interior_amenities.id", ondelete="CASCADE"))
    carpet_trims_mats_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_carpet_trim_mats.id", ondelete="CASCADE"))
    seats_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_seats.id", ondelete="CASCADE"))
    sunroof_convertible_top_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_sunroof_convertible_top.id", ondelete="CASCADE"))
    windows_doors_locks_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_windows_doors_locks.id", ondelete="CASCADE"))
    luggage_compartment_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.luggage_compartment.id", ondelete="CASCADE"))
    create_at = db.Column(TIMESTAMP(timezone=True),
                          nullable=False, server_default=text("now()"))

    airbag_safety_belts_id = db.relationship(AirbagSafetyBelts)
    audio_alarm_id = db.relationship(AudioAlarm)
    heat_ac_defog_defrost_id = db.relationship(HeatACDefogDefrost)
    interior_amenities_id = db.relationship(InteriorAmenities)
    carpet_trims_mats_id = db.relationship(CarpetTrimMats)
    seats_id = db.relationship(Seats)
    sunroof_convertible_top_id = db.relationship(SunroofConvertibleTop)
    windws_doors_locks_id = db.relationship(WindowsDoorsLocks)
    luggage_compartment_id = db.relationship(LuggageCompartment)

    def __repr__(self):
        return f"""Interior [id= {self.id},
                           airbag_safety_belts_id= {self.airbag_safety_belts_id},
                           audio_alarm_id= {self.audio_alarm_id},
                           heat_ac_defog_defrost_id= {self.heat_ac_defog_defrost_id},
                           interior_amenities_id= {self.interior_amenities_id},
                           carpet_trims_mats_id = {self.carpet_trims_mats_id},
                           seats_id = {self.seats_id},
                           sunroof_convertible_top_id = {self.sunroof_convertible_top_id},
                           windws_doors_locks_id = {self.windws_doors_locks_id},
                           luggage_compartment_id = {self.luggage_compartment_id}]"""

    def to_json(self):
        return {
            "id": self.id,
            "airbag_safety_belts_id": self.airbag_safety_belts_id,
            "audio_alarm_id": self.audio_alarm_id,
            "heat_ac_defog_defrost_id": self.heat_ac_defog_defrost_id,
            "interior_amenities_id": self.interior_amenities_id,
            "carpet_trims_mats_id": self.carpet_trims_mats_id,
            "seats_id": self.seats_id,
            "sunroof_convertible_top_id": self.sunroof_convertible_top_id,
            "windws_doors_locks_id": self.windws_doors_locks_id,
            "luggage_compartment_id": self.luggage_compartment_id,

        }

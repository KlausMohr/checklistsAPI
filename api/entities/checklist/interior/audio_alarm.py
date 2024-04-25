from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from api.utils.database.database import db


class AudioAlarm(db.Model):
    __tablename__ = "tb_audio_alarm"
    __table_args__ = {"schema": "cheklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    radio_cd_speaker = db.Column(db.SmallInteger(), nullable=False)
    antenna = db.Column(db.SmallInteger(), nullable=False)
    alarm_system = db.Column(db.SmallInteger(), nullable=False)
    navigation_system = db.Column(db.SmallInteger(), nullable=False)
    created_at = db.Column(TIMESTAMP(timezone=True),
                           nullable=False, server_default=text("now()"))

    def __repr__(self):
        return f"""Audio and Alarm [id={self.id},
                    radio_cd_speaker={self.radio_cd_speaker},
                    antenna={self.antenna},
                    alarm_system={self.alarm_system},
                    navigation_system={self.navigation_system}]"""

    def to_json(self):
        return {
            "id": self.id,
            "radio_cd_speaker": self.radio_cd_speaker,
            "antenna": self.antenna,
            "alarm_system": self.alarm_system,
            "navigation_system": self.navigation_system
        }

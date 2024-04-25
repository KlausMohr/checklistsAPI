from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from api.utils.database.database import db


class WindowsDoorsLocks(db.Model):
    __tablename__ = "tb_windows_doors_locks"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    door_handles_release = db.Column(db.SmallInteger(), nullable=False)
    remote_entry = db.Column(db.SmallInteger(), nullable=False)
    push_button_start = db.Column(db.SmallInteger(), nullable=False)
    door_locks = db.Column(db.SmallInteger(), nullable=False)
    child_safety_locks = db.Column(db.SmallInteger(), nullable=False)
    window_controls = db.Column(db.SmallInteger(), nullable=False)
    remote_decklid_release = db.Column(db.SmallInteger(), nullable=False)
    fuel_filler_door_release = db.Column(db.SmallInteger(), nullable=False)
    created_at = db.Column(TIMESTAMP(timezone=True),
                           nullable=False, server_default=text("now()"))

    def __repr__(self):
        return f"""Windows and Doors Locks [id={self.id},
                                            door_handles_release={self.door_handles_release},
                                            remote_entry={self.remote_entry},
                                            push_button_start={self.push_button_start},
                                            door_locks={self.door_locks},
                                            child_safety_locks={self.child_safety_locks},
                                            window_controls={self.window_controls},
                                            remote_decklid_release={self.remote_decklid_release},
                                            fuel_filler_door_release={self.fuel_filler_door_release}]"""

    def to_json(self):
        return {
            "id": self.id,
            "door_handles_release": self.door_handles_release,
            "remote_entry": self.remote_entry,
            "push_button_start": self.push_button_start,
            "door_locks": self.door_locks,
            "child_safety_locks": self.child_safety_locks,
            "window_controls": self.window_controls,
            "remote_decklid_release": self.remote_decklid_release,
            "fuel_filler_door_release": self.fuel_filler_door_release
        }

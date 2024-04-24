from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from api.utils.database.database import db


class InteriorAmenities(db.Model):
    __tablename__ = "tb_interior_amenities"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    clock = db.Column(db.Integer(), nullable=False)
    tilt_telescopic_steering_wheel = db.Column(db.Integer(), nullable=False)
    steering_column_lock = db.Column(db.Integer(), nullable=False)
    horn = db.Column(db.Integer(), nullable=False)
    warning_chimes = db.Column(db.Integer(), nullable=False)
    instrument_panel = db.Column(db.Integer(), nullable=False)
    windshield_wipers = db.Column(db.Integer(), nullable=False)
    rear_window_wiper = db.Column(db.Integer(), nullable=False)
    interior_light_courtesy = db.Column(db.Integer(), nullable=False)
    rear_view_mirror = db.Column(db.Integer(), nullable=False)
    active_park_assist = db.Column(db.Integer(), nullable=False)
    rear_entertainment_system = db.Column(db.Integer(), nullable=False)
    power_outlets = db.Column(db.Integer(), nullable=False)
    lighter = db.Column(db.Integer(), nullable=False)
    glove_box = db.Column(db.Integer(), nullable=False)
    center_armrest = db.Column(db.Integer(), nullable=False)
    console = db.Column(db.Integer(), nullable=False)
    sun_visors = db.Column(db.Integer(), nullable=False)
    created_at = db.Columne(TIMESTAMP(timezone=True),
                            nullable=False, server_default=text("now()"))

    def __repr__(self):
        return f"""Interior Amenities [id={self.id},
                                       clocl={self.clock},
                                       tilt_telescopic_steering_wheel={self.tilt_telescopic_steering_wheel},
                                       steering_column_lock={self.steering_column_lock},
                                       horn={self.horn},
                                       warning_chimes={self.warning_chimes},
                                       instrument_panel={self.instrument_panel},
                                       windshield_wipers={self.windshield_wipers},
                                       rear_window_wiper={self.rear_window_wiper},
                                       active_park_assist={self.active_park_assist},
                                       rear_entertainment_system={self.rear_entertainment_system},
                                       power_outlets={self.power_outlets},
                                       lighter={self.lighter},
                                       glove_box={self.glove_box},
                                       center_armrest={self.center_armrest},
                                       console={self.console},
                                       sun_visors={self.sun_visors},
                                       ]"""

    def to_json(self):
        return {
            "id": self.id,
            "clock": self.clock,
            "tilt_telescopic_steering_wheel": self.tilt_telescopic_steering_wheel,
            "steering_column_lock": self.steering_column_lock,
            "horn": self.horn,
            "warning_chimes": self.warning_chimes,
            "instrument_panel": self.instrument_panel,
            "windshield_wipers": self.windshield_wipers,
            "rear_window_wiper": self.rear_window_wiper,
            "active_park_assist": self.active_park_assist,
            "rear_entertainment_system": self.rear_entertainment_system,
            "power_outlets": self.power_outlets,
            "lighter": self.lighter,
            "glove_box": self.glove_box,
            "center_armrest": self.center_armrest,
            "console": self.console,
            "sun_visors": self.sun_visors
        }

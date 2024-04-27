from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.utils.aplication.config import db


class RoadTest(db.Model):
    __tablename__ = "tb_roadtest"

    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    engine_starting = db.Column(db.SmallInteger(), nullable=False)
    engine_idling = db.Column(db.SmallInteger(), nullable=False)
    remote_start = db.Column(db.SmallInteger(), nullable=False)
    engine_acceleration = db.Column(db.SmallInteger(), nullable=False)
    engine_noise = db.Column(db.SmallInteger(), nullable=False)
    auto_manual_transmission_shifting = db.Column(
        db.SmallInteger(), nullable=False)
    auto_manual_transmission_noise = db.Column(
        db.SmallInteger(), nullable=False)
    shift_interlock_operation = db.Column(db.SmallInteger(), nullable=False)
    drive_axle_transer_case_operation = db.Column(
        db.SmallInteger(), nullable=False)
    clutch_operation = db.Column(db.SmallInteger(), nullable=False)
    steering_basic_operation = db.Column(db.SmallInteger(), nullable=False)
    body_suspension_squeaks = db.Column(db.SmallInteger(), nullable=False)
    struts_schocks_operation = db.Column(db.SmallInteger(), nullable=False)
    brakes_abs_operation = db.Column(db.SmallInteger(), nullable=False)
    cruise_control = db.Column(db.SmallInteger(), nullable=False)
    gauges_operation = db.Column(db.SmallInteger(), nullable=False)
    driver_select_memory = db.Column(db.SmallInteger(), nullable=False)
    no_abnormal_wind_noise = db.Column(db.SmallInteger(), nullable=False)
    created_at = db.Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )

    def __repr__(self):
        return f"""Road Test [id= {self.id},
                            engine_starting= {self.engine_starting},
                            engine_idling= {self.engine_idling},
                            remote_start= {self.remote_start},
                            engine_acceleration= {self.engine_acceleration},
                            engine_noise= {self.engine_noise},
                            auto_manual_transmission_shifting= {self.auto_manual_transmission_shifting},
                            auto_manual_transmission_noise= {self.auto_manual_transmission_noise},
                            shift_interlock_operation= {self.shift_interlock_operation},
                            drive_axle_transfer_case_operation= {self.drive_axle_transer_case_operation},
                            clutch_operation= {self.clutch_operation},
                            steering_basic_operation= {self.steering_basic_operation},
                            body_suspension_squeaks= {self.body_suspension_squeaks},
                            struts_shocks_operation= {self.struts_schocks_operation},
                            brakes_abs_operation= {self.brakes_abs_operation},
                            cruise_control= {self.cruise_control},
                            gauges_operation= {self.gauges_operation},
                            driver_select_memory= {self.driver_select_memory},
                            no_abnormal_wind_noise = {self.no_abnormal_wind_noise}]"""

    def to_json(self):
        return {
            "id": self.id,
            "engine_starting": self.engine_starting,
            "engine_idling": self.engine_idling,
            "remote_start": self.remote_start,
            "engine_acceleration": self.engine_acceleration,
            "engine_noise": self.engine_noise,
            "auto_manual_transmission_shifting": self.auto_manual_transmission_shifting,
            "auto_manual_transmission_noise": self.auto_manual_transmission_noise,
            "shift_interlock_operation": self.shift_interlock_operation,
            "drive_axle_transfer_case_operation": self.drive_axle_transer_case_operation,
            "clutch_operation": self.clutch_operation,
            "steering_basic_operation": self.steering_basic_operation,
            "body_suspension_squeaks": self.body_suspension_squeaks,
            "struts_shocks_operation": self.struts_schocks_operation,
            "brakes_abs_operation": self.brakes_abs_operation,
            "cruise_control": self.cruise_control,
            "gauges_operation": self.gauges_operation,
            "driver_select_memory": self.driver_select_memory,
            "no_abnormal_wind_noise": self.no_abnormal_wind_noise
        }

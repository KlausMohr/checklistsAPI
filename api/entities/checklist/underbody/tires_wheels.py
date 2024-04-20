from api.utils.database.database import db


class TiresWheels(db.Model):
    __tablename__ = "tb_tires_wheels"
    _table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    tires_match_size = db.Column(db.SmallInteger, nullable=False)
    wheels_match_size = db.Column(db.SmallInteger, nullable=False)
    twi_front_lr = db.Column(db.SmallInteger, nullable=False)
    twi_rear_lr = db.Column(db.SmallInteger, nullable=False)
    tire_pressure_front = db.Column(db.SmallInteger, nullable=False)
    tire_pressure_rear = db.Column(db.SmallInteger, nullable=False)
    tire_pressure_system = db.Column(db.SmallInteger, nullable=False)
    wheels = db.Column(db.SmallInteger, nullable=False)
    wheels_covers = db.Column(db.SmallInteger, nullable=False)
    rack_pinion_linkage = db.Column(db.SmallInteger, nullable=False)
    control_arms_bush = db.Column(db.SmallInteger, nullable=False)
    tie_rods_idler_arm = db.Column(db.SmallInteger, nullable=False)
    springs = db.Column(db.SmallInteger, nullable=False)
    struts_shocks = db.Column(db.SmallInteger, nullable=False)
    wheel_alignment = db.Column(db.SmallInteger, nullable=False)
    power_steering_pump = db.Column(db.SmallInteger, nullable=False)

    def __repr__(self):
        return f"Tires and Wheels [id = {self.id},
                                   tires_match_size = {self.tires_match_size},
                                   wheels_match_size= {self.wheels_match_size},
                                   twi_front_lr= {self.twi_front_lr},
                                   twi_rear_lr= {self.twi_rear_lr},
                                   tire_pressure_front= {self.tire_pressure_front},
                                   tire_pressure_rear= {self.tire_pressure_rear},
                                   tire_pressure_system= {self.tire_pressure_system},
                                   wheels= {self.wheels},
                                   wheels_covers= {self.wheels_covers},
                                   rack_pinion_linkage= {self.rack_pinion_linkage},
                                   control_arms_bush= {self.control_arms_bush},
                                   tie_rods_idler_arm= {self.tie_rods_idler_arm},
                                   springs= {self.springs},
                                   struts_shocks= {self.struts_shocks},
                                   wheel_alignment= {self.wheel_alignment},
                                   power_steering_pump = {self.power_steering_pump}]"

    def to_json(self):
        return {
            "id": self.id,
            "tires_match_size": self.tires_match_size,
            "wheels_match_size": self.wheels_match_size,
            "twi_front_lr": self.twi_front_lr,
            "twi_rear_lr": self.twi_rear_lr,
            "tire_pressure_front": self.tire_pressure_front,
            "tire_pressure_rear": self.tire_pressure_rear,
            "tire_pressure_system": self.tire_pressure_system,
            "wheels": self.wheels,
            "wheels_covers": self.wheels_covers,
            "rack_pinion_linkage": self.rack_pinion_linkage,
            "control_arms_bush": self.control_arms_bush,
            "tie_rods_idler_arm": self.tie_rods_idler_arm,
            "springs": self.springs,
            "struts_shocks": self.struts_shocks,
            "wheel_alignment": self.wheel_alignment,
            "power_steering_pump": self.power_steering_pump
        }

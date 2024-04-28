from flask import request
from api.entities.checklist.underbody.tires_wheels import TiresWheels
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class TiresWheelsRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = (
                db.session.query()
                .with_entities(TiresWheels)
                .filter(TiresWheels.id == id)
            )
            try:
                if data:
                    for tires_wheels in data:
                        response = {"tires_wheels": tires_wheels.to_json()}
                return response_gen(200, "Tires and Wheels", response)
            except Exception as excepetion:
                print(excepetion)
                return response_gen(204, "No content for Tires and Wheels", response)

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = db.session.query(TiresWheels).filter(TiresWheels.id == id).first()

            body = request.get_json()

            try:
                tires_wheels = TiresWheels(
                    tires_match_size=body["tires_match_size"],
                    wheels_match_size=body["wheels_match_size"],
                    twi_front_lr=body["twi_front_lr"],
                    twi_rear_lr=body["twi_rear_lr"],
                    tire_pressure_front=body["tire_pressure_front"],
                    tire_pressure_rear=body["tire_pressure_rear"],
                    tire_pressure_system=body["tire_pressure_system"],
                    wheels=body["wheels"],
                    wheels_covers=body["wheels_covers"],
                    rack_pinion_linkage=body["rack_pinion_linkage"],
                    control_arms_bush=body["control_arms_bush"],
                    tie_rods_idler_arm=body["tie_rods_idler_arm"],
                    springs=body["springs"],
                    struts_shocks=body["struts_shocks"],
                    wheel_alignment=body["wheel_alignment"],
                    power_steering_pump=body["power_steering_pump"],
                )

                data.tires_match_size = tires_wheels.tires_match_size
                data.wheels_match_size = tires_wheels.wheels_match_size
                data.twi_front_lr = tires_wheels.twi_front_lr
                data.twi_rear_lr = tires_wheels.twi_rear_lr
                data.tire_pressure_front = tires_wheels.tire_pressure_front
                data.tire_pressure_rear = tires_wheels.twi_front_lr
                data.tire_pressure_system = tires_wheels.tire_pressure_system
                data.wheels = tires_wheels.wheels
                data.wheels_covers = tires_wheels.wheels_covers
                data.rack_pinion_linkage = tires_wheels.rack_pinion_linkage
                data.control_arms_bush = tires_wheels.control_arms_bush
                data.tie_rods_idler_arm = tires_wheels.tie_rods_idler_arm
                data.springs = tires_wheels.springs
                data.struts_shocks = tires_wheels.struts_shocks
                data.wheel_alignment = tires_wheels.wheel_alignment
                data.power_steering_pump = tires_wheels.power_steering_pump

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Tires and Wheels",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )

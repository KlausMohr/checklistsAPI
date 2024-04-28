from flask import request
from api.entities.checklist.underbody.brake import Brake
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class BrakeRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = db.session.query().with_entities(Brake).filter(Brake.id == id)
            try:
                if data:
                    for brake in data:
                        response = {"brake": brake.to_json()}
                return response_gen(200, "Brake", response)
            except Exception as excepetion:
                print(excepetion)
                return response_gen(204, "No content for Brake", response)

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = db.session.query(Brake).filter(Brake.id == id).first()

            body = request.get_json()

            try:
                brake = Brake(
                    calipers_wheels_cylinders=body["calipers_wheels_cylinders"],
                    front_brake_pads_shoes=body["front_brake_pads_shoes"],
                    rear_brake_pads_shoes=body["rear_brake_pads_shoes"],
                    rotor_drums=body["rotor_drums"],
                    brake_lines_hoses_fittings=body["brake_lines_hoses_fittings"],
                    parking_brake=body["parking_brake"],
                    master_cylinder_booster=body["master_cylinder_booster"],
                )

                data.calipers_wheels_cylinders = brake.calipers_wheels_cylinders
                data.front_brake_pads_shoes = brake.front_brake_pads_shoes
                data.rear_brake_pads_shoes = brake.rear_brake_pads_shoes
                data.rotor_drums = brake.rotor_drums
                data.brake_lines_hoses_fittings = brake.brake_lines_hoses_fittings
                data.parking_brake = brake.parking_brake
                data.master_cylinder_booster = brake.master_cylinder_booster

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Brake",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )

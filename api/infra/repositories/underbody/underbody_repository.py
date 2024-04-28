from flask import request
from api.entities.checklist.underbody_entity import Underbody
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class UnderbodyRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = (
                db.session.query().with_entities(Underbody).filter(Underbody.id == id)
            )
            try:
                if data:
                    for underbody in data:
                        response = {"underbody": underbody.to_json()}
                return response_gen(
                    200, "Transmission, Differential and Transfer Case", response
                )
            except Exception as excepetion:
                print(excepetion)
                return response_gen(
                    204,
                    "No content for Transmission, Differential and Transfer Case",
                    response,
                )

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = db.session.query(Underbody).filter(Underbody.id == id).first()

            body = request.get_json()

            try:
                underbody = Underbody(
                    frame_id=body["frame_id"],
                    exhaust_id=body["exhaust_id"],
                    trans_diff_transfer_id=body["trans_diff_transfer_id"],
                    tires_wheels_id=body["tires_wheels_id"],
                    brake_id=body["brake_id"],
                )

                data.frame_id = underbody.frame_id
                data.exhaust_id = underbody.exhaust_id
                data.trans_diff_transfer_id = underbody.trans_diff_transfer_id
                data.tires_wheels_id = underbody.tires_wheels_id
                data.brake_id = underbody.brake_id

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Transmission, Differential and Transfer Case",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )

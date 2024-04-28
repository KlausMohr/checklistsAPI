from flask import request
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from api.entities.checklist.underbody.frame import Frame
from ..irepository import Repository


class FrameRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = db.session.query().with_entities(Frame).filter(Frame.id == id)
            try:
                if data:
                    for frame in data:
                        response = {"frame": frame.to_json()}
                return response_gen(200, "Frame", response)
            except Exception as excepetion:
                print(excepetion)
                return response_gen(204, "No content for Frame", response)

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = db.session.query(Frame).filter(Frame.id == id).first()

            body = request.get_json()

            try:
                frame = Frame(
                    frame_damage=body["frame_damage"],
                    fuel_supply_system=body["fuel_supply_system"],
                )

                data.frame_damage = frame.frame_damage
                data.fuel_supply_system = frame.fuel_supply_system

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Frame",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )

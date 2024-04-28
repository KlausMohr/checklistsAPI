from flask import request
from api.entities.checklist.underhood_entity import Underhood
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class UnderhoodRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = (
                db.session.query().with_entities(Underhood).filter(Underhood.id == id)
            )
            try:
                if data:
                    for underhood in data:
                        response = {"underhood": underhood.to_json()}
                return response_gen(200, "Underhood", response)
            except Exception as excepetion:
                print(excepetion)
                return response_gen(204, "No content for Underhood", response)

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = db.session.query(Underhood).filter(Underhood.id == id).first()

            body = request.get_json()

            try:
                underhood = Underhood(
                    fluids_id=body["fluids_id"],
                    engine_id=body["engine_id"],
                    cooling_system_id=body["cooling_system_id"],
                    fuel_system_id=body["fuel_system_id"],
                    engine_electrical_system_id=body["engine_electrical_system_id"],
                )

                data.fluids_id = underhood.fluids_id
                data.engine_id = underhood.engine_id
                data.cooling_system_id = underhood.cooling_system_id
                data.fuel_system_id = underhood.fuel_system_id
                data.engine_electrical_system_id = underhood.engine_electrical_system_id

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Underhood",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )

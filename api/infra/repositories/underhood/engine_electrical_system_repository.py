from flask import request
from api.entities.checklist.underhood.engine_electrical_system import (
    EngineElectricalSystem,
)
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class EngineElectricalSystemRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = (
                db.session.query()
                .with_entities(EngineElectricalSystem)
                .filter(EngineElectricalSystem.id == id)
            )
            try:
                if data:
                    for engine_electrical_system in data:
                        response = {
                            "engine_electrical_system": engine_electrical_system.to_json()
                        }
                return response_gen(200, "Engine electrical system", response)
            except Exception as excepetion:
                print(excepetion)
                return response_gen(
                    204, "No content for Engine electrical system", response
                )

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = (
                db.session.query(EngineElectricalSystem)
                .filter(EngineElectricalSystem.id == id)
                .first()
            )

            body = request.get_json()

            try:
                engine_electrical_system = EngineElectricalSystem(
                    starter=body["starter"],
                    ignition=body["ignition"],
                    battery=body["battery"],
                    alternator_output=body["alternator_output"],
                    diesel_glow_plug_system=body["diesel_glow_plug_system"],
                )

                data.starter = engine_electrical_system.starter
                data.ignition = engine_electrical_system.ignition
                data.battery = engine_electrical_system.battery
                data.alternator_output = engine_electrical_system.alternator_output
                data.diesel_glow_plug_system = (
                    engine_electrical_system.diesel_glow_plug_system
                )

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Engine electrical system",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )

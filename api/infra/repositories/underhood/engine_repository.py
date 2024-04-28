from flask import request
from api.entities.checklist.underhood.engine import Engine
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class EngineRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = db.session.query().with_entities(Engine).filter(Engine.id == id)
            try:
                if data:
                    for engine in data:
                        response = {"engine": engine.to_json()}
                return response_gen(200, "Engine", response)
            except Exception as excepetion:
                print(excepetion)
                return response_gen(204, "No content for Engine", response)

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = db.session.query(Engine).filter(Engine.id == id).first()

            body = request.get_json()

            try:
                engine = Engine(
                    fluid_leaks=body["fluid_leaks"],
                    hoses_lines=body["hoses_lines"],
                    belts=body["belts"],
                    wiring=body["wiring"],
                    water_coolant_engine_oil=body["water_coolant_engine_oil"],
                    oil_pressure=body["oil_pressure"],
                    cylinder_compression=body["cylinder_compression"],
                    timing_belts=body["timing_belts"],
                    engine_mounts=body["engine_mounts"],
                    turbocharger=body["turbocharger"],
                )

                data.fluid_leaks = engine.fluid_leaks
                data.hoses_lines = engine.hoses_lines
                data.belts = engine.belts
                data.wiring = engine.wiring
                data.water_coolant_engine_oil = engine.water_coolant_engine_oil
                data.oil_pressure = engine.belts
                data.cylinder_compression = engine.cylinder_compression
                data.timing_belts = engine.timing_belts
                data.engine_mounts = engine.engine_mounts
                data.turbocharger = engine.turbocharger

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Engine",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )

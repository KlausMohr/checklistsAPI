from flask import request
from api.entities.checklist.underhood.fuel_system import FuelSystem
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class FuelSystemRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = (
                db.session.query().with_entities(FuelSystem).filter(FuelSystem.id == id)
            )
            try:
                if data:
                    for fuel_system in data:
                        response = {"fuel_system": fuel_system.to_json()}
                return response_gen(200, "Fuel system", response)
            except Exception as excepetion:
                print(excepetion)
                return response_gen(204, "No content for Fuel system", response)

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = db.session.query(FuelSystem).filter(FuelSystem.id == id).first()

            body = request.get_json()

            try:
                fuel_system = FuelSystem(
                    fuel_pump_noise=body["fuel_pump_noise"],
                    fuel_pump_pressure=body["fuel_pump_pressure"],
                    fuel_filter=body["fuel_filter"],
                    engine_air_filter=body["engine_air_filter"],
                )

                data.fuel_pump_noise = fuel_system.fuel_pump_noise
                data.fuel_pump_pressure = fuel_system.fuel_pump_pressure
                data.fuel_filter = fuel_system.fuel_filter
                data.engine_air_filter = fuel_system.engine_air_filter

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Fuel system",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )

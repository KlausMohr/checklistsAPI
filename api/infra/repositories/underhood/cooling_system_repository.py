from flask import request
from api.entities.checklist.underhood.cooling_system import CoolingSystem
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class CoolingSystemRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = (
                db.session.query()
                .with_entities(CoolingSystem)
                .filter(CoolingSystem.id == id)
            )
            try:
                if data:
                    for cooling_system in data:
                        response = {"cooling_system": cooling_system.to_json()}
                return response_gen(200, "Cooling System", response)
            except Exception as excepetion:
                print(excepetion)
                return response_gen(204, "No content for Cooling System", response)

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = (
                db.session.query(CoolingSystem).filter(CoolingSystem.id == id).first()
            )

            body = request.get_json()

            try:
                cooling_system = CoolingSystem(
                    radiator=body["radiator"],
                    pressure_test_radiator_cap=body["pressure_test_radiator_cap"],
                    cooling_fans=body["cooling_fans"],
                    water_pump=body["water_pump"],
                    coolant_recovery_tank=body["coolant_recovery_tank"],
                    cabin_air_filter=body["cabin_air_filter"],
                )

                data.radiator = cooling_system.radiator
                data.pressure_test_radiator_cap = (
                    cooling_system.pressure_test_radiator_cap
                )
                data.cooling_fans = cooling_system.cooling_fans
                data.water_pump = cooling_system.water_pump
                data.coolant_recovery_tank = cooling_system.coolant_recovery_tank
                data.cabin_air_filter = cooling_system.cooling_fans

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Cooling System",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )

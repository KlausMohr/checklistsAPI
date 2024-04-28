from flask import request
from api.entities.checklist.interior.heat_ac_defog_defrost import HeatACDefogDefrost
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class HeatACDefogDefrostRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = (
                db.session.query()
                .with_entities(HeatACDefogDefrost)
                .filter(HeatACDefogDefrost.id == id)
            )
            try:
                if data:
                    for heat_ac_defog_defrost in data:
                        response = {
                            "heat_ac_defog_defrost": heat_ac_defog_defrost.to_json()
                        }
                return response_gen(200, "Head, AC, Defog and Defrost", response)
            except Exception as excepetion:
                print(excepetion)
                return response_gen(
                    204, "No content for Head, AC, Defog and Defrost", response
                )

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = (
                db.session.query(HeatACDefogDefrost)
                .filter(HeatACDefogDefrost.id == id)
                .first()
            )

            body = request.get_json()

            try:
                heat_ac_defog_defrost = HeatACDefogDefrost(
                    ac_system=body["ac_system"],
                    heating_system=body["heating_system"],
                    defog_defrost=body["defog_defrost"],
                )

                data.ac_system = heat_ac_defog_defrost.ac_system
                data.heating_system = heat_ac_defog_defrost.heating_system
                data.defog_defrost = heat_ac_defog_defrost.defog_defrost

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Head, AC, Defog and Defrost",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )

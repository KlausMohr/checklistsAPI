from flask import request
from api.entities.checklist.underhood.fluids import Fluids
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class FluidsRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = db.session.query().with_entities(Fluids).filter(Fluids.id == id)
            try:
                if data:
                    for fluids in data:
                        response = {"fluids": fluids.to_json()}
                return response_gen(200, "Fluids", response)
            except Exception as excepetion:
                print(excepetion)
                return response_gen(204, "No content for Fluids", response)

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = db.session.query(Fluids).filter(Fluids.id == id).first()

            body = request.get_json()

            try:
                fluids = Fluids(
                    engine_oil_filter=body["engine_oil_filter"],
                    engine_oil=body["engine_oil"],
                    coolant=body["coolant"],
                    brake_fluid=body["brake_fluid"],
                    automatic_transmission_fluid=body["automatic_transmission_fluid"],
                    transfercase_fluid=body["transfercase_fluid"],
                    driveaxle_fluid=body["driveaxle_fluid"],
                    powersteering_fluid=body["powersteering_fluid"],
                    manual_transmission_fluid=body["manual_transmission_fluid"],
                    hydraulic_clutch_fluid=body["hydraulic_clutch_fluid"],
                    washer_fluid=body["washer_fluid"],
                )

                data.engine_oil_filter = fluids.engine_oil_filter
                data.engine_oil = fluids.engine_oil
                data.coolant = fluids.coolant
                data.brake_fluid = fluids.brake_fluid
                data.automatic_transmission_fluid = fluids.automatic_transmission_fluid
                data.transfercase_fluid = fluids.coolant
                data.driveaxle_fluid = fluids.driveaxle_fluid
                data.powersteering_fluid = fluids.powersteering_fluid
                data.manual_transmission_fluid = fluids.manual_transmission_fluid
                data.hydraulic_clutch_fluid = fluids.hydraulic_clutch_fluid
                data.washer_fluid = fluids.washer_fluid

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Fluids",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )

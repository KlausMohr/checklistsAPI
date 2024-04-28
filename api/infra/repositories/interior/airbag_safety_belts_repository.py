from flask import request
from api.entities.checklist.interior.airbag_safety_belts import AirbagSafetyBelts
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class AirBagSafetyBeltsRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = (
                db.session.query()
                .with_entities(AirbagSafetyBelts)
                .filter(AirbagSafetyBelts.id == id)
            )
            try:
                if data:
                    for airbag_saf_belts in data:
                        response = {"airbag_safety_belts": airbag_saf_belts.to_json()}
                return response_gen(200, "Airbag and Safety Belts inspection", response)
            except Exception as excepetion:
                print(excepetion)
                return response_gen(
                    204, "No content for Airbag and Safety Belts", response
                )

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = (
                db.session.query(AirbagSafetyBelts)
                .filter(AirbagSafetyBelts.id == id)
                .first()
            )

            body = request.get_json()

            try:
                airbag_saf_belts = AirbagSafetyBelts(
                    airbags=body["airbags"], safety_belts=body["safety_belts"]
                )

                data.airbags = airbag_saf_belts.airbags
                data.safety_belts = airbag_saf_belts.safety_belts

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Airbag and Safety Belts",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )

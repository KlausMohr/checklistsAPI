from flask import request
from api.entities.checklist.underbody.exhaust import Exhaust
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class ExhaustRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = db.session.query().with_entities(Exhaust).filter(Exhaust.id == id)
            try:
                if data:
                    for exhaust in data:
                        response = {"exhaust": exhaust.to_json()}
                return response_gen(200, "Exhaust", response)
            except Exception as excepetion:
                print(excepetion)
                return response_gen(204, "No content for Exhaust", response)

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = db.session.query(Exhaust).filter(Exhaust.id == id).first()

            body = request.get_json()

            try:
                exhaust = Exhaust(
                    exhaust_system_condition=body["exhaust_system_condition"],
                    emissions_control=body["emissions_control"],
                )

                data.exhaust_system_condition = exhaust.exhaust_system_condition
                data.emissions_control = exhaust.emissions_control

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Exhaust",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )

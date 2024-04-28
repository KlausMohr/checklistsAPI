from flask import request
from api.entities.checklist.diagnosis_entity import Diagnosis
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class DiagnosisRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = (
                db.session.query().with_entities(Diagnosis).filter(Diagnosis.id == id)
            )
            try:
                if data:
                    for diagnosis in data:
                        response = {"diagnosis": diagnosis.to_json()}
                return response_gen(200, "Diagnosis", response)
            except Exception as excepetion:
                print(excepetion)
                return response_gen(204, "No content for Diagnosis", response)

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = db.session.query(Diagnosis).filter(Diagnosis.id == id).first()

            body = request.get_json()

            try:
                diagnosis = Diagnosis(module_system_test=body["module_system_test"])

                data.module_system_test = diagnosis.module_system_test

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Diagnosis",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )

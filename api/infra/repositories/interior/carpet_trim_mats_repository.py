from flask import request
from api.entities.checklist.interior.carpet_trim_mats import CarpetTrimMats
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class CarpetTrimMatsRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = (
                db.session.query()
                .with_entities(CarpetTrimMats)
                .filter(CarpetTrimMats.id == id)
            )
            try:
                if data:
                    for carpet_trim_mats in data:
                        response = {"carpet_trim_mats": carpet_trim_mats.to_json()}
                return response_gen(200, "Carpet, Trim and Mats inspection", response)
            except Exception as excepetion:
                print(excepetion)
                return response_gen(
                    204, "No content for Carpet, Trim and Mats", response
                )

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = (
                db.session.query(CarpetTrimMats).filter(CarpetTrimMats.id == id).first()
            )

            body = request.get_json()

            try:
                carpet_trim_mats = CarpetTrimMats(
                    interior_free_odor=body["interior_free_odor"],
                    carpet=body["carpet"],
                    floor_mats=body["floor_mats"],
                    door_trim_panels=body["door_trim_panels"],
                    headliner=body["headliner"],
                )

                data.interior_free_odor = carpet_trim_mats.interior_free_odor
                data.carpet = carpet_trim_mats.carpet
                data.floor_mats = carpet_trim_mats.floor_mats
                data.door_trim_panels = carpet_trim_mats.door_trim_panels
                data.headliner = carpet_trim_mats.headliner

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Carpet, Trim and Mats",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )

from flask import request
from api.entities.checklist.interior.sunroof_convertible_top import (
    SunroofConvertibleTop,
)
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class SunroofConvertibleTopRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = (
                db.session.query()
                .with_entities(SunroofConvertibleTop)
                .filter(SunroofConvertibleTop.id == id)
            )
            try:
                if data:
                    for sunroof_convertible_top in data:
                        response = {
                            "sunroof_convertible_top": sunroof_convertible_top.to_json()
                        }
                return response_gen(200, "Sunroof and Convertible Tops", response)
            except Exception as excepetion:
                print(excepetion)
                return response_gen(
                    204, "No content for Sunroof and Convertible Tops", response
                )

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = (
                db.session.query(SunroofConvertibleTop)
                .filter(SunroofConvertibleTop.id == id)
                .first()
            )

            body = request.get_json()

            try:
                sunroof_convertible_top = SunroofConvertibleTop(
                    sunroof=body["sunroof"], convertible_top=body["convertible_top"]
                )

                data.sunroof = sunroof_convertible_top.sunroof
                data.convertible_top = sunroof_convertible_top.convertible_top

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Sunroof and Convertible Tops",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )

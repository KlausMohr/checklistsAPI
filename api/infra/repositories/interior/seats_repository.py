from flask import request
from api.entities.checklist.interior.seats import Seats
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class SeatsRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = db.session.query().with_entities(Seats).filter(Seats.id == id)
            try:
                if data:
                    for seats in data:
                        response = {"seats": seats.to_json()}
                return response_gen(200, "Seats", response)
            except Exception as excepetion:
                print(excepetion)
                return response_gen(204, "No content for Seats", response)

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = db.session.query(Seats).filter(Seats.id == id).first()

            body = request.get_json()

            try:
                seats = Seats(
                    upholstery=body["upholstery"],
                    seat_head_restraint=body["seat_head_restraint"],
                    folding_seats=body["folding_seats"],
                    heated_seats=body["heated_seats"],
                    cooled_seats=body["cooled_seats"],
                    integrated_child_safety=body["integrated_child_safety"],
                )

                data.upholstery = seats.upholstery
                data.seat_head_restraint = seats.seat_head_restraint
                data.folding_seats = seats.folding_seats
                data.heated_seats = seats.heated_seats
                data.cooled_seats = seats.cooled_seats
                data.integrated_child_safety = seats.folding_seats

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Seats",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )

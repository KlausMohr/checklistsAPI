from flask import request
from api.entities.checklist.interior.interior_amenities import InteriorAmenities
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class InteriorAmenitiesRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = (
                db.session.query()
                .with_entities(InteriorAmenities)
                .filter(InteriorAmenities.id == id)
            )
            try:
                if data:
                    for interior_amenities in data:
                        response = {"interior_amenities": interior_amenities.to_json()}
                return response_gen(200, "Interior amenities", response)
            except Exception as excepetion:
                print(excepetion)
                return response_gen(204, "No content for Interior amenities", response)

    def insert():
        with DBConnection() as db:
            body = request.get_json()
            try:
                if body:

                    interior_amenities = InteriorAmenities(
                        clock=body["clock"],
                        tilt_telescopic_steering_wheel=body[
                            "tilt_telescopic_steering_wheel"
                        ],
                        steering_column_lock=body["steering_column_lock"],
                        horn=body["horn"],
                        warning_chimes=body["warning_chimes"],
                        instrument_panel=body["instrument_panel"],
                        windshield_wipers=body["windshield_wipers"],
                        rear_window_wiper=body["rear_window_wiper"],
                        interior_light_courtesy=body["interior_light_courtesy"],
                        rear_view_mirror=body["rear_view_mirror"],
                        active_park_assist=body["active_park_assist"],
                        rear_entertainment_system=body["rear_entertainment_system"],
                        power_outlets=body["power_outlets"],
                        lighter=body["lighter"],
                        glove_box=body["glove_box"],
                        center_armrest=body["center_armrest"],
                        console=body["console"],
                        sun_visors=body["sun_visors"],
                    )
                    db.session.add(interior_amenities)
                    db.session.commit()
                    return response_gen(
                        200,
                        "Interior amenities",
                        interior_amenities.to_json(),
                        "Interior amenities checklist inspection successfully inserted",
                    )
            except Exception as exception:
                print("Error: ", exception)
                return response_gen(
                    400,
                    "Interior amenities",
                    {},
                    "Error while inserting a new Interior amenities checklist inspection",
                )

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = (
                db.session.query(InteriorAmenities)
                .filter(InteriorAmenities.id == id)
                .first()
            )

            body = request.get_json()

            try:
                interior_amenities = InteriorAmenities(
                    clock=body["clock"],
                    tilt_telescopic_steering_wheel=body[
                        "tilt_telescopic_steering_wheel"
                    ],
                    steering_column_lock=body["steering_column_lock"],
                    horn=body["horn"],
                    warning_chimes=body["warning_chimes"],
                    instrument_panel=body["instrument_panel"],
                    windshield_wipers=body["windshield_wipers"],
                    rear_window_wiper=body["rear_window_wiper"],
                    interior_light_courtesy=body["interior_light_courtesy"],
                    rear_view_mirror=body["rear_view_mirror"],
                    active_park_assist=body["active_park_assist"],
                    rear_entertainment_system=body["rear_entertainment_system"],
                    power_outlets=body["power_outlets"],
                    lighter=body["lighter"],
                    glove_box=body["glove_box"],
                    center_armrest=body["center_armrest"],
                    console=body["console"],
                    sun_visors=body["sun_visors"],
                )

                data.clock = interior_amenities.clock
                data.tilt_telescopic_steering_wheel = (
                    interior_amenities.tilt_telescopic_steering_wheel
                )
                data.steering_column_lock = interior_amenities.steering_column_lock
                data.horn = interior_amenities.horn
                data.warning_chimes = interior_amenities.warning_chimes
                data.instrument_panel = interior_amenities.steering_column_lock
                data.windshield_wipers = interior_amenities.windshield_wipers
                data.rear_window_wiper = interior_amenities.rear_window_wiper
                data.interior_light_courtesy = (
                    interior_amenities.interior_light_courtesy
                )
                data.rear_view_mirror = interior_amenities.rear_view_mirror
                data.active_park_assist = interior_amenities.active_park_assist
                data.rear_entertainment_system = (
                    interior_amenities.rear_entertainment_system
                )
                data.power_outlets = interior_amenities.power_outlets
                data.lighter = interior_amenities.lighter
                data.glove_box = interior_amenities.glove_box
                data.center_armrest = interior_amenities.center_armrest
                data.console = interior_amenities.console
                data.sun_visors = interior_amenities.sun_visors

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Interior amenities",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )

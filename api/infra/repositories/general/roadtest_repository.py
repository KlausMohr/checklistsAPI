from flask import request
from api.entities.checklist.roadtest_enitity import RoadTest
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class RoadtestRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = db.session.query().with_entities(RoadTest).filter(RoadTest.id == id)
            try:
                if data:
                    for road_test in data:
                        response = {"road_test": road_test.to_json()}
                return response_gen(200, "Road tests", response)
            except Exception as excepetion:
                print(excepetion)
                return response_gen(204, "No content for Road tests", response)

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = db.session.query(RoadTest).filter(RoadTest.id == id).first()

            body = request.get_json()

            try:
                road_test = RoadTest(
                    engine_starting=body["engine_starting"],
                    engine_idling=body["engine_idling"],
                    remote_start=body["remote_start"],
                    engine_acceleration=body["engine_acceleration"],
                    engine_noise=body["engine_noise"],
                    auto_manual_transmission_shifting=body[
                        "auto_manual_transmission_shifting"
                    ],
                    auto_manual_transmission_noise=body[
                        "auto_manual_transmission_noise"
                    ],
                    shift_interlock_operation=body["shift_interlock_operation"],
                    drive_axle_transer_case_operation=body[
                        "drive_axle_transer_case_operation"
                    ],
                    clutch_operation=body["clutch_operation"],
                    steering_basic_operation=body["steering_basic_operation"],
                    body_suspension_squeaks=body["body_suspension_squeaks"],
                    struts_schocks_operation=body["struts_schocks_operation"],
                    brakes_abs_operation=body["brakes_abs_operation"],
                    cruise_control=body["cruise_control"],
                    gauges_operation=body["gauges_operation"],
                    driver_select_memory=body["driver_select_memory"],
                    no_abnormal_wind_noise=body["no_abnormal_wind_noise"],
                )

                data.engine_starting = road_test.engine_starting
                data.engine_idling = road_test.engine_idling
                data.remote_start = road_test.remote_start
                data.engine_acceleration = road_test.engine_acceleration
                data.engine_noise = road_test.engine_noise
                data.auto_manual_transmission_shifting = road_test.remote_start
                data.auto_manual_transmission_noise = (
                    road_test.auto_manual_transmission_noise
                )
                data.shift_interlock_operation = road_test.shift_interlock_operation
                data.drive_axle_transer_case_operation = (
                    road_test.drive_axle_transer_case_operation
                )
                data.clutch_operation = road_test.clutch_operation
                data.steering_basic_operation = road_test.steering_basic_operation
                data.body_suspension_squeaks = road_test.body_suspension_squeaks
                data.struts_schocks_operation = road_test.struts_schocks_operation
                data.brakes_abs_operation = road_test.brakes_abs_operation
                data.cruise_control = road_test.cruise_control
                data.gauges_operation = road_test.gauges_operation
                data.driver_select_memory = road_test.driver_select_memory
                data.no_abnormal_wind_noise = road_test.no_abnormal_wind_noise

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Road tests",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )

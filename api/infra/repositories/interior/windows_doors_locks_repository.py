from flask import request
from api.entities.checklist.interior.windows_doors_locks import WindowsDoorsLocks
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class WindowsDoorsLocksRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = (
                db.session.query()
                .with_entities(WindowsDoorsLocks)
                .filter(WindowsDoorsLocks.id == id)
            )
            try:
                if data:
                    for windows_doors_locks in data:
                        response = {
                            "windows_doors_locks": windows_doors_locks.to_json()
                        }
                return response_gen(200, "Windows, Doors and Locks", response)
            except Exception as excepetion:
                print(excepetion)
                return response_gen(
                    204, "No content for Windows, Doors and Locks", response
                )

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = (
                db.session.query(WindowsDoorsLocks)
                .filter(WindowsDoorsLocks.id == id)
                .first()
            )

            body = request.get_json()

            try:
                windows_doors_locks = WindowsDoorsLocks(
                    door_handles_release=body["door_handles_release"],
                    remote_entry=body["remote_entry"],
                    push_button_start=body["push_button_start"],
                    door_locks=body["door_locks"],
                    child_safety_locks=body["child_safety_locks"],
                    window_controls=body["window_controls"],
                    remote_decklid_release=body["remote_decklid_release"],
                    fuel_filler_door_release=body["fuel_filler_door_release"],
                )

                data.door_handles_release = windows_doors_locks.door_handles_release
                data.remote_entry = windows_doors_locks.remote_entry
                data.push_button_start = windows_doors_locks.push_button_start
                data.door_locks = windows_doors_locks.door_locks
                data.child_safety_locks = windows_doors_locks.child_safety_locks
                data.window_controls = windows_doors_locks.push_button_start
                data.remote_decklid_release = windows_doors_locks.remote_decklid_release
                data.fuel_filler_door_release = (
                    windows_doors_locks.fuel_filler_door_release
                )

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Windows, Doors and Locks",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )

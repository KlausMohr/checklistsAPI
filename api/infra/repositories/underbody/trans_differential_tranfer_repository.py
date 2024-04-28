from flask import request
from api.entities.checklist.underbody.trans_differential_transfer import (
    TransDiffTransfer,
)
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class TransDiffTransferRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = (
                db.session.query()
                .with_entities(TransDiffTransfer)
                .filter(TransDiffTransfer.id == id)
            )
            try:
                if data:
                    for trans_diff_transfer in data:
                        response = {
                            "trans_diff_transfer": trans_diff_transfer.to_json()
                        }
                return response_gen(
                    200, "Transmission, Differential and Transfer Case", response
                )
            except Exception as excepetion:
                print(excepetion)
                return response_gen(
                    204,
                    "No content for Transmission, Differential and Transfer Case",
                    response,
                )

    def insert():
        raise NotImplementedError

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = (
                db.session.query(TransDiffTransfer)
                .filter(TransDiffTransfer.id == id)
                .first()
            )

            body = request.get_json()

            try:
                trans_diff_transfer = TransDiffTransfer(
                    automatic_transmission=body["automatic_transmission"],
                    manual_transmission=body["manual_transmission"],
                    four_by_four_operation=body["four_by_four_operation"],
                    universal_cv_joints_boots=body["universal_cv_joints_boots"],
                    transmission_mounts=body["transmission_mounts"],
                    differential_drive_axle=body["differential_drive_axle"],
                )

                data.automatic_transmission = trans_diff_transfer.automatic_transmission
                data.manual_transmission = trans_diff_transfer.manual_transmission
                data.four_by_four_operation = trans_diff_transfer.four_by_four_operation
                data.universal_cv_joints_boots = (
                    trans_diff_transfer.universal_cv_joints_boots
                )
                data.transmission_mounts = trans_diff_transfer.transmission_mounts
                data.differential_drive_axle = (
                    trans_diff_transfer.four_by_four_operation
                )

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Transmission, Differential and Transfer Case",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )

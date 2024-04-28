from flask import request
from api.entities.checklist.interior.audio_alarm import AudioAlarm
from api.infra.database_config.database_config import DBConnection
from api.infra.response_generator.response_gen import response_gen
from ..irepository import Repository


class AudioAlarmRepository(Repository):
    def get_all():
        raise NotImplementedError

    def get_by_id(id):
        with DBConnection() as db:
            response = {}
            data = (
                db.session.query().with_entities(AudioAlarm).filter(AudioAlarm.id == id)
            )
            try:
                if data:
                    for audio_alarm in data:
                        response = {"audio_alarm": audio_alarm.to_json()}
                return response_gen(200, "Audio and alarm inspection", response)
            except Exception as excepetion:
                print(excepetion)
                return response_gen(204, "No content for Audio and Alarm", response)

    def insert():
        with DBConnection() as db:
            body = request.get_json()
            try:
                if body:

                    audio_alarm = AudioAlarm(
                    radio_cd_speaker=body["radio_cd_speakers"],
                    antenna=body["antenna"],
                    alarm_system=body["alarm_system"],
                    navigation_system=body["navigation_system"],
                )
                    db.session.add(audio_alarm)
                    db.session.commit()
                    return response_gen(
                        200,
                        "Audio and Alarm",
                        audio_alarm.to_json(),
                        "Audio and Alarm checklist inspection successfully inserted",
                    )
            except Exception as exception:
                print("Error: ", exception)
                return response_gen(
                    400,
                    "Audio and Alarm",
                    {},
                    "Error while inserting a new Audio and Alarm checklist inspection",
                )

    def delete(id):
        raise NotImplementedError

    def update(id):
        with DBConnection() as db:
            data = db.session.query(AudioAlarm).filter(AudioAlarm.id == id).first()

            body = request.get_json()

            try:
                audio_alarm = AudioAlarm(
                    radio_cd_speaker=body["radio_cd_speakers"],
                    antenna=body["antenna"],
                    alarm_system=body["alarm_system"],
                    navigation_system=body["navigation_system"],
                )

                data.radio_cd_speaker = audio_alarm.airbags
                data.antenna = audio_alarm.safety_belts
                data.alarm_system = audio_alarm.alarm_system
                data.navigation_system = audio_alarm.navigation_system

                db.session.add(data)
                db.session.commit()
                return response_gen(
                    200,
                    "Audio and Alarm",
                    data.to_json(),
                    "Checklist group successfully updated",
                )
            except Exception as excepetion:
                print("Error", excepetion)
                return response_gen(
                    400, "Error while trying to update this checklist group", {}
                )

from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from api.utils.database.database import db


migrate = Migrate()

DB_NAME = "checklist_app"


def create_app():
    app = Flask(__name__)
    app.config["JSON_SORT_KEYS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "postgresql://postgres:Admin1234@127.0.0.1:5432/checklist_app?options=-c%20search_path=checklist_app"
    )
    db.init_app(app)
    
    from api.entities.owner_entity import Owner
    from api.entities.vehicle_entity import Vehicle
    from api.entities.ownership_entity import Ownership
    from api.entities.checklist.exterior.body_bumpers import BodyPanelsBumper
    from api.entities.checklist.exterior.doors_hood_tailgate import DoorsHoodTailgate
    from api.entities.checklist.exterior.grille_trim_roof_rack import GrilleTrimRoofRack
    from api.entities.checklist.exterior.glass_outside_mirrors import GlassOutsideMirrors
    from api.entities.checklist.exterior.exterior_lights import ExteriorLights
    from api.entities.checklist.exterior_entity import Exterior
    from api.entities.checklist.diagnosis_entity import Diagnosis
    from api.entities.checklist.roadtest_enitity import RoadTest
    from api.entities.checklist.underbody_entity import Underboody
    from api.entities.checklist.hybrid_entity import Hybrid
    
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()
        db.session.commit()
        print('DB created!')

    return app

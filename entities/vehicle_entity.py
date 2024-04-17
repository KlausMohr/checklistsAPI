from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, String
from dataclasses import dataclass

Base = declarative_base()


@dataclass
class Vehicle(Base):
    __tablename__ = "tb_vehicle"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    make = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    year = Column(String(10), nullable=False)
    color = Column(String(10), nullable=False)
    vin = Column(String(30), nullable=False)
    mileage = Column(String(20), nullable=False)
    licenseplt = Column(String(8), nullable=False)

    __table_args__ = {"schema": "checklist_app"}

    def to_json(self):
        return {
            "id": self.id,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "color": self.color,
            "vin": self.vin,
            "mileage": self.mileage,
            "licenseplt": self.licenseplt,
        }

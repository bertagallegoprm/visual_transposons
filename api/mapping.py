from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os

connection_string = f"""mysql+mysqlconnector://{os.getenv("USER")}:{os.getenv("PASSWORD")}@{os.getenv("HOST")}/transposons"""

engine = create_engine(connection_string, echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Transposon(Base):
    __tablename__ = "transposon"
    id = Column(Integer, primary_key=True)
    name = Column(String, name="transposonName")
    id_location = Column(Integer, ForeignKey("location.id"))
    id_family = Column(Integer, ForeignKey("family.id"))

class Location(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True)
    start = Column(Integer, name="minStart")
    end = Column(Integer, name="maxEnd")
    id_chromosome = Column(Integer, ForeignKey("chromosome.id"))
    id_orientation = Column(Integer, ForeignKey("orientation.id"))
    transposon = relationship("Transposon")

class Orientation(Base):
    __tablename__ = "orientation"
    id = Column(Integer, primary_key=True)
    five_prime = Column(String, name="isFivePrime")
    location = relationship("Location")

class Chromosome(Base):
    __tablename__ = "chromosome"
    id = Column(Integer, primary_key=True)
    number = Column(Integer, name="chromosomeNumber")
    location = relationship("Location")

class Family(Base):
    __tablename__ = "family"
    id = Column(Integer, primary_key=True)
    name = Column(String, name="familyName")
    transposon = relationship("Transposon")
    id_super_family = Column(Integer, ForeignKey("superFamily.id"))

class SuperFamily(Base):
    __tablename__ = "superFamily"
    id = Column(Integer, primary_key=True)
    name = Column(String, name="superFamilyName")
    family = relationship("Family")

# Test
query1 = session.query(Transposon.name).count()
print("transposon: ",query1)
query2 = session.query(Location.start).count()
print("location: ",query2)
query3 = session.query(Orientation.five_prime).count()
print("orientation: ",query3)
query4 = session.query(Chromosome.number).count()
print("chromosome: ",query4)
query5 = session.query(Family.name).count()
print("family:", query5)
query6 = session.query(SuperFamily.name).count()
print("superFamily: ", query6)


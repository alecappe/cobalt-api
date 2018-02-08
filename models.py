# Refer to http://flask-sqlalchemy.pocoo.org/2.3/models/

from app import db


class Cpu_Mode(db.Model):
    """Full CPU model specification"""

    # Internal unique autoincremental ID
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Product name (es. INTEL® CORE™ i7-8709G)
    name = db.Column(db.String(40), unique=True, nullable=False)
    # Product family (es. Intel® Core™ i7 Processors)
    family = db.Column(db.String(40))
    # Generation
    generation = db.Column(db.Integer)
    # Base Frequency
    base_frequency = db.Column(db.Float, nullable=False)
    # Turbo Frequency
    turbo_frequency = db.Column(db.Float, nullable=False)
    # Cores
    cores = db.Column(db.Integer, nullable=False)
    # Threads
    threads = db.Column(db.Integer, nullable=False)
    # Cache
    cache = db.Column(db.Integer, nullable=False)
    # Bus Speed (es. 8 GT/s DMI)
    bus_speed = db.Column(db.Integer, nullable=False)
    # Max memory size (es. 64 GB)
    max_memory = db.Column(db.Integer, nullable=False)
    # Graphics Base-Frequency
    base_graphics_freq = db.Column(db.Float)
    # Graphics Max-Frequency
    max_graphics_freq = db.Column(db.Float)

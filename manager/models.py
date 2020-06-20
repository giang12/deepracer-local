from manager import db
from sqlalchemy_mixins import AllFeaturesMixin

class BaseModel(db.Model, AllFeaturesMixin):
    __abstract__ = True
    pass


class LocalModel(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    description = db.Column(db.String(128))
    track = db.Column(db.String(120))
    reward_function_filename = db.Column(db.String(120), default="reward.py")
    model_metadata_filename = db.Column(db.String(128), default="action_space.py")

    episodes_between_training = db.Column(db.Integer, default=20)
    batch_size = db.Column(db.Integer, default=10)
    epochs = db.Column(db.Integer, default=10)
    learning_rate = db.Column(db.Float, default=0.0003)
    entropy = db.Column(db.Float, default=0.01)
    discount_factor = db.Column(db.Float, default=0.999)
    loss_type = db.Column(db.String(64), default="mean squared error")

    change_start_position = db.Column(db.Boolean, default=True)
    alternate_direction = db.Column(db.Boolean, default=False)
    pretrained_model = db.Column(db.String(128), default=None)

    nn_layers = db.Column(db.Integer, default=3)
    sensor_stereo_cameras = db.Column(db.Boolean, default=False)
    sensor_lidar = db.Column(db.Boolean, default=False)

    race_type = db.Column(db.String(32), default="TIME_TRIAL")
    number_of_obstacles = db.Column(db.Integer, default=0)
    obstacle_type = db.Column(db.String(16), default="BOX")
    randomize_obstacle_locations = db.Column(db.Boolean, default=False)

    number_of_bot_cars = db.Column(db.Integer, default=0)
    bot_car_speed = db.Column(db.Float, default=1.0)
    is_lane_change = db.Column(db.Boolean, default=False)
    upper_lane_change_time = db.Column(db.Integer, default=5)
    lower_lane_change_time = db.Column(db.Integer, default=5)

    status = db.Column(db.String(64), default="queued")

    episodes_target = db.Column(db.Integer, default=1000)
    episodes_trained = db.Column(db.Integer, default=0)

    laps_complete = db.Column(db.Integer, default=0)
    average_pct_complete = db.Column(db.Float, default=0.0)
    best_lap_time = db.Column(db.Float, default=0.0)
    best_lap_episode = db.Column(db.Integer, default=0)
    crashes = db.Column(db.Integer, default=0)
    off_tracks = db.Column(db.Integer, default=0)

    minutes_target = db.Column(db.Integer, default=0)
    minutes_trained = db.Column(db.Integer, default=0)
    start_timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return '<LocalModel {}-{}>'.format(self.id, self.name)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
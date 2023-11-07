from services.activity_service import ActivityService
from services.user_service import UserService
from services.location_service import LocationService


# Use this to populate the database

def add_stuff():
    usr_s = UserService()
    act_s = ActivityService()
    loc_s = LocationService()

    usr_s.add_user(username="alpha", age=1, display_name="Alpha", password="alpha-pass", profile_picture="google.com")
    usr_s.add_user(username="beta", age=2, display_name="Beta", password="beta-pass", profile_picture="google.com")
    usr_s.add_user(username="gamma", age=3, display_name="Gamma", password="gamma-pass", profile_picture="google.com")
    usr_s.add_user(username="delta", age=4, display_name="Delta", password="delta-pass", profile_picture="google.com")
    usr_s.add_user(username="epsilon", age=5, display_name="Epsilon", password="epsilon-pass", profile_picture="google.com")

    loc_s.add_location(46.7781, 23.5775)
    loc_s.add_location(46.7723, 23.6123)
    loc_s.add_location(46.7675, 23.5972)
    loc_s.add_location(46.7703, 23.6034)
    loc_s.add_location(46.7661, 23.6261)

    act_s.add_activity(name="Alpha's Activity", category="Sport", description="This is Alpha's activity.", location_id=1, number_of_participants=111)
    act_s.add_activity(name="Beta's Activity", category="Sport", description="This is Beta's activity.", location_id=2, number_of_participants=222)
    act_s.add_activity(name="Gamma's Activity", category="Sport", description="This is Gamma's activity.", location_id=3, number_of_participants=333)
    act_s.add_activity(name="Delta's Activity", category="Sport", description="This is Delta's activity.", location_id=4, number_of_participants=444)
    act_s.add_activity(name="Epsilon's Activity", category="Sport", description="This is Epsilon's activity.", location_id=5, number_of_participants=555)




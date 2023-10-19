from services.activity_service import ActivityService
from services.user_service import UserService
from services.location_service import LocationService


# Use this to populate the database

def add_stuff():
    usr_s = UserService()
    act_s = ActivityService()
    loc_s = LocationService()

    usr_s.add_user("alpha", 1, "Alpha", "alpha-pass", profile_picture="google.com")
    usr_s.add_user("beta", 2, "Beta", "beta-pass", profile_picture="google.com")
    usr_s.add_user("gamma", 3, "Gamma", "gamma-pass", profile_picture="google.com")
    usr_s.add_user("delta", 4, "Delta", "delta-pass", profile_picture="google.com")
    usr_s.add_user("epsilon", 5, "Epsilon", "epsilon-pass", profile_picture="google.com")

    loc_s.add_location(46.7781, 23.5775)
    loc_s.add_location(46.7723, 23.6123)
    loc_s.add_location(46.7675, 23.5972)
    loc_s.add_location(46.7703, 23.6034)
    loc_s.add_location(46.7661, 23.6261)

    act_s.add_activity("alphas-activity", "Alpha's Activity", "Sport", "This is Alpha's activity.", 1, "111")
    act_s.add_activity("betas-activity", "Beta's Activity", "Sport", "This is Beta's activity.", 2, "222")
    act_s.add_activity("gammas-activity", "Gamma's Activity", "Sport", "This is Gamma's activity.", 3, "333")
    act_s.add_activity("deltas-activity", "Delta's Activity", "Sport", "This is Delta's activity.", 4, "444")
    act_s.add_activity("epsilons-activity", "Epsilon's Activity", "Sport", "This is Epsilon's activity.", 5, "555")


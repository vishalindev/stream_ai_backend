from app.main import app


def test_legacy_routes_are_registered():
    paths = {route.path for route in app.routes}
    assert "/Employee/createuser" in paths
    assert "/Plant/fetchplant" in paths
    assert "/PlatFormUser/fetchroleall" in paths
    assert "/Camera/fetchcamerasall" in paths
    assert "/Zone/createzone" in paths
    assert "/Rule/fetchruleall" in paths
    assert "/Notification/fetchnotification" in paths
    assert "/Dashboard/fetchanomalycameras" in paths
    assert "/Reports/fetchnoticiationface" in paths

from core.models import Host


def get_all_responsible_query():
    return Host.get_motor_collection().distinct("responsible")

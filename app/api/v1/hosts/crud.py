from beanie.odm.queries.find import FindMany

from core.models import Host


def get_all_hosts_query() -> FindMany[Host]:
    return Host.find_all()


def get_hosts_query(responsible: str) -> FindMany[Host]:
    return Host.find(Host.responsible == responsible)

from beanie.odm.queries.find import FindMany

from core.models import Host


def get_all_hosts_query() -> FindMany[Host]:
    all_hosts_query = Host.find_all()
    return all_hosts_query


def get_hosts_query(responsible: str) -> FindMany[Host]:
    hosts_query = Host.find(Host.responsible == responsible)
    return hosts_query

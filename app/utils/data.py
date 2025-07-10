from typing import Any

from beanie import Document
from beanie.odm.queries.find import FindMany


async def query_to_docs(query: FindMany[Document]) -> list[dict[str, Any]]:
    docs_list = await query.to_list()
    docs_dicts = [doc.model_dump(exclude={"id"}) for doc in docs_list]
    return docs_dicts

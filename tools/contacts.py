from typing import List
from langchain.agents import tool

CONTACTS = [{"name":"Gabriel", "phone":"+14077394397"}]


@tool("get_all_contacts")
def get_all_contacts(placeholder: str) -> List[dict]:
    """Get contacts."""
    return CONTACTS

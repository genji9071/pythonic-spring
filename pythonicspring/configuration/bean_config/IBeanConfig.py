from typing import List, Optional

from pydantic import BaseModel

from pythonicspring.configuration.IAbcConfig import IAbcConfig


class IBeanConfigProperty(BaseModel):
    name: str
    value: str


class IBeanConfig(IAbcConfig):
    id: str
    class_name: str
    properties: Optional[List[IBeanConfigProperty]]


if __name__ == '__main__':
    obj = IBeanConfig(id='abc', class_name=1)
    print('ok')

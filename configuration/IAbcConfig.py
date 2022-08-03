from abc import ABCMeta

from pydantic import BaseModel


class IAbcConfig(BaseModel, metaclass=ABCMeta):
    pass

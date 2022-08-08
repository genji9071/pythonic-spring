from enum import Enum

from pythonicspring.configuration.IAbcConfig import IAbcConfig
from pythonicspring.configuration.bean_config.IBeanConfig import IBeanConfig


class EConfigType(str, Enum):
    bean = 'bean'


config_type_map = {
    EConfigType.bean: IBeanConfig
}


class ISpringConfig:
    config_type: EConfigType
    detail: IAbcConfig

    def __init__(self, config_type, detail):
        config_class = config_type_map.get(config_type)
        if config_class is None:
            raise ValueError(f"initialize failed! config_type: {config_type}")
        config_instance = config_class.__new__(config_class)
        config_instance.__init__(**detail)
        self.detail = config_instance
        self.config_type = config_type


if __name__ == '__main__':
    obj = ISpringConfig(config_type=EConfigType.bean, detail=IBeanConfig(id='abc', class_name=1))
    print('ok')

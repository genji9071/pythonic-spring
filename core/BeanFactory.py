import json
import os
import pkgutil
from typing import Dict, List

from configuration.ISpringConfig import ISpringConfig, EConfigType
from configuration.bean_config.IBeanConfig import IBeanConfig
from core.BeanProxy import BeanProxy

_beans_dict_: Dict[str, BeanProxy] = {}
_beans_config_: Dict[str, IBeanConfig] = {}


class BeanFactory:

    def __init__(self, instance_path, scan_regex):
        self.working_directory = os.getcwd()
        self._load_property_(instance_path)
        self.add_beans_to_factory(scan_regex)

    def add_beans_to_factory(self, scan_regex):
        root_module_name = os.path.basename(self.working_directory)
        scan_regex_dict = None if scan_regex is None else self.nested(scan_regex).get(root_module_name)
        self.recursive_import(scan_regex_dict, self.working_directory, root_module_name)
        pass

    def recursive_import(self, scan_regex_dict, pkgpath, module_path):
        for _, file, _ in pkgutil.iter_modules([pkgpath]):
            next_dict = None
            if scan_regex_dict is not None:
                next_dict = scan_regex_dict.get("*") or scan_regex_dict.get(file)
                if "*" not in scan_regex_dict and file not in scan_regex_dict:
                    continue
            self.recursive_import(next_dict, f"{pkgpath}/{file}", f"{module_path}.{file}")
            __import__(f"{module_path}.{file}")

    def _load_property_(self, instance_path):
        for relpath, dirs, files in os.walk(self.working_directory):
            if "spring.json" in files:
                try:
                    with open(os.path.join(relpath, "spring.json"), 'r') as load_f:
                        load_conf = ISpringConfig(**json.load(load_f))
                    if load_conf.config_type == EConfigType.bean:
                        _beans_config_.setdefault(load_conf.detail.id, load_conf.detail)
                except Exception as ex:
                    print(f'??? {ex}')

    def nested(self, data: List[str], split: str = ".") -> dict:
        result = {}
        for key in data:
            paths = key.split(split)
            cursor = result
            for path in paths[:-1]:
                if cursor.get(path) is None:
                    cursor[path] = {}
                cursor = cursor.get(path)
            cursor[paths[-1]] = None
        return result

    @staticmethod
    def add_bean_to_factory(bean_name, bean_class=None) -> BeanProxy:
        prop_dict = {}
        bean_config = _beans_config_.get(bean_name)
        if bean_config is not None:
            prop_dict = zip(map(lambda x: x.name, bean_config.properties),
                            map(lambda x: x.value, bean_config.properties))
        if bean_class:
            instance = bean_class.__new__(bean_class)
            instance.__init__(**dict(prop_dict))
            if bean_name in _beans_dict_:
                _beans_dict_[bean_name].inject_bean(instance, bean_name)
            else:
                # bean_proxy = BeanProxy.__new__(BeanProxy)
                # bean_proxy.__init__()
                # bean_proxy = BeanProxy()
                # bean_proxy.inject_bean(instance, bean_name)
                bean_proxy = BeanProxy(instance, bean_name)
                _beans_dict_[bean_name] = bean_proxy
        else:
            _beans_dict_[bean_name] = BeanProxy(None, bean_name)
        return _beans_dict_[bean_name]

    @staticmethod
    def get_bean_by_name(name: str) -> BeanProxy:
        return _beans_dict_.get(name)

    @staticmethod
    def get_beans_by_type(cls) -> List[BeanProxy]:
        return list(filter(lambda x: x.__class__.__name__ == cls, _beans_dict_.values()))

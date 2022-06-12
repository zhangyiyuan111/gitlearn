import pytest

from commons.yaml_unit import clear_yaml


@pytest.fixture(scope="session", autouse=True)
def clear_extract():
    clear_yaml("extract.yaml")

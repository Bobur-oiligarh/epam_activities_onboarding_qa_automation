"""Fixtures to executing tests for instance host."""
import os
from typing import Dict
import pytest
import yaml
from test_framework.models.host_models.linux_host import LinuxHost

HOST_DATA_FILE = 'host_data.yaml'


@pytest.fixture()
def get_expected_data_for_linux_host(request) -> Dict:
    """This tool extracts ec2 datas from .yaml file to python readable type: dictionary
    Here uses the request fixture to get the full path of .yaml file

    :return: dictionary filled with file content
    """
    dir_path = os.path.dirname(request.module.__file__)
    file_path = os.path.join(dir_path, HOST_DATA_FILE)
    with open(file_path) as file:
        documents = yaml.load(file, Loader=yaml.SafeLoader)
    return documents


@pytest.fixture()
def get_actual_data_for_linux_host(get_expected_data_for_linux_host) -> LinuxHost:
    """This fixture initializes an original linux host using LinuxHost model

    :param get_expected_data_for_linux_host: fixture which provide expected datas
    :return: LinuxHost object instance
    """
    user = get_expected_data_for_linux_host.get('user')
    server_ip = get_expected_data_for_linux_host.get('host_ip')
    ssh_config_path = get_expected_data_for_linux_host.get('path_to_ssh_config')
    return LinuxHost(user=user, server_ip=server_ip, ssh_config_path=ssh_config_path)

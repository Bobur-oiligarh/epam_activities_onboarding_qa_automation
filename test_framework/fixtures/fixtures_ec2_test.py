"""Fixtures to executing tests for EC2."""
import os
import logging
from typing import Dict
from botocore.exceptions import ClientError
from test_framework.models.aws_ec2_models.aws_ec2_resouces import AWSEC2, NetworkInterface, AWSSecurityGroups
import yaml
import pytest

EC2_DATA_FILE = 'ec2_instance_data.yaml'


@pytest.fixture()
def get_expected_result(request) -> Dict:
    """
    This tool extracts ec2 datas from .yaml file to python readable type: dictionary
    Here uses the request fixture to get the full path of .yaml file
    :return: dictionary filled with file content
    """
    dir_path = os.path.dirname(request.module.__file__)
    file_path = os.path.join(dir_path, EC2_DATA_FILE)
    with open(file_path) as file:
        documents = yaml.load(file, Loader=yaml.SafeLoader)
    return documents


@pytest.fixture()
def get_ec2_instance_id(get_expected_result) -> str:
    """Fixture to get an aws instance id, which is tested
    :param get_expected_result: fixture which provides instance id
    :return: string
    """
    return get_expected_result.get('id')


@pytest.fixture()
def get_ec2_network_interface_id(get_expected_result) -> str:
    """
    Fixture to get an aws instance id, which is tested
    :param get_expected_result: fixture which provides instance id
    :return: string
    """
    return get_expected_result.get('network_interface_id')


@pytest.fixture()
def get_actual_result(get_ec2_instance_id: str) -> AWSEC2:
    """
    Initializes an original aws ec2 object with accepted instance id
    :param get_ec2_instance_id: fixture which provides instance id
    :return: AWSEC2 object
    """
    try:
        return AWSEC2(get_ec2_instance_id)
    except ClientError as error:
        logging.error(f'Cant open EC2 instance: {error}')
    return None


@pytest.fixture()
def get_actual_network_interface(get_ec2_network_interface_id: str) -> NetworkInterface:
    """
    Initializes a Network Interface from AWS EC2 with excepted id
    :param get_ec2_network_interface_id: fixture which
                                         provides network interface id
    :return: NetworkInterface object
    """
    return NetworkInterface(get_ec2_network_interface_id)


@pytest.fixture()
def get_actual_allowed_ports(get_actual_result: AWSEC2) -> AWSSecurityGroups:
    """
    Gets allowed ports for certain by id AWS EC2 Security Group
    :param get_actual_result: fixture which is instance of AWS EC2
    :return: AWSSecurityGroup
    """
    security_group_id = get_actual_result.security_group_id
    return AWSSecurityGroups(security_group_id)

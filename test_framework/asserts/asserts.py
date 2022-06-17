from typing import Dict

from pytest_check import check_func
from test_framework.models.aws_ec2_resouces import AWSEC2

"""
Module with several asserts for test EC2 instance
"""


@check_func
def soft_check_instance_exist(ec2_instance: AWSEC2) -> bool:
    """
    Checks EC2 instance for existence.
    :param: actual_result: AWSEC2 object
    :return: return boolean value
    """
    error_message = f'EC2 instance does not exist: {ec2_instance.tags_name}'
    assert ec2_instance, error_message
    return bool(ec2_instance)


def soft_check(expected_result: Dict, actual_result: AWSEC2):
    """
    Compares ec2 origin data from aws.amazon.com with expected data from yaml
    :param expected_result: ec2 expected datas from yaml file
    :param actual_result: ec2 actual datas from aws servers
    :return:
    """
    error_message = f"expected_result: {expected_result}; " \
                    f"actual_result: {actual_result}"
    assert expected_result == actual_result, error_message

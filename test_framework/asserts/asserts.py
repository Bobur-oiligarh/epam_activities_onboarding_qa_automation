from typing import Dict
from models.aws_ec2_resouces import AWSEC2

"""Module with several asserts for test EC2 instance.
"""


def soft_check(expected_result: Dict, actual_result: AWSEC2, attribute: str):
    """
    Compares ec2 origin data from aws.amazon.com with expected data from yaml
    :param attribute: an attribute name, which will tested
    :param expected_result: ec2 expected datas from yaml file
    :param actual_result: ec2 actual datas from aws servers
    :return:
    """
    error_message = f"{attribute} does not match. Expected_result: {expected_result}; " \
                    f"Actual_result: {actual_result}"
    assert expected_result == actual_result, error_message

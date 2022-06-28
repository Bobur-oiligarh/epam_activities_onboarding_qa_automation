
"""Module with several asserts for test EC2 instance.
"""


def soft_check(expected_result: str, actual_result: str, type_of_check: str):
    """
    Compares ec2 origin data from aws.amazon.com with expected data from yaml
    :param type_of_check: an attribute name, which will tested
    :param expected_result: ec2 expected datas from yaml file
    :param actual_result: ec2 actual datas from aws servers
    :return:
    """
    assert expected_result == actual_result, \
        f"{type_of_check} does not match. Expected_result: {expected_result}; " \
        f"Actual_result: {actual_result}"

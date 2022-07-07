"""Module with several validations for test EC2 instance.
"""


def soft_check(expected_result: object, actual_result: object,):
    """
    Compares ec2 origin data from aws.amazon.com with expected data from yaml
    :param expected_result: ec2 expected datas from yaml file
    :param actual_result: ec2 actual datas from aws servers
    """
    assert expected_result == actual_result, \
        f"Actual data does not match to expected data. " \
        f"Expected_result: {expected_result}; Actual_result: {actual_result}"

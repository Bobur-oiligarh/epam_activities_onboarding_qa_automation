"""
Module contains tests of EC2 instances
"""

from test_packages.asserts.asserts import soft_check, soft_check_instance_exist


def test_ec2_instance_image_id(get_expected_result, get_actual_result):
    expected_image_id = get_expected_result['image_id']
    actual_image_id = get_actual_result.image_id
    if soft_check_instance_exist(get_actual_result):
        soft_check(expected_image_id, actual_image_id)


def test_ec2_instance_type(get_expected_result, get_actual_result):
    expected_instance_type = get_expected_result['instance_type']
    actual_instance_type = get_actual_result.instance_type
    if soft_check_instance_exist(get_actual_result):
        soft_check(expected_instance_type, actual_instance_type)


def test_ec2_instance_tags(get_expected_result, get_actual_result):
    expected_instance_tags = get_expected_result['tags']
    actual_instance_tags = get_actual_result.tags_name
    if soft_check_instance_exist(get_actual_result):
        soft_check(expected_instance_tags, actual_instance_tags)


def test_ec2_instance_key_name(get_expected_result, get_actual_result):
    expected_instance_key_name = get_expected_result['key_name']
    actual_instance_key_name = get_actual_result.key_name
    if soft_check_instance_exist(get_actual_result):
        soft_check(expected_instance_key_name, actual_instance_key_name)


def test_ec2_instance_private_ip_address(get_expected_result, get_actual_result):
    expected_instance_private_ip = get_expected_result['private_ip_address']
    actual_instance_private_ip = get_actual_result.private_ip_address
    if soft_check_instance_exist(get_actual_result):
        soft_check(expected_instance_private_ip, actual_instance_private_ip)


def test_ec2_instance_state(get_expected_result, get_actual_result):
    expected_instance_state = get_expected_result['state']
    actual_instance_state = get_actual_result.state
    if soft_check_instance_exist(get_actual_result):
        soft_check(expected_instance_state, actual_instance_state)


def test_ec2_network_interface_tag(get_expected_result, get_actual_network_interface):
    expected_network_interface_tag = get_expected_result['network_interface_tag']
    actual_network_interface_tag = get_actual_network_interface.tag
    soft_check(expected_network_interface_tag, actual_network_interface_tag)


def test_ec2_allowed_ports(get_expected_result, get_actual_allowed_ports):
    expected_allowed_ports = get_expected_result["security_group_allowed_ports"]
    actual_allowed_ports = get_actual_allowed_ports.get_allowed_ports
    soft_check(expected_allowed_ports, actual_allowed_ports)

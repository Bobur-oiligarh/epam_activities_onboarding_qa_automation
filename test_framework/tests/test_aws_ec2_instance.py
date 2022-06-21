"""Module contains tests for EC2 instances."""

from asserts.asserts import soft_check


def test_ec2_instance_image_id(get_expected_result, get_actual_result):
    """Validate instance image id"""
    expected_image_id = get_expected_result['image_id']
    actual_image_id = get_actual_result.image_id
    soft_check(expected_image_id, actual_image_id, "Image_id")


def test_ec2_instance_type(get_expected_result, get_actual_result):
    """Validate instance type"""
    expected_instance_type = get_expected_result['instance_type']
    actual_instance_type = get_actual_result.instance_type
    soft_check(expected_instance_type, actual_instance_type, "Instance_type")


def test_ec2_instance_tags(get_expected_result, get_actual_result):
    """Validate instance tags"""
    expected_instance_tags = get_expected_result['tags']
    actual_instance_tags = get_actual_result.tags_name
    soft_check(expected_instance_tags, actual_instance_tags, "Instance_tags")


def test_ec2_instance_key_name(get_expected_result, get_actual_result):
    """Validate key pair name"""
    expected_instance_key_name = get_expected_result['key_name']
    actual_instance_key_name = get_actual_result.key_name
    soft_check(expected_instance_key_name, actual_instance_key_name, "Key_name")


def test_ec2_instance_private_ip_address(get_expected_result, get_actual_result):
    """Validate instance private ip_address"""
    expected_instance_private_ip = get_expected_result['private_ip_address']
    actual_instance_private_ip = get_actual_result.private_ip_address
    soft_check(expected_instance_private_ip, actual_instance_private_ip, "Private_ip_address")


def test_ec2_instance_state(get_expected_result, get_actual_result):
    """Validate instance state"""
    expected_instance_state = get_expected_result['state']
    actual_instance_state = get_actual_result.state
    soft_check(expected_instance_state, actual_instance_state, "Instance_state")


def test_ec2_network_interface_tag(get_expected_result, get_actual_network_interface):
    """Validate network interface tag"""
    expected_network_interface_tag = get_expected_result['network_interface_tag']
    actual_network_interface_tag = get_actual_network_interface.tag
    soft_check(expected_network_interface_tag, actual_network_interface_tag, "Net_interface_tag")


def test_ec2_allowed_ports(get_expected_result, get_actual_allowed_ports):
    """Validate Security Group allowed ports"""
    expected_allowed_ports = get_expected_result["security_group_allowed_ports"]
    actual_allowed_ports = get_actual_allowed_ports.get_allowed_ports
    soft_check(expected_allowed_ports, actual_allowed_ports, "SG_allowed_ports")

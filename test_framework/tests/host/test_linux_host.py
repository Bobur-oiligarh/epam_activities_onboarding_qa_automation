"""Contains tests for linux host testing."""

from test_framework.validations.aws_validation import soft_check


def test_host_distribution(get_expected_data_for_linux_host, get_actual_data_for_linux_host):
    """Validate host OS distribution."""
    expected_data = get_expected_data_for_linux_host.get("distribution")
    soft_check(expected_data, get_actual_data_for_linux_host.distribution)


def test_package_is_installed(get_expected_data_for_linux_host, get_actual_data_for_linux_host):
    """Validate any package installation."""
    package_name = get_expected_data_for_linux_host.get("package_name")
    soft_check("True", get_actual_data_for_linux_host.is_package_installed(package_name))


def test_docker_container_is_running(get_expected_data_for_linux_host, get_actual_data_for_linux_host):
    """Validate running docker container."""
    docker_container = get_expected_data_for_linux_host.get("docker_container_name")
    soft_check('True', get_actual_data_for_linux_host.is_docker_container_running(docker_container))


def test_socket_is_listening_port(get_expected_data_for_linux_host, get_actual_data_for_linux_host):
    """Validate socket listening ports."""
    host_ip = get_expected_data_for_linux_host['host_ip']
    port_number = get_expected_data_for_linux_host['flask_api_socket_listening_port']
    soft_check('True', get_actual_data_for_linux_host.is_socket_listening(host_ip, port_number))

"""
Module with LinuxHost class, which is to initialize and get actual datas for
instance hosts.
"""
import testinfra
from test_framework.models.host_models.base_host import BaseHost


class LinuxHost(BaseHost):
    """Class for linux models."""

    def __init__(self, user: str, server_ip: str, ssh_config_path: str):
        """Initialize an instance host.

        :param user: username of host OS
        :param server_ip: a public_ip of the server
        :param ssh_config_path: path to ssh config file (ssh public key .pem in aws)
        """
        self.host = testinfra.get_host(f"paramiko://{user}@{server_ip}", ssh_config=ssh_config_path)

    @property
    def distribution(self) -> str:
        """Gets host OS distribution.

        :return: string type
        """
        return self.host.system_info.distribution

    def is_package_installed(self, package_name: str) -> bool:
        """Gets info about is docker installed.

        :param package_name: a package_name which should be checked
        :return: True or False value
        """
        return self.host.package(package_name).is_installed

    def is_docker_container_running(self, container_name: str) -> bool:
        """Method checks is docker running.

        :param container_name: the container name, string type
        :return: True or False
        """
        return self.host.docker(container_name).is_running

    def is_socket_listening(self, host_ip: str, port: str) -> bool or str:
        """Method checks is socket listening.

        :param host_ip: public ip address of ec2 instance, string type
        :param port: port number in which socket listens according rules.
        :return: True or False
        """
        return self.host.socket(f"tcp://{host_ip}:{port}").is_listening



from typing import Dict
import boto3

"""Module with class AWS to connect with origin aws ec2 instance using boto3.
"""


class AWSEC2:
    """
    A class to initialize with original AWS ec2 instance and to get its attributes
    """

    def __init__(self, instance_id: str):
        """
        Initializes an aws ec2 instance with excepted its id
        :param instance_id: string
        """
        self.ec2 = boto3.resource('ec2', region_name='ap-south-1')
        self.instance = self.ec2.Instance(instance_id)

        self.tags_name = self.instance.tags[0]
        self.image_id = self.instance.image_id
        self.instance_type = self.instance.instance_type
        self.key_name = self.instance.key_name
        self.private_ip_address = self.instance.private_ip_address
        self.state = self.instance.state['Name']
        self.security_group_id = self.instance.security_groups[0]['GroupId']


class NetworkInterface:
    """
    This class accepts a Network Interface ID as an argument and
    initializes with it, so that we can get an information about its attributes.
    """

    def __init__(self, network_interface_id: str):
        """
        Initializes AWS network_interface using its ID
        :param network_interface_id: string type
        """
        self._ec2 = boto3.resource('ec2', region_name='ap-south-1')
        self.network_interface = self._ec2.NetworkInterface(network_interface_id)

        self.tag = self.network_interface.tag_set[0]['Value']
        self.ip_address = self.network_interface.private_ip_address


class AWSSecurityGroups:
    """
    Provides an original AWS EC2 Security Group
    by initializing with it with its id.
    """

    def __init__(self, group_id: str):
        """
        Initializes EC2 Security Group by its id
        :param group_id: security group id
        """
        self.ec2 = boto3.resource('ec2', region_name='ap-south-1')
        self.security_group = self.ec2.SecurityGroup(group_id)
        self.allowed_ports = {}

    @property
    def get_allowed_ports(self) -> Dict:
        """
        Gets all allowed ports for certain security_group
        :return: dictionary with allowed ports
        """
        ip_permissions = self.security_group.ip_permissions
        self.allowed_ports = {"FromPort": [], 'ToPort': []}

        for item in ip_permissions:
            self.allowed_ports['FromPort'].append(item['FromPort'])
            self.allowed_ports['ToPort'].append(item['ToPort'])
        return self.allowed_ports

import boto3


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
        self.ec2 = boto3.resource('ec2', region_name='ap-south-1')
        self.network_interface = self.ec2.NetworkInterface(network_interface_id)
        self.tag = self.network_interface.tag_set[0]['Value']
        self.ip_address = self.network_interface.private_ip_address

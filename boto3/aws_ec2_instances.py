import boto3


class EC2Instance:
    """
    This class accepts an instance ID as an argument and
    initializes with it, so that we can get an information about it.
    """

    def __init__(self, instance_id: str):
        """
        Initializes AWS EC2 instance with instance_id
        :param instance_id: string type
        """
        self.ec2 = boto3.resource('ec2', region_name='ap-south-1')
        self.instance = self.ec2.Instance(instance_id)
        self.tag = self.instance.tags
        self.state = self.instance.state
        self.security_groups = self.instance.security_groups
        self.public_ip = self.instance.public_ip_address
        self.private_ip = self.instance.private_ip_address
        self.ami = self.instance.image_id
        self.instance_type = self.instance.instance_type


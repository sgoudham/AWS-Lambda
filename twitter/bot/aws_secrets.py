import boto3


def get_secret(parameter_name):
    """Get a parameter from SSM Parameter store and decrypt it"""

    ssm = boto3.client('ssm')
    return ssm.get_parameter(Name=parameter_name, WithDecryption=True)['Parameter']['Value']

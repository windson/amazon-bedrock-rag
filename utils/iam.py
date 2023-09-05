import boto3


def get_account_id():
    sts = boto3.client("sts")
    return sts.get_caller_identity()["Account"]


def get_execution_role_arn():
    sts = boto3.client("sts")
    return sts.get_caller_identity()['Arn']
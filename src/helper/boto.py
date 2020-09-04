# import logging
import boto3

class BotoHelper():

  def __init__(self, namespace, region_name='eu-west-1'):
    self.__namespace  = namespace
    self.client       = boto3.client(self.__namespace,region_name)
    # boto3.set_stream_logger(name='botocore')

  def change_credentials(self, credentials, region='eu-west-1'):
    self.client = boto3.client(self.__namespace,
        region_name=region,
        aws_access_key_id=credentials["AccessKeyId"],
        aws_secret_access_key=credentials["SecretAccessKey"],
        aws_session_token=credentials["SessionToken"]
      )

  def who_am_i(self):
    response = self.client.get_caller_identity()
    print(response)

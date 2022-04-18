import boto3

def lambda_handler(event, context):
   
  ec2 = boto3.client('ec2',region_name="ap-southeast-1")
  
  instances = ec2.describe_instances(Filters=[  {'Name':'tag:Name', 'Values':["webserver"]},
                                              {'Name':'tag:Project', 'Values':["zomato"]}
                                              
                                           ]
                                    )

  for item in instances['Reservations']:
    
    instance = item['Instances'][0]
    instance_id = instance['InstanceId']
    print("Stopping Instance : {}".format(instance_id))
    ec2.stop_instances(InstanceIds=[ instance_id ])

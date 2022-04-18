# Python_Lambda_fuction_to_stop-start_an_instance

AWS Lambda is Amazon’s serverless compute service. You can run your code on it without having to manage servers or even containers. It will automatically scale depending on how much work you feed into it. And it build event-driven functions for easy communication between decoupled services. Reduce costs by running applications during times of peak demand i.e you need to pay only for the time taken to execute the code. The key features of Lambda function are : 

## Outline

First we will be creating a lambda function to stop/start testing instance in order to reduce cost. Then we will create a python code to stop, start instance and upload it to Lambda. Now we will apply a trigger on lambda function using AWS cloudwatch events. We have crontab facility in AWS cloudwatch, so we schedule a cronjob to apply the trigger on lambda at the demanding time.

## Requirements

- Boto module

  ```
  # pip3 install boto3
  ```
  - Python code to stop/start instance (stop.py, start.py)

## Provisioning

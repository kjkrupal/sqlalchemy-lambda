import aws_cdk as core
import aws_cdk.assertions as assertions

from sqlalchemy_lambda.sqlalchemy_lambda_stack import SqlalchemyLambdaStack

# example tests. To run these tests, uncomment this file along with the example
# resource in sqlalchemy_lambda/sqlalchemy_lambda_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SqlalchemyLambdaStack(app, "sqlalchemy-lambda")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

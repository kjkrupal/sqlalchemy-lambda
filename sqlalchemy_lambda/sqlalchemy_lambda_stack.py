import os
import subprocess
import configparser
from aws_cdk import (
    Stack,
    aws_lambda as function,
    aws_apigateway as api
)
from constructs import Construct


class SqlalchemyLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        crud_lambda_name = "crud-function"
        crud_api_name = "crud-api"

        dependencies_layer = self.create_dependencies_layer(
            self.stack_name, crud_lambda_name
        )

        configs = self.get_configs()

        crud_lambda = function.Function(
            self,
            crud_lambda_name,
            handler="function.handler",
            runtime=function.Runtime.PYTHON_3_8,
            code=function.Code.from_asset("src/lambdas/crud"),
            layers=[dependencies_layer],
        )
        crud_lambda.add_environment("USER", configs["user"])
        crud_lambda.add_environment("PASSWORD", configs["password"])
        crud_lambda.add_environment("HOST", configs["host"])
        crud_lambda.add_environment("PORT", configs["port"])
        crud_lambda.add_environment("DATABASE", configs["database"])

        api.LambdaRestApi(
            self,
            crud_api_name,
            handler=crud_lambda
        )

    def get_configs(self):
        config = configparser.ConfigParser()
        config.read("environment.ini")
        return config.defaults()

    def create_dependencies_layer(self, stack_name, function_name):
        requirements_file = "src/requirements.txt"
        output_dir = f"layer/{function_name}"

        if not os.environ.get("SKIP_PIP"):
            subprocess.check_call(
                f"pip install -r {requirements_file} -t {output_dir}/python".split()
            )

        layer_id = f"{stack_name}-{function_name}-dependencies"
        layer_code = function.Code.from_asset(output_dir)
        return function.LayerVersion(self, layer_id, code=layer_code)

from aws_lambda_powertools.utilities.parser import BaseModel


class Author(BaseModel):
    id: int
    name: str

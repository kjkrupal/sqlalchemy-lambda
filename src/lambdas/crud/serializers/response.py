from aws_lambda_powertools.utilities.parser import BaseModel


class ErrorSerializer(BaseModel):
    message: str
    error: str


class AuthorSerializer(BaseModel):
    id: int
    name: str

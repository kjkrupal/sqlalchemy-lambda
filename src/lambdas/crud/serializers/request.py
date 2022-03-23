from aws_lambda_powertools.utilities.parser import BaseModel


class CreateAuthorSerializer(BaseModel):
    name: str


class UpdateAuthorSerializer(BaseModel):
    id: int
    name: str


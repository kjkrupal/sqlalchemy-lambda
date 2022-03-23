from aws_lambda_powertools.utilities.parser import BaseModel


class CreateAuthor(BaseModel):
    name: str


class UpdateAuthor(BaseModel):
    id: int
    name: str


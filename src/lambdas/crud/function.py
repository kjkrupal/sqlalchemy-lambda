import os
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from aws_lambda_powertools.event_handler.api_gateway import APIGatewayRestResolver
from aws_lambda_powertools.event_handler.api_gateway import Response
from aws_lambda_powertools.utilities.parser import parse
from dto.request import CreateAuthor
from dao.models import Author, Book


db_string = "mysql+pymysql://{user}:{password}@{host}/{database}".format(
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    host=os.getenv("HOST"),
    database=os.getenv("DATABASE")
)
engine = create_engine(db_string, echo=True)
Session = sessionmaker(bind=engine)

app = APIGatewayRestResolver()


@app.post("/authors")
def create_author():
    create_author_json = app.current_event.json_body

    try:
        create_author = parse(create_author_json, model=CreateAuthor)
        author = Author(name=create_author.name)
        session = Session()
        session.add(author)
        session.commit()

        response = {
            "id": author.id,
            "name": author.name
        }

        return Response(
            status_code=201,
            content_type="application/json",
            body=json.dumps(response),
        )

    except Exception as e:
        response = {
            "message": "Something went wrong.",
            "error": str(e)
        }
        return Response(
            status_code=400,
            content_type="application/json",
            body=json.dumps(response),
        )


@app.get("/authors")
def get_authors():
    return [
        {
            "name": "krupal"
        },
        {
            "name": "tanvi"
        }
    ]


@app.get("/authors/{id}")
def get_author_by_id(id: int):
    pass


@app.put("/authors/{id}")
def update_author(id: int):
    pass


@app.delete("/authors/{id}")
def delete_author(id: int):
    pass


def handler(event, context):
    return app.resolve(event, context)

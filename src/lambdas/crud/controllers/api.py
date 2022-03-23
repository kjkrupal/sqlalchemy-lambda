import os
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from aws_lambda_powertools.event_handler.api_gateway import APIGatewayRestResolver
from aws_lambda_powertools.event_handler.api_gateway import Response
from aws_lambda_powertools.utilities.parser import parse
from serializers.request import CreateAuthorSerializer, UpdateAuthorSerializer
from serializers.response import AuthorSerializer, ErrorSerializer
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
        create_author = parse(create_author_json, model=CreateAuthorSerializer)
        author = Author(name=create_author.name)
        session = Session()
        session.add(author)
        session.commit()

        response = AuthorSerializer(id=author.id, name=author.name).dict()

        return Response(
            status_code=201,
            content_type="application/json",
            body=json.dumps(response)
        )

    except Exception as e:
        response = ErrorSerializer(message="Something went wrong.", error=str(e)).dict()
        return Response(
            status_code=400,
            content_type="application/json",
            body=json.dumps(response),
        )


@app.get("/authors")
def get_authors():

    try:
        session = Session()
        authors = session.query(Author).all()

        response = [
            AuthorSerializer(id=author.id, name=author.name).dict()
            for author in authors
        ]

        return Response(
            status_code=200,
            content_type="application/json",
            body=json.dumps(response),
        )
    except Exception as e:
        response = ErrorSerializer(message="Something went wrong.", error=str(e)).dict()
        return Response(
            status_code=400,
            content_type="application/json",
            body=json.dumps(response),
        )


@app.get("/authors/<id>")
def get_author_by_id(id: int):
    try:
        session = Session()
        author = session.query(Author).get(id)

        response = AuthorSerializer(id=author.id, name=author.name).dict()

        return Response(
            status_code=201,
            content_type="application/json",
            body=json.dumps(response),
        )

    except Exception as e:
        response = ErrorSerializer(message="Author with id " + str(id) + " does not exist", error=str(e)).dict()
        return Response(
            status_code=400,
            content_type="application/json",
            body=json.dumps(response),
        )


@app.put("/authors/<id>")
def update_author(id: int):
    update_author_json = app.current_event.json_body

    try:
        update_author = parse(update_author_json, model=UpdateAuthorSerializer)
        session = Session()
        author = session.query(Author).get(id)
        author.name = update_author.name
        session.commit()

        response = AuthorSerializer(id=author.id, name=author.name).dict()

        return Response(
            status_code=200,
            content_type="application/json",
            body=json.dumps(response),
        )

    except Exception as e:
        response = ErrorSerializer(message="Author with id " + str(id) + " does not exist", error=str(e)).dict()
        return Response(
            status_code=400,
            content_type="application/json",
            body=json.dumps(response),
        )


@app.delete("/authors/<id>")
def delete_author(id: int):

    try:
        session = Session()
        author = session.query(Author).filter(Author.id == id).delete()
        session.commit()

        return Response(
            status_code=204,
            content_type="application/json",
            body=None
        )

    except Exception as e:
        response = ErrorSerializer(message="Author with id " + str(id) + " does not exist", error=str(e)).dict()
        return Response(
            status_code=400,
            content_type="application/json",
            body=json.dumps(response),
        )


@app.post("/books")
def create_book():
    create_author_json = app.current_event.json_body

    try:
        create_author = parse(create_author_json, model=CreateAuthorSerializer)
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


@app.get("/books")
def get_books():
    return [
        {
            "name": "krupal"
        },
        {
            "name": "tanvi"
        }
    ]


@app.get("/books/<id>")
def get_book_by_id(id: int):
    pass


@app.put("/books/<id>")
def update_book(id: int):
    pass


@app.delete("/books/<id>")
def delete_book(id: int):
    pass


@app.get("/authors/<author_id>/books")
def get_books_by_author_id(author_id: int):
    pass


@app.get("/authors/<author_id>/books/<book_id>")
def get_books_by_id_by_author_id(author_id: int, book_id: int):
    pass


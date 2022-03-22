from aws_lambda_powertools.event_handler import APIGatewayRestResolver


app = APIGatewayRestResolver()


class AuthorController:

    def __init__(self):
        pass

    def resolve(self, event, context):
        return app.resolve(event, context)

    @app.post("/authors")
    def create_author():
        pass

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

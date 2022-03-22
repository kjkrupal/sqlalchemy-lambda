from api.author import AuthorController


def handler(event, context):
    controller = AuthorController()
    response = controller.resolve(event, context)
    return response

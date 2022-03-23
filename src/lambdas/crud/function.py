from controllers.api import app


def handler(event, context):
    return app.resolve(event, context)

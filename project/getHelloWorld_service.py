from pydantic import BaseModel


class HelloWorldRequest(BaseModel):
    """
    A simple request model for the Hello World endpoint. There are no parameters required for this request.
    """

    pass


class HelloWorldResponse(BaseModel):
    """
    The response model for the Hello World endpoint. It returns a simple JSON object with a single key-value pair.
    """

    message: str


def getHelloWorld(request: HelloWorldRequest) -> HelloWorldResponse:
    """
    This endpoint returns a JSON formatted 'hello world' message. It utilizes the ResponseFormatter module to ensure the message is returned in a standardized JSON format. When a client sends a GET request to this endpoint, the server will respond with a JSON object containing the key 'message' and value 'hello world'. This endpoint can be accessed by both administrators and users.

    Args:
    request (HelloWorldRequest): A simple request model for the Hello World endpoint. There are no parameters required for this request.

    Returns:
    HelloWorldResponse: The response model for the Hello World endpoint. It returns a simple JSON object with a single key-value pair.

    Example:
        request = HelloWorldRequest()
        response = getHelloWorld(request)
        assert response.message == 'hello world'
    """
    response = HelloWorldResponse(message="hello world")
    return response

from pydantic import BaseModel


class HelloWorldRequestModel(BaseModel):
    """
    The request model for the hello world endpoint. Since it's a simple GET request with no additional parameters, the fields are empty.
    """

    pass


class HelloWorldResponseModel(BaseModel):
    """
    The response model for the hello world endpoint, containing a single field for the 'hello world' message.
    """

    message: str


def get_hello_world(request: HelloWorldRequestModel) -> HelloWorldResponseModel:
    """
    This endpoint returns a simple message 'hello world'. It does not require any input parameters or authentication, making it accessible to anyone. The returned response is a plain text message.

    Args:
    request (HelloWorldRequestModel): The request model for the hello world endpoint. Since it's a simple GET request with no additional parameters, the fields are empty.

    Returns:
    HelloWorldResponseModel: The response model for the hello world endpoint, containing a single field for the 'hello world' message.

    Example:
    >>> request = HelloWorldRequestModel()
    >>> response = get_hello_world(request)
    >>> print(response.message)
    'hello world'
    """
    return HelloWorldResponseModel(message="hello world")

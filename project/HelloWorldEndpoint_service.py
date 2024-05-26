import asyncio

import prisma
import prisma.models
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


async def format_response(message: str) -> str:
    """
    Formats the provided message using the ResponseFormatter module.

    Args:
        message (str): The message to be formatted.

    Returns:
        str: The formatted message.

    Example:
        message = 'hello world'
        formatted_message = await format_response(message)
        > '<JSON formatted message>'
    """
    formatter = await prisma.models.ResponseFormatter.prisma().find_first()
    if formatter is None:
        raise ValueError("No ResponseFormatter found")
    return f'{{"message": "{message}"}}'


def HelloWorldEndpoint(request: HelloWorldRequestModel) -> HelloWorldResponseModel:
    """
    This endpoint returns a JSON response with the 'hello world' message. It calls the ResponseFormatter module to format the raw message into JSON format. No authentication is required.

    Args:
        request (HelloWorldRequestModel): The request model for the hello world endpoint. Since it's a simple GET request with no additional parameters, the fields are empty.

    Returns:
        HelloWorldResponseModel: The response model for the hello world endpoint, containing a single field for the 'hello world' message.

    Example:
        request = HelloWorldRequestModel()
        response = HelloWorldEndpoint(request)
        > HelloWorldResponseModel(message='{"message": "hello world"}')
    """
    loop = asyncio.get_event_loop()
    formatted_message = loop.run_until_complete(format_response("hello world"))
    return HelloWorldResponseModel(message=formatted_message)

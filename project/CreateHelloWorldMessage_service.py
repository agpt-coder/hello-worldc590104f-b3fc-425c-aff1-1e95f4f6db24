import prisma
import prisma.models
from pydantic import BaseModel


class HelloWorldMessageResponse(BaseModel):
    """
    The response model returns the formatted 'hello world' message.
    """

    formatted_message: str


async def CreateHelloWorldMessage(raw_message: str) -> HelloWorldMessageResponse:
    """
    This endpoint allows the creation of a new 'hello world' message. The raw message is expected in the request body.
    Although modifying the 'hello world' message is not common, this endpoint is provided for completeness.
    Only administrators can access this endpoint.

    Args:
        raw_message (str): The raw 'hello world' message to be formatted and saved.

    Returns:
        HelloWorldMessageResponse: The response model returns the formatted 'hello world' message.

    Example:
        await CreateHelloWorldMessage("Hello, World!")
        > HelloWorldMessageResponse(formatted_message="Hello, World!")
    """
    formatted_message = raw_message
    await prisma.models.HelloWorldModule.prisma().create(
        data={"name": "helloworld", "description": formatted_message}
    )
    return HelloWorldMessageResponse(formatted_message=formatted_message)

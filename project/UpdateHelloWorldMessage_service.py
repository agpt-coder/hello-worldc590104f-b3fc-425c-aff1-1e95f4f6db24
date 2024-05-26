import prisma
import prisma.models
from pydantic import BaseModel


class UpdateHelloWorldMessageResponse(BaseModel):
    """
    Response model for the 'hello world' message update. Acknowledges the update operation.
    """

    message: str
    status: str


async def UpdateHelloWorldMessage(message: str) -> UpdateHelloWorldMessageResponse:
    """
    This endpoint updates the 'hello world' message. It updates the entire message
    if it already exists. The raw message is expected in the request body.
    Only administrators can access this endpoint.

    Args:
    message (str): The new 'hello world' message.

    Returns:
    UpdateHelloWorldMessageResponse: Response model for the 'hello world' message update.
    Acknowledges the update operation.

    Example:
    updated_message = await UpdateHelloWorldMessage("New Hello World Message")
    print(updated_message.message)  # Output: "New Hello World Message"
    print(updated_message.status)  # Output: "updated" or "created"
    """
    hello_world_entry = await prisma.models.HelloWorldModule.prisma().find_first()
    if hello_world_entry:
        await prisma.models.HelloWorldModule.prisma().update(
            where={"id": hello_world_entry.id}, data={"description": message}
        )
        return UpdateHelloWorldMessageResponse(message=message, status="updated")
    else:
        await prisma.models.HelloWorldModule.prisma().create(
            data={"name": "hello_world_message", "description": message}
        )
        return UpdateHelloWorldMessageResponse(message=message, status="created")

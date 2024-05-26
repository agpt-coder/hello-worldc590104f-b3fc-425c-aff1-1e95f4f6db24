from typing import Optional

import prisma
import prisma.models
from pydantic import BaseModel


class DeleteHelloWorldRequest(BaseModel):
    """
    Request model for deleting the 'hello world' message. There are no additional fields needed for this endpoint.
    """

    pass


class DeleteHelloWorldResponse(BaseModel):
    """
    Response model for the delete operation on the 'hello world' message.
    """

    message: str


async def get_current_user_role(user_id: int) -> Optional[str]:
    """
    Retrieves the role of the current user from the database.

    Args:
        user_id (int): The ID of the user to check.

    Returns:
        Optional[str]: The role of the user (Admin or User) or None if the user is not found.

    Example:
        role = await get_current_user_role(5)
        > "Admin"
    """
    user = await prisma.models.User.prisma().find_unique(where={"id": user_id})
    return user.role.name if user else None


async def delete_hello_world_message() -> None:
    """
    Deletes the 'hello world' message from HelloWorldModule table.

    Returns:
        None

    Example:
        await delete_hello_world_message()
    """
    await prisma.models.HelloWorldModule.prisma().delete_many()


async def DeleteHelloWorldMessage(
    request: DeleteHelloWorldRequest,
) -> DeleteHelloWorldResponse:
    """
    This endpoint deletes the 'hello world' message. Although typically a 'hello world' message might not need deletion,
    this endpoint is included for completeness. Only administrators can access this endpoint.

    Args:
    request (DeleteHelloWorldRequest): Request model for deleting the 'hello world' message. There are no additional fields needed for this endpoint.

    Returns:
    DeleteHelloWorldResponse: Response model for the delete operation on the 'hello world' message.

    Example:
        request = DeleteHelloWorldRequest()
        response = await DeleteHelloWorldMessage(request)
    """
    user_id = 1
    role = await get_current_user_role(user_id)
    if role != "Admin":
        return DeleteHelloWorldResponse(
            message="Only administrators are allowed to delete the 'hello world' message."
        )
    await delete_hello_world_message()
    return DeleteHelloWorldResponse(message="'hello world' message has been deleted.")

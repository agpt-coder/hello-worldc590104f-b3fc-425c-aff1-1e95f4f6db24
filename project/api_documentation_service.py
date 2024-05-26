from datetime import datetime

import prisma
import prisma.models
from fastapi import HTTPException, status
from pydantic import BaseModel


class GetAPIDocumentationRequest(BaseModel):
    """
    The request model for the GET /api/documentation endpoint. This request does not require any parameters.
    """

    pass


class APIDocumentationResponse(BaseModel):
    """
    A response model that includes the necessary details regarding the API documentation for the 'hello world' endpoint.
    """

    id: int
    title: str
    description: str
    createdAt: datetime
    updatedAt: datetime


async def verify_administrator_role(user_id: int) -> bool:
    """
    Verifies if the user has an 'administrator' role.

    This function checks the user's role from the database to see if they possess administrator privileges.

    Args:
        user_id (int): The unique identifier of the user to verify.

    Returns:
        bool: True if the user is an administrator, False otherwise.

    Example:
        verify_administrator_role(1)
        > True
    """
    user = await prisma.models.User.prisma().find_first(where={"id": user_id})
    if user and user.role == "Admin":
        return True
    return False


async def api_documentation(
    request: GetAPIDocumentationRequest, user_id: int
) -> APIDocumentationResponse:
    """
    This endpoint provides detailed API documentation. It explains how to access the 'hello world' endpoint, including the request methods, expected responses, and any other relevant information. It will respond with a 200 status code and a JSON object containing the API documentation. This route is protected and can only be accessed by users with the 'administrator' role.

    Args:
        request (GetAPIDocumentationRequest): The request model for the GET /api/documentation endpoint. This request does not require any parameters.
        user_id (int): The unique identifier of the user making the request.

    Returns:
        APIDocumentationResponse: A response model that includes the necessary details regarding the API documentation for the 'hello world' endpoint.

    Example:
        user_id = 1
        api_documentation(GetAPIDocumentationRequest(), user_id)
        > APIDocumentationResponse(id=1, title='Hello World API', description='This is a hello world endpoint.', createdAt=datetime.now(), updatedAt=datetime.now())
    """
    is_admin = await verify_administrator_role(user_id)
    if not is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this resource.",
        )
    documentation = await prisma.models.APIDocumentation.prisma().find_first()
    if not documentation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="API documentation not found."
        )
    response = APIDocumentationResponse(
        id=documentation.id,
        title=documentation.title,
        description=documentation.description,
        createdAt=documentation.createdAt,
        updatedAt=documentation.updatedAt,
    )
    return response

from typing import List

from pydantic import BaseModel


class GetAPIDocumentationRequest(BaseModel):
    """
    The request model for the GET /api/documentation endpoint. This request does not require any parameters.
    """

    pass


class EndpointDocumentation(BaseModel):
    """
    Model representing the detailed documentation of an endpoint.
    """

    path: str
    method: str
    description: str
    request_model: str
    response_model: str
    roles_allowed: List[str]


class GetAPIDocumentationResponse(BaseModel):
    """
    Response model describing the detailed API documentation including available endpoints, request methods, expected responses, and permissible roles.
    """

    endpoints: List[EndpointDocumentation]


async def get_api_documentation(
    request: GetAPIDocumentationRequest,
) -> GetAPIDocumentationResponse:
    """
    This endpoint provides detailed documentation about the API, including how to access the 'hello world' endpoint.

    It leverages the information from the 'hello world' endpoint and User Management module to display comprehensive documentation.

    Args:
        request (GetAPIDocumentationRequest): The request model for the GET /api/documentation endpoint. This request does not require any parameters.

    Returns:
        GetAPIDocumentationResponse: Response model describing the detailed API documentation including available endpoints, request methods, expected responses, and permissible roles.
    """
    hello_world_doc = EndpointDocumentation(
        path="/api/hello-world",
        method="GET",
        description="Returns 'hello world'",
        request_model="None",
        response_model="{'message': 'hello world'}",
        roles_allowed=["Admin", "User"],
    )
    endpoints = [hello_world_doc]
    response = GetAPIDocumentationResponse(endpoints=endpoints)
    return response

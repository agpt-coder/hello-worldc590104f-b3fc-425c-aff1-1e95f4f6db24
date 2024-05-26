import logging
from contextlib import asynccontextmanager

import project.api_documentation_service
import project.CreateHelloWorldMessage_service
import project.DeleteHelloWorldMessage_service
import project.get_api_documentation_service
import project.get_hello_world_service
import project.getHelloWorld_service
import project.getHelloWorldMessage_service
import project.hello_world_service
import project.HelloWorldEndpoint_service
import project.UpdateHelloWorldMessage_service
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response
from prisma import Prisma

logger = logging.getLogger(__name__)

db_client = Prisma(auto_register=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_client.connect()
    yield
    await db_client.disconnect()


app = FastAPI(
    title="hello world",
    lifespan=lifespan,
    description='create a single api app. This api should just return "hello world"',
)


@app.get(
    "/api/documentation",
    response_model=project.get_api_documentation_service.GetAPIDocumentationResponse,
)
async def api_get_get_api_documentation(
    request: project.get_api_documentation_service.GetAPIDocumentationRequest,
) -> project.get_api_documentation_service.GetAPIDocumentationResponse | Response:
    """
    This endpoint provides detailed documentation about the API, including how to access the 'hello world' endpoint. The documentation includes available endpoints, request methods, expected responses, and the roles that have access to each endpoint. It leverages the information from the 'hello world' endpoint and User Management module to display comprehensive documentation.
    """
    try:
        res = await project.get_api_documentation_service.get_api_documentation(request)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.get(
    "/api/hello-world",
    response_model=project.get_hello_world_service.HelloWorldResponseModel,
)
async def api_get_get_hello_world(
    request: project.get_hello_world_service.HelloWorldRequestModel,
) -> project.get_hello_world_service.HelloWorldResponseModel | Response:
    """
    This endpoint returns a simple message 'hello world'. It does not require any input parameters or authentication, making it accessible to anyone. The returned response is a plain text message.
    """
    try:
        res = project.get_hello_world_service.get_hello_world(request)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.get("/hello", response_model=project.getHelloWorld_service.HelloWorldResponse)
async def api_get_getHelloWorld(
    request: project.getHelloWorld_service.HelloWorldRequest,
) -> project.getHelloWorld_service.HelloWorldResponse | Response:
    """
    This endpoint returns a JSON formatted 'hello world' message. It utilizes the ResponseFormatter module to ensure the message is returned in a standardized JSON format. When a client sends a GET request to this endpoint, the server will respond with a JSON object containing the key 'message' and value 'hello world'. This endpoint can be accessed by both administrators and users.
    """
    try:
        res = project.getHelloWorld_service.getHelloWorld(request)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.post(
    "/hello-world",
    response_model=project.CreateHelloWorldMessage_service.HelloWorldMessageResponse,
)
async def api_post_CreateHelloWorldMessage(
    raw_message: str,
) -> project.CreateHelloWorldMessage_service.HelloWorldMessageResponse | Response:
    """
    This endpoint allows the creation of a new 'hello world' message. The raw message is expected in the request body. Although modifying the 'hello world' message is not common, this endpoint is provided for completeness. Only administrators can access this endpoint.
    """
    try:
        res = await project.CreateHelloWorldMessage_service.CreateHelloWorldMessage(
            raw_message
        )
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.get(
    "/hello-world",
    response_model=project.HelloWorldEndpoint_service.HelloWorldResponseModel,
)
async def api_get_HelloWorldEndpoint(
    request: project.HelloWorldEndpoint_service.HelloWorldRequestModel,
) -> project.HelloWorldEndpoint_service.HelloWorldResponseModel | Response:
    """
    This endpoint returns a JSON response with the 'hello world' message. It calls the ResponseFormatter module to format the raw message into JSON format. No authentication is required.
    """
    try:
        res = project.HelloWorldEndpoint_service.HelloWorldEndpoint(request)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.delete(
    "/hello-world",
    response_model=project.DeleteHelloWorldMessage_service.DeleteHelloWorldResponse,
)
async def api_delete_DeleteHelloWorldMessage(
    request: project.DeleteHelloWorldMessage_service.DeleteHelloWorldRequest,
) -> project.DeleteHelloWorldMessage_service.DeleteHelloWorldResponse | Response:
    """
    This endpoint deletes the 'hello world' message. Although typically a 'hello world' message might not need deletion, this endpoint is included for completeness. Only administrators can access this endpoint.
    """
    try:
        res = await project.DeleteHelloWorldMessage_service.DeleteHelloWorldMessage(
            request
        )
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.get(
    "/api/hello", response_model=project.getHelloWorldMessage_service.HelloWorldResponse
)
async def api_get_getHelloWorldMessage(
    request: project.getHelloWorldMessage_service.HelloWorldRequest,
) -> project.getHelloWorldMessage_service.HelloWorldResponse | Response:
    """
    This endpoint returns a 'hello world' message in JSON format. When a GET request is made to this endpoint, it invokes the 'getHelloWorldMessage' function. This function interacts with the ResponseFormatter module to format the response correctly. The expected response is a JSON object containing a single key-value pair where the key is 'message' and the value is 'hello world'. No additional parameters are required for this request.
    """
    try:
        res = project.getHelloWorldMessage_service.getHelloWorldMessage(request)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.put(
    "/hello-world",
    response_model=project.UpdateHelloWorldMessage_service.UpdateHelloWorldMessageResponse,
)
async def api_put_UpdateHelloWorldMessage(
    message: str,
) -> project.UpdateHelloWorldMessage_service.UpdateHelloWorldMessageResponse | Response:
    """
    This endpoint updates the 'hello world' message. It updates the entire message if it already exists. The raw message is expected in the request body. Only administrators can access this endpoint.
    """
    try:
        res = await project.UpdateHelloWorldMessage_service.UpdateHelloWorldMessage(
            message
        )
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.get(
    "/api/hello-world",
    response_model=project.hello_world_service.HelloWorldResponseModel,
)
async def api_get_hello_world(
    request: project.hello_world_service.HelloWorldRequestModel,
) -> project.hello_world_service.HelloWorldResponseModel | Response:
    """
    This endpoint returns 'Hello World'. It is a public endpoint that can be accessed by anyone. Upon successful request, it will respond with a 200 status code and a plain text message saying 'Hello World'. No authentication is required.
    """
    try:
        res = project.hello_world_service.hello_world(request)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.get(
    "/api/documentation",
    response_model=project.api_documentation_service.APIDocumentationResponse,
)
async def api_get_api_documentation(
    request: project.api_documentation_service.GetAPIDocumentationRequest,
) -> project.api_documentation_service.APIDocumentationResponse | Response:
    """
    This endpoint provides detailed API documentation. It explains how to access the 'hello world' endpoint, including the request methods, expected responses, and any other relevant information. It will respond with a 200 status code and a JSON object containing the API documentation. This route is protected and can only be accessed by users with the 'administrator' role.
    """
    try:
        res = await project.api_documentation_service.api_documentation(request)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )

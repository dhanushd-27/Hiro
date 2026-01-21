import time
import uuid
import logging
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from fastapi import Request, Response

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app")

class LoggingMiddleware(BaseHTTPMiddleware):
  async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
    request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    request.state.request_id = request_id

    start_time = time.time()
    response = await call_next(request)
    duration = (time.time() - start_time) * 1000

    logger.info(
        "\n\t%s %s %s %.2fms\n"
        "\t%s",
        request.method,
        request.url.path,
        response.status_code,
        duration,
        request_id,
    )

    return response
import logging

from starlette.requests import Request
from starlette.middleware.base import BaseHTTPMiddleware

logging.basicConfig(
    filename="middlewear.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logger.info(f"Incoming request: {request.method} {request.url}")
        
        response = await call_next(request)

        logger.info(f"Response status: {response.status_code}")

        return response

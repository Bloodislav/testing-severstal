from fastapi import APIRouter
from core.config import settings
from .rolls import router as rolls_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(
    router=rolls_router,
    prefix=settings.api.v1.rolls,
)

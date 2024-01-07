"""Router for Basic Info"""
import time
from fastapi import APIRouter

router = APIRouter()

@router.get('/time')
async def get_time() -> dict:
    """Return time"""
    return {'time': time.time()}

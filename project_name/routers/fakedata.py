"""Router for fakedata"""
from fastapi import APIRouter
from project_name.services.fakegen import generate_job

router = APIRouter()

@router.get('/fakedata')
async def get_fakedata() -> dict:
    """Return fakedata"""
    return {'fakedata': generate_job(3)}

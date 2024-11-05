from fastapi import APIRouter, HTTPException
from redisClient.redis_client import redis_client

router = APIRouter(
    prefix="/redis",
    tags=["redis"]
)


@router.post("/test/")
async def redis_test(redis_key: str, redis_value: str):
    try:
        redis_client.setex(redis_key, 100, redis_value)
        return {"message": f"Key '{redis_key}' set with value '{redis_value}'"}
    except Exception as exception:
        raise HTTPException(status_code=500, detail=f"Redis error with message: {exception}")

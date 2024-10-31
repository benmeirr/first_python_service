from typing import Optional

from starlette import status
from fastapi import APIRouter
from api.externalApi.tvMaze import tv_maze_api
from api.externalApi.tvMaze.model.TvMazeShowResponse import TvMazeShowResponse

router = APIRouter(
    prefix="/tv_maze",
    tags=["tv_maze"]
)


@router.get("/show/{tv_maze_show_id}", status_code=status.HTTP_200_OK)
async def get_show_by_id(tv_maze_show_id: int) -> Optional[TvMazeShowResponse]:
    return await tv_maze_api.get_show_by_id(tv_maze_show_id)


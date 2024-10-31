from api.externalApi.tvMaze.model.TvMazeShowResponse import TvMazeShowResponse
from typing import Optional
from config.config import Config
import httpx

config = Config()


async def get_show_by_id(show_id: int) -> Optional[TvMazeShowResponse]:
    url = f"{config.TV_MAZE_API_BASE_URL}/shows/{show_id}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()

            data = response.json()

            tv_show_response = TvMazeShowResponse(
                tv_maze_show_id=data.get("id"),
                tv_maze_show_name=data.get("name"),
                tv_maze_show_url=data.get("url"),
                tv_maze_show_original_url=data.get("image", {}).get("original")
            )

            return tv_show_response

        except httpx.HTTPStatusError as exception:
            print(f"Can't fetch TV show with id: {show_id} with error: {exception.response}")
            return None

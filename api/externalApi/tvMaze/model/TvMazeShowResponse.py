from typing import Optional

from pydantic import BaseModel


class TvMazeShowResponse(BaseModel):
    tv_maze_show_id: int
    tv_maze_show_name: str
    tv_maze_show_url: str
    tv_maze_show_original_url: Optional[str] = None



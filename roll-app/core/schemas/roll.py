from pydantic import BaseModel
from datetime import date


class RollAddDTO(BaseModel):
    length: int
    weight: int


class RollDelDTO(BaseModel):
    id: int
    data_deleted: date


class RollDTO(BaseModel):
    id: int | None = None
    length: int | None = None
    weight: int | None = None
    data_added: date | None = None
    data_deleted: date | None = None


class RollStatDTO(BaseModel):
    count_add: int
    count_del: int
    mid_length: float
    mid_weight: float
    max_length: int
    min_length: int
    max_weight: int
    min_weight: int
    sum_length: int
    max_add_del: int
    min_add_del: int

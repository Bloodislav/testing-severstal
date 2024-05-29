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


class RollAverageValue(BaseModel):
    mid_length: int
    mid_weight: int


class RollMaxMin(BaseModel):
    max_length: int
    min_length: int
    max_weight: int
    min_weight: int
    max_add_del: int
    min_add_del: int


class RollStatDTO(BaseModel):
    count_add: int
    count_del: int
    ave_value: RollAverageValue
    max_min: RollMaxMin

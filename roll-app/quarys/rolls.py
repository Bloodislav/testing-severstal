from datetime import date
from typing import Any

from sqlalchemy import select, update, func
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Roll
from core.schemas.roll import RollAddDTO, RollDTO
from core.schemas.roll import RollStatDTO, RollAverageValue

async def create_roll(
    session: AsyncSession,
    roll_create: RollAddDTO
) -> Roll:
    """ Create roll in DB """
    roll = Roll(**roll_create.model_dump())
    session.add(roll)
    await session.commit()
    return roll


async def edit_one_roll(
    session: AsyncSession,
    id: int,
    data: dict
) -> Roll | None:
    """ Edit roll in DB """
    stmt = update(Roll).values(**data).filter_by(id=id).returning(Roll)
    res = await session.execute(stmt)
    await session.commit()
    roll = res.scalar()
    return roll


async def get_rolls(
    session: AsyncSession,
    filters: RollDTO,
    limit: int = 100
) -> Any:
    """ Create rolls in DB """
    filter_data = filters.model_dump()
    filter_data = {key: value for (key, value) in filter_data.items() if value}
    res = await session.execute(select(Roll).limit(limit=limit).filter_by(**filter_data))
    return res.scalars().all()


async def get_stats(
    session: AsyncSession,
    from_date: date,
    to_date: date,
):
   """ TODO """
   ...
   
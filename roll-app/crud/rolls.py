from datetime import date
from typing import Any

from sqlalchemy import select, update, func
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Roll
from core.schemas.roll import RollAddDTO, RollDTO
from core.schemas.roll import RollStatDTO

class RollCrud:
    @classmethod
    async def create_roll(self, session: AsyncSession, roll_create: RollAddDTO) -> Roll:
        """Create roll in DB"""
        try:
            roll = Roll(**roll_create.model_dump())
            session.add(roll)
            await session.commit()
            return roll
        except (SQLAlchemyError, Exception) as e:
            raise e

    @classmethod
    async def edit_one_roll(self, session: AsyncSession, id: int, data: dict) -> Roll | None:
        """Edit roll in DB"""
        try:
            stmt = update(Roll).values(**data).filter_by(id=id).returning(Roll)
            res = await session.execute(stmt)
            await session.commit()
            roll = res.scalar()
            return roll
        except (SQLAlchemyError, Exception) as e:
            raise e

    @classmethod
    async def get_rolls(self, session: AsyncSession, filters: RollDTO) -> Any:
        """Create rolls in DB"""
        try:
            filter_data = filters.model_dump()
            filter_data = {key: value for (key, value) in filter_data.items() if value}
            res = await session.execute(select(Roll).filter_by(**filter_data))
            return res.scalars().all()
        except (SQLAlchemyError, Exception) as e:
            raise e

    @classmethod
    async def get_stats(self, 
        session: AsyncSession,
        from_date: date,
        to_date: date,
    ):
        """TODO Сделать нормально"""
        try:
            stmt = select(
                func.count(Roll.data_added).label("count_add"),
                func.count(Roll.data_deleted).label("count_del"),
                (func.sum(Roll.length) / func.count(Roll.length)).label("mid_length"),
                (func.sum(Roll.weight) / func.count(Roll.weight)).label("mid_weight"),
                func.max(Roll.length).label("max_length"),
                func.min(Roll.length).label("min_length"),
                func.max(Roll.weight).label("max_weight"),
                func.min(Roll.weight).label("min_weight"),
                func.sum(Roll.length).label("sum_length"),
                func.max(Roll.data_deleted - Roll.data_added).label("max_add_del"),
                func.min(Roll.data_deleted - Roll.data_added).label("min_add_del"),
            ).filter(Roll.data_added>=from_date, Roll.data_added<=to_date)
            
            res = await session.execute(stmt)
            return res.mappings().first()
        except (SQLAlchemyError, Exception) as e:
            raise e

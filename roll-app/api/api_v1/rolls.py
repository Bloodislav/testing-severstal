from typing import Annotated, List
from datetime import datetime, timezone, date

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.schemas.roll import RollAddDTO, RollDTO, RollStatDTO
from crud.rolls import RollCrud

router = APIRouter(tags=["Рулоны"])

@router.post("", response_model=RollDTO)
async def create_roll(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    roll_create: RollAddDTO,
):
    """Add new roll"""
    user = await RollCrud.create_roll(session=session, roll_create=roll_create)
    return user


@router.patch("/{roll_id}", response_model=RollDTO)
async def del_roll(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    roll_id: int,
):
    """Del roll"""
    roll = await RollCrud.edit_one_roll(
        session=session,
        id=roll_id,
        data={"data_deleted": datetime.now(timezone.utc).date()},
    )
    return roll


@router.get("", response_model=List[RollDTO])
async def get_rolls(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    filters: Annotated[
        RollDTO,
        Depends(RollDTO),
    ],
):
    """Get rolls with limit"""
    result = await RollCrud.get_rolls(session=session, filters=filters)
    return result


@router.get("/stats", response_model=RollStatDTO)
async def get_statistic(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    from_date: date,
    to_date: date,
):
    """Get statistic"""
    """ TODO """
    result = await RollCrud.get_stats(session, from_date, to_date)
    return result

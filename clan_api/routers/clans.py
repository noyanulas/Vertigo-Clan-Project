from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from fastapi import Query

from clan_api.db.session import get_db
from clan_api.db.models import Clan
from clan_api.schemas.clan import ClanCreate, ClanOut

router = APIRouter(prefix="/clans", tags=["clans"])


@router.post("/", response_model=ClanOut)
def create_clan(payload: ClanCreate, db: Session = Depends(get_db)):
    clan = Clan(
        name=payload.name,
        region=payload.region,
    )
    db.add(clan)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Clan name already exists"
        )

    db.refresh(clan)
    return clan

@router.get("/", response_model=List[ClanOut])
def list_clans(db: Session = Depends(get_db)):
    return db.query(Clan).order_by(Clan.created_at.desc()).all()

@router.get("/search", response_model=list[ClanOut])
def search_clans(
    name: str = Query(..., min_length=3),
    db: Session = Depends(get_db),
):
    stmt = (
        select(Clan)
        .where(Clan.name.ilike(f"%{name}%"))
        .order_by(Clan.created_at.desc())
    )
    result = db.execute(stmt).scalars().all()
    return result


from uuid import UUID

@router.delete("/{clan_id}", status_code=204)
def delete_clan(clan_id: UUID, db: Session = Depends(get_db)):
    clan = db.get(Clan, clan_id)
    if not clan:
        raise HTTPException(status_code=404, detail="Clan not found")

    db.delete(clan)
    db.commit()

from fastapi import APIRouter, Depends, Query

from app.core.security import get_current_user
from app.shared.schemas.common import DomainPayload
from app.modules.rule.service import service

router = APIRouter(prefix="/Rule", tags=["Smart Rules Engine"], dependencies=[Depends(get_current_user)])


@router.get("/fetchruleall", name="API_GET_RULES")
async def get_rules(PageNumber: int = Query(1, ge=1), PageSize: int = Query(100, ge=1, le=5000)):
    return await service.execute("API_GET_RULES", f"/fetchruleall?PageNumber={PageNumber}&PageSize={PageSize}", action="list")


@router.post("/addnotificationrule", name="API_SAVE_RULE")
async def save_rule(payload: DomainPayload):
    return await service.execute("API_SAVE_RULE", "/addnotificationrule", action="create", payload=payload.model_dump())


@router.put("/updaterule", name="API_UPDATE_RULE")
async def update_rule(payload: DomainPayload):
    return await service.execute("API_UPDATE_RULE", "/updaterule", action="update", payload=payload.model_dump())


@router.get("/fetchrulebyunitid", name="API_GET_RULEBYUNITID")
async def get_rule_by_unit_id(unit_id: str | None = Query(None)):
    path = f"/fetchrulebyunitid?unit_id={unit_id}" if unit_id else "/fetchrulebyunitid"
    return await service.execute("API_GET_RULEBYUNITID", path)

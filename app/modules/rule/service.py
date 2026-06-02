from app.shared.service import DomainService
from app.modules.rule.repository import repository

service = DomainService("rule", repository)

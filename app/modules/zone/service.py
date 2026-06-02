from app.shared.service import DomainService
from app.modules.zone.repository import repository

service = DomainService("zone", repository)

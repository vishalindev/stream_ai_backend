from app.shared.service import DomainService
from app.modules.platformuser.repository import repository

service = DomainService("platformuser", repository)

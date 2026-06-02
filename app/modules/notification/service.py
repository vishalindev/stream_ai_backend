from app.shared.service import DomainService
from app.modules.notification.repository import repository

service = DomainService("notification", repository)

from app.shared.service import DomainService
from app.modules.admin.repository import employee_repository, plant_repository

employee_service = DomainService("employee", employee_repository)
plant_service = DomainService("plant", plant_repository)

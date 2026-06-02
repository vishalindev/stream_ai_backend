from app.shared.service import DomainService
from app.modules.camera.repository import repository

service = DomainService("camera", repository)

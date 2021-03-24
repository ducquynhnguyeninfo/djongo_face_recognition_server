from .brand_service import *
from .vehiclemodel_service import *
from .order_service import *

from order_manager.repositories.vehiclemodel_repository import VehicleModelRepository
from order_manager.repositories.order_repository import OrderRepository

brandRepo = BrandRepository()
vmRepo = VehicleModelRepository()
orderRepo = OrderRepository()

brandService = BrandService(repository=brandRepo)
vehicleModelService = VehicleModelService(repository=vmRepo)
orderService = OrderService(repository=orderRepo)
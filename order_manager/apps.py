from django.apps import AppConfig
# from order_manager.repositories.brand_repository import BrandRepository
# from order_manager.services.brand_service import BrandService


class OrderManagerConfig(AppConfig):
    # auto generate model uuid
    name = 'order_manager'
    print("this line of code run at the begins")
    
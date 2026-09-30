from fastapi import APIRouter


from app.api.routes import (
    database,
    health,
    home,
    products,
)





api_router = APIRouter()







# ------------------------------------------------------------
# HEALTH ROUTES
# ------------------------------------------------------------

api_router.include_router(

    health.router

)







# ------------------------------------------------------------
# DATABASE TEST ROUTES
# ------------------------------------------------------------

api_router.include_router(

    database.router

)







# ------------------------------------------------------------
# HOME PAGE ROUTES
# ------------------------------------------------------------

api_router.include_router(

    home.router

)







# ------------------------------------------------------------
# PRODUCT ROUTES
# ------------------------------------------------------------

api_router.include_router(

    products.router

)
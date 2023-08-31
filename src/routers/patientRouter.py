from fastapi import APIRouter

patient_router = APIRouter()

# GET /Patient
@patient_router.get("/Patient")
async def get_patient():
    return {}

# POST /Patient
@patient_router.post("/Patient")
async def create_patient():
    return {}

# PUT /Patient
@patient_router.put("/Patient")
async def update_patient():
    return {}

# DELETE /Patient
@patient_router.delete("/Patient")
async def delete_patient():
    return {}

from fastapi import FastAPI

app = FastAPI(
    title="AI-Powered Food Waste Reduction & Smart Donation Management System",
    description="Backend API for donation posting, smart matching, ML waste prediction, and route optimization.",
    version="0.1.0",
)


@app.get("/")
def health_check():
    return {"status": "ok", "service": "food-waste-donation-system-api"}


# Routers will be included here as they're built, e.g.:
# from app.routes import auth, donations, matching
# app.include_router(auth.router, prefix="/auth", tags=["auth"])
# app.include_router(donations.router, prefix="/donations", tags=["donations"])

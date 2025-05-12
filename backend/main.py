# backend/main.py

from fastapi import FastAPI
from routes import dashboard, zodiac_routes, human_design_routes, mbti_routes, summary_routes, user_routes, profile_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="The Relationship Ledger API",
    version="0.1.0",
    description="Backend API for personality & relationship insight engine"
)

# Optional: CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(dashboard.router, prefix="/main")
app.include_router(zodiac_routes.router, prefix="/analysis")
app.include_router(human_design_routes.router, prefix="/analysis") 
app.include_router(mbti_routes.router, prefix="/analysis")
app.include_router(summary_routes.router, prefix="/analysis")
app.include_router(user_routes.router, prefix="/user")
app.include_router(profile_routes.router, prefix="/profile")

# ✅ Optional entrypoint for direct running
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

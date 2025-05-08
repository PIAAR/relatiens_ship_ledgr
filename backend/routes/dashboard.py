# backend/routes/dashboard.py

from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.get("/dashboard", tags=["Dashboard"])
async def get_dashboard_status():
    """
    Returns general system status and placeholder data for the Relationship Ledger dashboard.
    """
    return {
        "project": "The Relationship Ledger",
        "version": "0.1.0",
        "status": "online",
        "timestamp": datetime.utcnow().isoformat(),
        "available_modules": [
            "Astrology Report",
            "MBTI Analysis (coming soon)",
            "Human Design Engine (coming soon)",
            "Summary Blender",
        ],
        "next_actions": [
            "Connect frontend UI",
            "Implement MBTI route",
            "Complete onboarding flow",
        ]
    }


"""ClaimSage API application."""

from fastapi import FastAPI

app = FastAPI(
    title="ClaimSage API",
    description="Secure AI assistant for insurance employees.",
    version="0.1.0",
)


@app.get("/health/live", tags=["Health"])
def liveness_check() -> dict[str, str]:
    """Report whether the API process is running."""
    return {
        "status": "ok",
        "service": "claimsage-api",
    }

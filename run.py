import uvicorn
from app.database import Base, engine

if __name__ == "__main__":
    Base.metadata.create_all(engine)

    uvicorn.run(
        "app:app",
        port=8000,
        reload=True,
        use_colors=True
    )

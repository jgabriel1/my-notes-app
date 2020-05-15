import uvicorn
from app.database import Base, engine
from app.database.models import User, Note

if __name__ == "__main__":
    Base.metadata.create_all(engine)

    uvicorn.run(
        "app:app",
        port=8000,
        reload=True,
        use_colors=True
    )

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": (
            "Tutorial for combining workflow steps to "
            + "a Composite Actions."
        )
    }

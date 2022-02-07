import uvicorn
from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.openapi.utils import get_openapi
from app.helpers.file_helper import checkValidExtensions, readPointsFile
from app.services.interpolation_service import getInterpolatedPoints

app = FastAPI()

@app.get('/', tags=['Base'])
async def root() -> dict:
    return {'message': 'Hello World'}

@app.post('/upload/points', tags=['Upload'])
async def uploadfile(file: UploadFile) -> dict:
    if not checkValidExtensions(file.filename):
        raise HTTPException(status_code=400, detail="File extension is not .txt or .las")
    
    points = readPointsFile(file)
    interpolated = getInterpolatedPoints(points[:, 0], points[:, 1], points[:, 2])

    return {'filename': file.filename}

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Open Interpolation API",
        version="0.1.0",
        description="Open API for interpoation with any (n, 3) point clouds",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080, reload=True)

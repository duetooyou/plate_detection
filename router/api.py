import base64
import io
from fastapi import UploadFile, File
from fastapi.routing import APIRouter
from models import OutputNeural
from PIL import Image

router = APIRouter(prefix='/api',
                   tags=['api'])


@router.post('/detection/', response_model=OutputNeural)
async def detection(image: UploadFile = File(...)):
    buffer = io.BytesIO()
    img = Image.open(io.BytesIO(await image.read()))
    img.save(buffer, "JPEG")
    buffer.seek(0)
    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return {'plate': image.filename, 'img_str': img_str}

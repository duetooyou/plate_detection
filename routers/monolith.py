import base64
import io
from PIL import Image
from fastapi import UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRouter
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")
router = APIRouter(prefix='/monolith',
                   tags=['monolith'])


@router.get('/home/', response_class=HTMLResponse)
async def hello_world(request: Request):
    return templates.TemplateResponse('home.html', {'request': request,
                                                    'result': None})


@router.post('/home/', response_class=HTMLResponse)
async def form_post(request: Request, image: UploadFile = File(...)):
    buffer = io.BytesIO()
    img = Image.open(io.BytesIO(await image.read()))
    img.save(buffer, "JPEG")
    buffer.seek(0)
    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # np_image = np.array(Image.open(io.BytesIO(await image.read())))
    # result_image, plate_name = final_detect(np_image, MODEL_PLATES, MODEL_CHARS, FONT_PATH)
    # my_img = Image.fromarray(result_image)
    # buffer = io.BytesIO()
    # my_img.save(buffer, format='JPEG')
    # buffer.seek(0)
    return templates.TemplateResponse('home.html', {'request': request,
                                                    'result': img_str})

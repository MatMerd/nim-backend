from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.config import BASE_DIR


router = APIRouter(prefix="/pages", tags=["Pages"])

templates = Jinja2Templates(
    directory=BASE_DIR / "templates",
)


@router.get("/base")
def get_base_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("base.jinja", {"request": request})


@router.get("/calendar")
def get_calendar_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("calendar/calendar.jinja", {"request": request})

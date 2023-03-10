from __future__ import annotations

import os
import textwrap
from io import BytesIO

from django.http import HttpResponse
from django.views.generic import View
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# O'zgartiring kerakli fontga
FONT_PATH = os.path.join(BASE_DIR, 'fonts/arial.ttf')
# O'zgartiring sertifikat rasmingizni joylashuvi
CERT_PATH = os.path.join(BASE_DIR, 'certificates/certificate.png')


class CertificateView(View):
    def get(self, request):
        # Ism va familiyani so'radi va sertifikat rasmini yaratadi
        name = request.GET.get('name', '')
        img = Image.open(CERT_PATH).convert('RGBA')

        # Sertifikat rasmining oldindan yuklab olib, o'lchamini aniqlash
        width, height = img.size

        # Matnni yozish uchun fontni belgilash
        font = ImageFont.truetype(FONT_PATH, 50)

        # Matnning joylashuvi va shaklini belgilash
        draw = ImageDraw.Draw(img)
        text_width, text_height = draw.textsize(name, font)
        x = (width - text_width) / 2
        y = height * 0.75

        # Matnni sertifikatga yozish
        draw.text((x, y), name, font=font, fill=(0, 0, 0, 255))

        # So'nggi qadam, Sertifikat rasmini HTTP yanada nusxaga o'tkazish
        response = HttpResponse(content_type='image/png')
        img.save(response, 'PNG')
        return response

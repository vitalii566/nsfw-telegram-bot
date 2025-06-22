
from telegram import InputFile
from io import BytesIO

def get_input_file():
    # Пример возврата файла в памяти
    image_data = BytesIO()
    image_data.write(b"GIF89a\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02L\x01\x00;")
    image_data.seek(0)
    return InputFile(image_data, filename="nsfw.gif")

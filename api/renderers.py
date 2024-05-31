from io import BytesIO
from PIL import Image
from rest_framework import renderers

class ImageRenderer(renderers.BaseRenderer):
    media_type = 'image/png'
    format = 'PNG'
    charset = None
    render_style = 'binary'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if isinstance(data, Image.Image):
            image_io = BytesIO()
            data.save(image_io, format=self.format)
            return image_io.getvalue()
        return data
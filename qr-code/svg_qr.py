import qrcode
from qrcode import image
import qrcode.image.svg

def gen_qr_svg(text = "https://linklerz.xyz/"):
    factory = qrcode.image.svg.SvgPathImage
    svg_img = qrcode.make(text, image_factory=factory)

    svg_img.save("svg_qr.svg")


gen_qr_svg("https://linklerz.xyz/")
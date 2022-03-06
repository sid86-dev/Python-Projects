import threading
from main import*
from svg_qr import*


t1 = threading.Thread(target=gen_qr)
t2 = threading.Thread(target=gen_qr_svg)

t1.start()
t2.start()

t1.join()
t2.join()
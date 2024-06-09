import subprocess
import sys
import os
from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

script_dir = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = os.path.join(script_dir, "assets", "frame1")

def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)

def voltar():
    args = [sys.executable, str(OUTPUT_PATH / "encomendas_pesquisa_i.py")]
    subprocess.run(args)

window = Tk()

window.geometry("950x680")
window.configure(bg = "#FFFFFF")
window.title("Sistema de Condomínio")


canvas = Canvas( window, bg = "#FFFFFF", height = 680, width = 950, bd = 0, highlightthickness = 0, relief = "ridge")

canvas.place(x = 0, y = 0)
canvas.create_text( 559.0, 70.0, anchor="nw", text="retirada", fill="#8EBC4F", font=("BeVietnamPro SemiBold", 45 * -1))
canvas.create_text( 64.0, 70.0, anchor="nw", text="entrega", fill="#8EBC4F", font=("BeVietnamPro SemiBold", 45 * -1))
canvas.create_text( 782.0, 21.0, anchor="nw", text="encomendas", fill="#B9B9B9", font=("BeVietnamPro Light", 19 * -1))

button_image_2 = PhotoImage( file=relative_to_assets("button_2.png"))
button_2 = Button( image=button_image_2, borderwidth=0, highlightthickness=0, command=voltar, relief="flat")
button_2.place( x=34.0, y=33.0, width=30.0, height=15.0)


#entrada nome retirada
canvas.create_text( 562.0, 133.0, anchor="nw", text="nome:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image( 718.0, 170.66262912750244, image=entry_image_1)
entry_1 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_1.place( x=571.0, y=155.0, width=294.0, height=29.325258255004883)

#entrada cpf retirada
canvas.create_text( 562.0,192.0,anchor="nw", text="cpf:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_2 = PhotoImage( file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image( 670.0, 229.66262912750244, image=entry_image_2)
entry_2 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_2.place( x=571.0, y=214.0, width=198.0, height=29.325258255004883)

#entrada bloco retirada
canvas.create_text(562.0, 251.0, anchor="nw" ,text="bloco:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_3 = PhotoImage( file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image( 639.5, 288.66262912750244, image=entry_image_3)
entry_3 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_3.place( x=571.0, y=273.0, width=137.0, height=29.325258255004883)

#entrada porteiro retirada
canvas.create_text( 562.0, 310.0, anchor="nw", text="porteiro:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_4 = PhotoImage( file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image( 645.0, 347.66262912750244, image=entry_image_4)
entry_4 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_4.place( x=571.0, y=332.0, width=148.0, height=29.325258255004883)

#entrada apartamento retirada
canvas.create_text( 737.0, 251.0, anchor="nw", text="apartamento:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_5 = PhotoImage( file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image( 814.5, 288.66262912750244, image=entry_image_5)
entry_5 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_5.place( x=746.0, y=273.0, width=137.0, height=29.325258255004883)

#entrada data retirada
canvas.create_text( 562.0, 370.0, anchor="nw", text="data:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_6 = PhotoImage( file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image( 645.0, 407.66262912750244, image=entry_image_6)
entry_6 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_6.place( x=571.0, y=392.0, width=148.0, height=29.325258255004883)


#entrada nome entrega
canvas.create_text( 64.0, 133.0, anchor="nw", text="nome:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_11 = PhotoImage( file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image( 220.0, 170.66262912750244, image=entry_image_11)
entry_11 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_11.place(  x=73.0, y=155.0, width=294.0, height=29.325258255004883)

#entrada bloco entrega
canvas.create_text( 64.0, 193.0, anchor="nw", text="bloco:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_9 = PhotoImage( file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image( 141.5, 230.66262912750244, image=entry_image_9)
entry_9 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_9.place( x=73.0, y=215.0, width=137.0, height=29.325258255004883)

#entrada apartamento entrega
canvas.create_text( 239.0, 193.0, anchor="nw", text="apartamento:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_10 = PhotoImage( file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image( 316.5, 230.66262912750244, image=entry_image_10)
entry_10 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_10.place( x=248.0, y=215.0, width=137.0,  height=29.325258255004883)

#entrada data entrega
canvas.create_text( 64.0, 253.0, anchor="nw", text="data:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_7 = PhotoImage( file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image( 141.5, 290.66262912750244, image=entry_image_7)
entry_7 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_7.place( x=73.0, y=275.0, width=137.0, height=29.325258255004883)

#entrada porteiro entrega
canvas.create_text( 64.0, 310.0, anchor="nw", text="porteiro:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_8 = PhotoImage( file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image( 139.5, 347.66262912750244, image=entry_image_8)
entry_8 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_8.place( x=71.0, y=332.0, width=137.0, height=29.325258255004883)

#button salvar
button_image_1 = PhotoImage( file=relative_to_assets("button_1.png"))
button_1 = Button( image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"), relief="flat")
button_1.place( x=562.0, y=437.0, width=77.0, height=34.890625)

window.resizable(False, False)
window.mainloop()

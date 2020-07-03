import tkinter as tk
from time import sleep
qntr =0 
ml = 0 
toma = 0
meta = 0 

# width = Largura 
# height = altura

tconf = tk.Tk()
def quit():
    global tconf
    tconf.quit()

def confirm(a):
    global meta
    try: 
        meta = int(a)
    except:

        aviso = tk.Label(frame,text = 'VALOR INVÁLIDO DIGITE NOVAMENTE!', fg = 'white', bg = '#4682B4')
        aviso.place(relx =0, rely = 0.75, relheight = 0.25, relwidth = 1)
    else:
        tconf.destroy()

canvas = tk.Canvas(tconf, height = 150, width = 400)
canvas.pack()

back = tk.PhotoImage(file = 'waterbg.png')
back_label = tk.Label(tconf, image = back)
back_label.place(relwidth = 1, relheight = 1)

frame = tk.Frame(bg = '#4682B4')
frame.place(relx = 0.05, rely = 0.1, relwidth = 0.91, relheight = 0.8)

info = tk.Label(frame, bg = '#4682B4', text = 'PONHA SUA META DIARIA A BAIXO (EM ML): ', fg= 'white', font = 40)
info.place(relx = 0, rely = 0.1, relwidth = 1, relheight = 0.25)


metaintp = tk.Entry(frame,font = 15)
metaintp.place(relx = 0.05, rely = 0.4, relwidth = 0.25, relheight = 0.25)



bttn = tk.Button(text = 'CONFIRMAR', command = lambda: confirm(metaintp.get()))
bttn.place(relx = 0.4, rely = 0.43, relwidth = 0.25, relheight = 0.2)

tconf.mainloop()





def count(qnt):
    global toma, qntr
    try:
        qntr = int(qnt)
    except:
        pass
    else:
        toma += qntr
        frame_info_info = tk.Label(frame_info, fg = 'white', bg = '#1E90FF', text = f'VOCE JA TOMOU: {toma} Mls', font = 10)
        frame_info_info.place(relx = 0.05, rely = 0.1, relwidth = 0.9, relheight = 0.2)
        if int(toma) >= meta:
            check_label1 = tk.Label(frame2, image = check)
            check_label1.place(relx = 0.25, rely = 0.05, relwidth = 0.5, relheight = 0.5)
tela = tk.Tk()

check = tk.PhotoImage(file = 'concluido.png')

canvatyu = tk.Canvas(height = 400, width = 350)
canvatyu.pack()

back1 = tk.PhotoImage(file = 'waterbg.png')
back_label1 = tk.Label(tela, image = back1)
back_label1.place(relwidth = 1, relheight = 1)


frame2 = tk.Label(tela,bg = '#f0f0f0')
frame2.place(relx = 0.1, rely = 0.05, relheight = 0.9, relwidth = 0.8)

copo = tk.PhotoImage(file = 'copo.png')
copo_label = tk.Label(frame2, image = copo)
copo_label.place(relx = 0.25, rely = 0.05, relwidth = 0.5, relheight = 0.5)

frame_info = tk.Label(frame2, bg = '#4682B4')
frame_info.place(relx = 0.05, rely = 0.55, relheight = 0.4, relwidth = 0.9)

frame_info_info = tk.Label(frame_info, fg = 'white', bg = '#1E90FF', text = f'VOCE JA TOMOU: {toma} Mls', font = 10)
frame_info_info.place(relx = 0.05, rely = 0.1, relwidth = 0.9, relheight = 0.2)

addintp = tk.Entry(frame_info,bg = 'white', font = 10)
addintp.place(relx = 0.35, rely = 0.4, relwidth = 0.25, relheight = 0.2)

addbttn = tk.Button(frame_info,text = 'ADICIONAR',command = lambda: count(addintp.get()))
addbttn.place(relx = 0.28, rely = 0.7, relwidth = 0.4,relheight = 0.2)
tela.mainloop()
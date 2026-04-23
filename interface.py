import tkinter as tk
from tkinter import messagebox

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from airport import *

lista_trabajo = []


def btn_cargar_click():
    global lista_trabajo
    lista_trabajo = LoadAirports("Airports.txt")
    actualizar_pantalla()
    messagebox.showinfo("Cargar", "Datos cargados correctamente")

def btn_anadir_click():
    c = entrada_cod.get().upper()
    lat = entrada_lat.get()
    lon = entrada_lon.get()
    if c != "":
        try:
            lat=float(lat)
            lon=float(lon)
            nuevo = Airport(c, lat, lon)
            AddAirport(lista_trabajo, nuevo)
            actualizar_pantalla()
        except ValueError:
            messagebox.showerror("Error", "Porfavor, introduzca numeros entero. Gracias :)")


def btn_borrar_click():
    c = entrada_cod.get().upper()
    RemoveAirport(lista_trabajo, c)
    actualizar_pantalla()

def btn_guardar_click():
    SaveSchengenAirports(lista_trabajo, "Schengen_Only.txt")
    messagebox.showinfo("Guardar", "Archivo Schengen_Only.txt creado")

def actualizar_pantalla():
    caja.delete(1.0, tk.END)
    for a in lista_trabajo:
        SetSchengen(a)
        res = "SI" if a.schengen else "NO"
        caja.insert(tk.END, f"Cod: {a.code} | Lat: {a.lat} | Lon: {a.lon} | Schengen: {res}\n")


canvas_picture = None
def mostrar_grafico():
    global canvas_picture
    if not lista_trabajo:
        from tkinter import messagebox
        messagebox.showwarning("AVISO", "CARGA EL ARCHIVO PARA GENERAR EL GRÁFICO")
        return

    fig = PlotAirports(lista_trabajo)

    if canvas_picture is not None:
        canvas_picture.grid_forget()

    canvas_obj = FigureCanvasTkAgg(fig, master=root)
    canvas_obj.draw()  # [cite: 44]

    canvas_picture = canvas_obj.get_tk_widget()

    canvas_picture.config(width=600, height=400)
    canvas_picture.grid(row=1, column=1, rowspan=2, padx=5, pady=5, sticky=tk.N+tk.S+tk.E+tk.W)

#######################DISEÑO INTERFAZ###################
root = tk.Tk()
root.title('Airport')
root.geometry("1000x800")


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=10)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)


button_pictures_frame = tk.LabelFrame(root, text='Acciones')
button_pictures_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N+tk.S+tk.E+tk.W)


button_pictures_frame.columnconfigure(0, weight=1)
button_pictures_frame.rowconfigure(0, weight=1)
button_pictures_frame.rowconfigure(1, weight=1)


btn_cargar = tk.Button(button_pictures_frame, text="Cargar Archivo", command=btn_cargar_click)
btn_cargar.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N+tk.S+tk.E+tk.W)

btn_guardar = tk.Button(button_pictures_frame, text="Guardar Schengen", command=btn_guardar_click)
btn_guardar.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N+tk.S+tk.E+tk.W)


input_frame = tk.LabelFrame(root, text='Datos Aeropuerto')
input_frame.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N+tk.S+tk.E+tk.W)

tk.Label(input_frame, text="ICAO:").pack()
entrada_cod = tk.Entry(input_frame)
entrada_cod.pack(fill="x", padx=5)

tk.Label(input_frame, text="Lat:").pack()
entrada_lat = tk.Entry(input_frame)
entrada_lat.pack(fill="x", padx=5)

tk.Label(input_frame, text="Lon:").pack()
entrada_lon = tk.Entry(input_frame)
entrada_lon.pack(fill="x", padx=5)

btn_add = tk.Button(input_frame, text="Añadir", command=btn_anadir_click)
btn_add.pack(pady=5)


caja = tk.Text(root, height=10)
caja.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)


grafico_frame = tk.LabelFrame(root, text='Gráficas')
grafico_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)


btn_ver_grafico = tk.Button(grafico_frame, text="Generar Gráfico",
                            command=mostrar_grafico)
btn_ver_grafico.grid(row=0, column=0, pady=5)

root.mainloop()
from matplotlib.pyplot import plot

class Aircraft:
    def __init__(self, aircraft, company, origin, time):
        self.aircraft= aircraft #string
        self.company= company #3 letras ICAO code
        self.origin= origin #4 letras ICAO code
        self.time= time #formato hh:mm

def LoadArrivals(filename):
    lista_arrivals= []
    try:
        f= open(filename,"r")
        lineas = f.readlines()
        f.close()

        i=1
        while i < len(lineas):
            partes = lineas[i].split()
            if len(partes)==4:
                aircraft = partes[0]
                origin = partes[1]
                time = partes[2]
                company = partes[3]
                if ':' in time:
                    nuevo= Aircraft(aircraft, company, origin, time)
                    lista_arrivals.append(nuevo)
            i=i+1

    except FileNotFoundError:
        print("No se encontro el archivo:", filename)
        return []
    return lista_arrivals

#mis_vuelos = LoadArrivals("arrivals.txt")??

def PlotArrivals (aircrafts):

    if len(aircrafts) == 0:
        print("No existeix la llista")
        return

    import matplotlib.pyplot as pyplot
    Vx = range(24)  # hores
    Vy = [] * 24  # arribades/hora
    i = 0
    while i < len(aircrafts): #el while para formar la función
        fila = aircrafts[i] #cojo una fila
        tiempo= fila.time #al definirlo como clase el aircraft, cojo solo el atributo de time, con el fila.time
        partes = tiempo.split(":") #parto el time, pero con el : diviendolo

        hlanding = int(partes[0]) #aqui ya defino lo que seria la hora de aterrizaje

        Vy[hlanding] = Vy[hlanding] + 1 #ponemos la hroa en su casila
        i = i + 1

        pyplot.title("Frecuencia de aterrizajes por hora")
        pyplot.ylabel("Número de aviones")
        pyplot.xlabel("Hora del día")
        pyplot.bar(Vx,Vy)
        pyplot.show()

def SaveFlights(aircrafts, filename):
    if len(aircrafts) == 0:
        print("No existeix la llista")
        return False
    try:
        out = open(filename, 'w')
        out.write("Aircraft\tOrigin\tTime\tCompany\n") #la cabecera del .txt
        i = 0
        while i < len(aircrafts):
            fila = aircrafts[i]

            aircraft = fila.aircraft
            origin = fila.origin
            arrival = fila.time
            airline = fila.company

            if aircraft == "":
                aircraft = "-"
            if origin == "":
                origin = "-"
            if arrival == "":
                arrival = "-"
            if airline == "":
                airline = "-"
            out.write(aircraft + "\t" + origin + "\t" + arrival + "\t" + airline + "\n")

            i = i + 1

        out.close()
        return True
    except FileNotFoundError:
        print("No existeix la llista")


def PlotAirlines (aircrafts):
        if len(aircrafts) == 0:
            print("No existeix la llista")
            return

        import matplotlib.pyplot as pyplot
        Vx = []  # aerolinies
        Vy = []  # nº vols
        i = 0
        while i < len(aircrafts):
            fila = aircrafts[i]
            airline = fila.company
            if airline not in Vx:
                Vx.append(airline)
                Vy.append(1)
            else:
                encontrado = False
                x = 0
                while not encontrado and x < len(Vx):
                    if Vx[x] == airline:
                        encontrado = True
                    else:
                        x = x + 1
                if encontrado:
                    Vy[x] = Vy[x] + 1
            i=i+1

                    # també es podría fer amb pos=airlines.index("airline") (??)

        pyplot.bar(Vx,Vy)
        pyplot.xlabel("Aerolíneas")
        pyplot.ylabel("Número de vuelos")
        pyplot.show()


def PlotFlightsType(aircrafts):

    if len(aircrafts)>0:
        import matplotlib.pyplot as pyplot
        schengen = 0 #contadores schengen vs no schengen
        no_schengen = 0

        schengen_codes = ['LO', 'EB', 'LK', 'LC', 'EK', 'EE', 'EF', 'LF', 'ED', 'LG', 'EH', 'LH',
                    'BI', 'LI', 'EV', 'EY', 'EL', 'LM', 'EN', 'EP', 'LP', 'LZ', 'LJ', 'LE', 'ES', 'LS']

        i = 0
        while i < len(aircrafts):
            fila=aircrafts[i] #selecciono una fila
            origen = fila.company #cojo el icao ej: LEBL
            inicio= origen[0:2] #lo mismo que V1, cogiendo LE
            encontrado = False
            j = 0
            while j < len(schengen_codes) and not encontrado: #misma busqueda que version 1
                if schengen_codes[j] == inicio:
                    encontrado = True
                j = j + 1

            if schengen == True:
                schengen = schengen + 1
            else:
                no_schengen = no_schengen + 1

            i = i + 1

        plot.bar(['Vuelos'], [schengen])
        plot.bar(['Vuelos'], [no_schengen])

        plot.title("Vuelos Schengen vs No Schengen")
        plot.show()

    else:
        print("Error: No hay vuelos.")
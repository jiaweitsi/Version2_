def MapFlights(aircrafts, airports):
    if len(aircrafts) > 0:
        f = open("FlightsMap.kml", "w")

        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
        f.write('<Document>\n')

        lon_lebl = "2.0784"
        lat_lebl = "41.2974"

        i = 0
        while i < len(aircrafts):
            vuelo = aircrafts[i]


            pos_aeropuerto = -1
            j = 0
            while j < len(airports):
                if airports[j].code == vuelo.origin:
                    pos_aeropuerto = j
                j = j + 1

            if pos_aeropuerto != -1:
                ap_origen = airports[pos_aeropuerto]

                prefijos_s = ['LO', 'EB', 'LK', 'LC', 'EK', 'EE', 'EF', 'LF', 'ED', 'LG', 'EH', 'LH', 'BI', 'LI', 'EV',
                              'EY', 'EL', 'LM', 'EN', 'EP', 'LP', 'LZ', 'LJ', 'LE', 'ES', 'LS']
                color = "red"

                k = 0
                while k < len(prefijos_s):
                    if ap_origen.code[0:2] == prefijos_s[k]:
                        color = "blue"
                    k = k + 1

                f.write('<Placemark>\n')
                f.write('  <name>' + vuelo.id + '</name>\n')
                f.write('  <Style><LineStyle><color>' + color + '</color><width>2</width></LineStyle></Style>\n')
                f.write('  <LineString>\n')
                f.write('    <coordinates>\n')
                f.write(f"      {ap_origen.lon},{ap_origen.lat},0\n")
                f.write(f"      {lon_lebl},{lat_lebl},0\n")
                f.write('    </coordinates>\n')
                f.write('  </LineString>\n')
                f.write('</Placemark>\n')

            i = i + 1

        f.write('</Document>\n')
        f.write('</kml>\n')
        f.close()
        print("Archivo FlightsMap.kml generado correctamente.")
    else:
        print("Error: No hay vuelos para mapear.")


import math


def CalcularDistancia(lat1, lon1, lat2, lon2):
    r = 6371.0

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distancia = r*c
    return distancia


def LongDistanceArrivals(aircrafts, airports, lista_lejanos):
    lat_lebl = 41.2974
    lon_lebl = 2.0784

    if len(aircrafts) > 0:
        i = 0
        while i < len(aircrafts):
            vuelo = aircrafts[i]

            pos_ap = -1
            j = 0
            while j < len(airports):
                if airports[j].code == vuelo.origin:
                    pos_ap = j
                j = j + 1

            if pos_ap != -1:
                ap_origen = airports[pos_ap]

                d = CalcularDistancia(ap_origen.lat, ap_origen.lon, lat_lebl, lon_lebl)

                if d > 2000:
                    lista_lejanos.append(vuelo)

            i = i + 1
    else:
        print("Error: No hay vuelos cargados.")

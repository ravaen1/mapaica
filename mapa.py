
import folium
import webbrowser

# Crea un objeto mapa centrado en una ubicación específica
mapa = folium.Map(location=[-14.048148, -75.739941], zoom_start=12)

# Agrega un marcador en la misma ubicación
folium.Marker(location=[-14.076831, -75.748412], popup="ubicacion de referencia!!").add_to(mapa)


# Guarda el mapa en un archivo HTML
mapa.save('mapa.html')

# Abre el archivo HTML en el navegador predeterminado del usuario
webbrowser.open('mapa.html')

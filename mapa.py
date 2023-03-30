
import folium
import webbrowser

# Crea un objeto mapa centrado en una ubicación específica
mapa = folium.Map(location=[-14.048148, -75.748584], zoom_start=12)

# Guarda el mapa en un archivo HTML
mapa.save('mapa.html')

# Abre el archivo HTML en el navegador predeterminado del usuario
webbrowser.open('mapa.html')

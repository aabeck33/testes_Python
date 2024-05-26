import folium as fl
from folium import plugins
import json
import jinja2
from folium.map import Marker

LOCATION_CENTER = [0,-60]
ZOOM = 4
lista_locais = json.load(open(".\mapas\lista_enderecos.json", "r")) #Codificação ANSI para ajustar os caracteres especiais.

def construct_map(mapa):
    fl.TileLayer('openstreetmap').add_to(mapa)
    fl.TileLayer('stamenterrain').add_to(mapa)
    fl.TileLayer('stamentoner').add_to(mapa)
    fl.TileLayer('stamenwatercolor').add_to(mapa)
    fl.TileLayer('cartodbpositron').add_to(mapa)
    fl.TileLayer('cartodbdark_matter').add_to(mapa)

    ff_group = fl.FeatureGroup(name="F&F",overlay=True).add_to(mapa)
    ind_group = fl.FeatureGroup(name="Industrial",overlay=True).add_to(mapa)
    agro_group = fl.FeatureGroup(name="Agro",overlay=True).add_to(mapa)
    adm_group = fl.FeatureGroup(name="Adm",overlay=True).add_to(mapa)

    for local in lista_locais:
        localiza = (str(local['Latitude']),str(local['Longitude']))
        endereco = f"{local['Rua']},+{str(local['Numero'])}+-+{local['Bairro']},+{local['Cidade']},+{local['Estado']},+{str(local['CEP'])}/@{str(local['Latitude'])},{str(local['Longitude'])}"
        googlemaps = f"https://www.google.com/maps/place/{endereco.replace(' ', '+')}"
        if 'F&F' in local['Nome 1']:
            cor = 'blue'
            icone = 'fa-truck'
            layer_group = ff_group
        elif 'Administrativo' in local['Nome 1']:
            cor = 'orange'
            icone = 'fa-building'
            layer_group = adm_group
        elif 'AGRO' in local['Nome 1']:
            cor = 'green'
            icone = 'fa-leaf'
            layer_group = agro_group
        else:
            cor = 'red'
            icone = 'fa-industry'
            layer_group = ind_group
    
        marcador = fl.Marker(
            location=localiza,
            draggable=False,
            popup=f'<p id="latlon">{localiza[0]}, {localiza[1]} <br><a href={googlemaps}>GoogleMaps</a></p>',
            tooltip='<p><b>'+ local['Nome'] +'</b><br>'+
                    local['Rua'] +','+ str(local['Numero']) +'<br>'+
                    local['Bairro'] +' - '+ local['Cidade'] +'/'+ local['Estado'] +'<br>'+
                    'CEP: '+ str(local['CEP']) +'</p>',
            icon=fl.Icon(color=cor, icon_color='white', prefix='fa', icon=icone)
        )
        layer_group.add_child(marcador)

    minimap = plugins.MiniMap()
    mapa.add_child(minimap)
    mapa.add_child(fl.LatLngPopup())
    mouse = fl.plugins.MousePosition(
        position='bottomleft',
        separator=',',
        empty_string='Unavailable',
        prefix='Coordenadas: ',
        num_digits=5
        )
    mapa.add_child(mouse)
    fl.LayerControl().add_to(mapa)

    return mapa

meumapa = fl.Map(
    location=LOCATION_CENTER,
    zoom_start=ZOOM,
    tiles='openstreetmap'
)
construct_map(meumapa)

meumapa.save(".\mapas\output\smap.html")

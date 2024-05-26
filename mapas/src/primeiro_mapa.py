import folium as fl
from folium import plugins
import json
import jinja2
from jinja2 import Template
from folium.map import Marker

tmpldata = """<!-- monkey patched Marker template -->
{% macro script(this, kwargs) %}
    var {{ this.get_name() }} = L.marker(
        {{ this.location|tojson }},
        {{ this.options|tojson }}
    ).addTo({{ this._parent.get_name() }}).on('click', onClick);
{% endmacro %}
"""

Marker._mytemplate = Template(tmpldata)
def myMarkerInit(self, *args, **kwargs):
    self.__init_orig__(*args, **kwargs)
    self._template = self._mytemplate
Marker.__init_orig__ = Marker.__init__
Marker.__init__ = myMarkerInit


lista_locais = json.load(open(".\mapas\lista_enderecos.json", "r"))
location_center = [0,-60]

mapa = fl.Map(
    location=location_center,
    zoom_start=4,
    tiles='openstreetmap',
    #default_css=[('leaflet_css', 'https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css'), ('bootstrap_css', 'https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css'), ('glyphicons_css', 'https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css'), ('awesome_markers_font_css', 'https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css'), ('awesome_markers_css', 'https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css'), ('awesome_rotate_css', 'https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css')],
    #default_js=[('leaflet', 'https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js'), ('jquery', 'https://code.jquery.com/jquery-1.12.4.min.js'), ('bootstrap', 'https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js'), ('awesome_markers', 'https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js')]
)

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

'''
fl.Marker(
    location_center,
    popup='Texto do marcador',
    tooltip='Clique aqui',
    icon=fl.Icon(color='pink', prefix='glyphicon', icon='info-sign')
).add_to(mapa)

fl.CircleMarker(
    location_center,
    radius=50,
    color='#234328',
    fill=True,
    fill_color='#328923'
).add_to(mapa)
'''

for local in lista_locais:
    localiza = (str(local['Latitude']),str(local['Longitude']))
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
        #popup=f'<input type="text" value="{localiza[0]}, {localiza[1]}" id="myInput"><button onclick="myFunction()">Copy location</button>',
        popup=f'<p id="latlon">{localiza[0]}, {localiza[1]}</p>',
        tooltip='<b>'+ local['Nome'] +'</b>',
        icon=fl.Icon(color=cor, icon_color='white', prefix='fa', icon=icone)
        #icon=fl.DivIcon(html=f"""<div style="font-family: courier new; color: blue">{data.iloc[i]['name']}</div>""")
        #icon=fl.features.CustomIcon('PASTE_URL', icon_size=(24, 24))
    )
 
    #marcador.add_to(mapa)
    layer_group.add_child(marcador)

me_coord = fl.MacroElement().add_to(mapa)

me_coord._template = jinja2.Template("""
    {% macro script(this, kwargs) %}
    function myFunction() {
      /* Get the text field */
      var copyText = document.getElementById("myInput");

      /* Select the text field */
      copyText.select();
      copyText.setSelectionRange(0, 99999); /* For mobile devices */

      /* Copy the text inside the text field */
      document.execCommand("copy");
    }

    function copy(text) {
        var input = document.createElement('textarea');
        input.innerHTML = text;
        document.body.appendChild(input);
        input.select();
        var result = document.execCommand('copy');
        document.body.removeChild(input);
        return result;
    };
    
    function getInnerText( sel ) {
        var txt = '';
        $( sel ).contents().each(function() {
            var children = $(this).children();
            txt += ' ' + this.nodeType === 3 ? this.nodeValue : children.length ? getInnerText( this ) : $(this).text();
        });
        return txt;
    };

    /* This function is used to copy by clicking on Markers - Rename this and the next */
    function _onClick(e) {
       var popup = e.target.getPopup();
       var content = popup.getContent();
       text = getInnerText(content);
       copy(text);
    };

    /* This function is used to copy by daggable Markers */
    function onClick(e) {
       var lat = e.latlng.lat; 
       var lng = e.latlng.lng;
       var newContent = '<p id="latlon">' + lat + ', ' + lng + '</p>';
       e.target.setPopupContent(newContent);
       copy(lat + ', ' + lng);
    };
    {% endmacro %}
""")

minimap = plugins.MiniMap()
mapa.add_child(minimap)
mapa.add_child(fl.LatLngPopup())
#mapa.add_child(folium.ClickForMarker(popup="Waypoint"))
mouse = fl.plugins.MousePosition(
    position='bottomleft',
    separator=',',
    empty_string='Unavailable',
    prefix='Coordenadas: ',
    num_digits=5
    )
mapa.add_child(mouse)

fl.LayerControl().add_to(mapa)
mapa.save(".\mapas\output\pmap.html")

# https://getbootstrap.com/docs/3.3/components/
# https://fontawesome.com/v4/icons/
# https://devpress.csdn.net/python/62fe298cc677032930804792.html
import pandas as pd
import folium

CB_geoData = pd.read_csv('./CoffeeBean_geo.csv', encoding ='cp949', engine = 'python')

wido = list(CB_geoData['위도'])
geungdo = list(CB_geoData['경도'])


k = 0
for a,b in zip(wido,geungdo):
    map_CB = folium.Map(location = [a,b], zoom_start = 15)

    for i, store in CB_geoData.iterrows():
         folium.Marker(location = [store['위도'], store['경도']], popup = store['store'], icon = folium.Icon(color = 'red', icon = 'star')).add_to(map_CB)

    map_CB.save('./map_CB'+ str(k) + '.html')
    k += 1

import pandas as pd
import streamlit as st


dfcat = pd.read_csv('Catalog\catalogo con fotos.csv', sep=';', encoding='utf-8')

#st.dataframe(dfcat[['SKU','URL_SKU1']])

n=0
for i in dfcat['SKU']:
    print(n)
    sku = dfcat['SKU'].iloc[n]
    url_img = dfcat['URL_SKU1'].iloc[n]
    try:
        st.image(url_img,width=200)
        st.write(sku)
    except:
        pass
    n += 1        

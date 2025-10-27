import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px


# Page setup 
st.set_page_config(page_title="Constitution Preamble Clusters", layout="wide")
st.title("Constitution Preamble Clusters Across the World")
st.markdown("Explore how different constitutions express national ideals and values through their preambles.")

# 1. Load data
file_path = "data/processed/constitution_preamble_clustered.csv"
df = pd.read_csv(file_path, usecols=['Country', 'cluster'])
df['cluster'] = pd.to_numeric(df['cluster'], errors='coerce')

# 2. Load world geometry 
world = gpd.read_file(
    "https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip"
)

# 3. Merge on country names 
merged = world.merge(df, how='left', left_on='NAME', right_on='Country')

# 4. Map numeric clusters (0–6) to human-readable labels
label_map = {
    0: 'Faith & Founding',
    1: 'Civic Republic',
    2: 'Religious-Administrative',
    3: 'Collective Progress',
    4: 'Legal-Institutional',
    5: 'Parliamentary-Administrative',
    6: 'Unity & Pluralism'
}
merged['cluster_label'] = merged['cluster'].map(label_map)
merged['cluster_label'] = pd.Categorical(
    merged['cluster_label'],
    categories=list(label_map.values()),
    ordered=True
)

# 5. Plot interactive map 
fig = px.choropleth(
    merged,
    geojson=merged.__geo_interface__,
    locations='NAME',
    featureidkey='properties.NAME',
    color='cluster_label',
    hover_name='NAME',
    color_discrete_map={
        'Faith & Founding': '#ff6692',
        'Civic Republic': '#ffa15a',
        'Religious-Administrative': "#7dd123",
        'Collective Progress': '#ff97ff',
        'Legal-Institutional': "#b043e2",
        'Parliamentary-Administrative': "#219fe9",
        'Unity & Pluralism': "#f7eb41"
    },
    title="World Map Colored by Preambles of Countries’ Constitutions"
)
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(legend_title_text='Cluster Categories',
        height=900,  
        margin=dict(l=0, r=0, t=50, b=0)
    )

st.plotly_chart(fig, use_container_width=True)

# 6. Cluster descriptions 
st.header("Cluster Summaries")

cluster_info = {
    "Legal-Institutional": {
        "Sample Countries": "Australia, Canada, United Kingdom, France, Mexico",
        "Interpretation": "Common-law or Commonwealth traditions emphasizing legality and institutional formality."
    },
    "Unity & Pluralism": {
        "Sample Countries": "South Africa, Kenya, Congo, Ethiopia",
        "Interpretation": "Generally, African constitutions stressing unity, dignity, and cultural pluralism."
    },
    "Faith & Founding": {
        "Sample Countries": "Argentina, Bolivia, Brazil, Chile, United States of America",
        "Interpretation": "Constitutions emphasizing faith, moral values, social justice, and independence, mostly found in South Americas."
    },
    "Civic Republic": {
        "Sample Countries": "India, Ukraine, Russia, Estonia",
        "Interpretation": "Countries historically within or influenced by the USSR’s sphere of influence, focusing on peace, civic responsibility, and renewal."
    },
    "Religious-Administrative": {
        "Sample Countries": "Afghanistan, Pakistan, Iran, Iraq, Egypt",
        "Interpretation": "Governance guided by religious principles and structured administrative order, mostly found in Islamic nations."
    },
    "Collective Progress": {
        "Sample Countries": "Indonesia, Bangladesh, Bhutan, Thailand, China",
        "Interpretation": "Socialist or revolutionary constitutions centered on unity and collective progress."
    },
    "Parliamentary-Administrative": {
        "Sample Countries": "Germany, Austria, Belgium, Norway, Italy",
        "Interpretation": "European parliamentary and administrative constitutional systems."
    }
}

for name, details in cluster_info.items():
    st.subheader(name)
    st.markdown(f"**Sample Countries:** {details['Sample Countries']}")
    st.markdown(f"**Interpretation:** {details['Interpretation']}")

# 7. Notebook link or embed 
st.header("Notebook Access")
st.markdown(
    "[📓 View full analysis notebook on GitHub](https://github.com/ShailKPatel/Constitutional-Values/blob/main/notebooks/01_data_preprocessing.ipynb)"
)


# Constitution Preamble Clusters Across the World

**Explore how different constitutions express national ideals and values through their preambles.**

This project analyzes the **preambles** of world constitutions using modern **natural language processing (NLP)** techniques to discover shared linguistic and philosophical themes. It visualizes countries clustered by their constitutional language into distinct categories of national identity and governance.

---

## Overview

Constitutional preambles serve as a window into a nation’s founding values and principles — from faith and unity to legality and progress. Using **semantic embeddings** and **unsupervised clustering**, this project identifies recurring ideological patterns and presents them through an **interactive world map** built with Streamlit and Plotly.

### Live App  
 [View Streamlit Dashboard](https://constitutional-values.streamlit.app/)

### Full Notebook  
 [01_data_preprocessing.ipynb](https://github.com/ShailKPatel/Constitutional-Values/blob/main/notebooks/01_data_preprocessing.ipynb)

---

## Methodology

1. **Text Cleaning & Preprocessing**
   - Remove punctuation, numbers, and stop words.
   - Standardize text casing.
   - Prepare preambles for embedding.

2. **Embedding**
   - Model: `SentenceTransformer('all-mpnet-base-v2')`
   - Generates semantic vectors for each country's preamble.

3. **Clustering**
   - Algorithm: `KMeans`
   - Number of clusters determined via **Elbow** and **Silhouette** methods.
   - Chosen: **6 clusters**

4. **Dimensionality Reduction**
   - Visualized in 2D space using **PCA**.

5. **Visualization**
   - Mapped using **GeoPandas** and **Plotly Choropleth**.
   - Interactive dashboard built in **Streamlit**.

---

## Cluster Summaries

| Cluster | Description | Sample Countries |
|----------|--------------|------------------|
| **Legal-Institutional** | Common-law or Commonwealth traditions emphasizing legality and institutional formality. | Australia, Canada, United Kingdom, France, Mexico |
| **Unity & Pluralism** | African constitutions stressing unity, dignity, and cultural pluralism. | South Africa, Kenya, Congo, Ethiopia |
| **Faith & Founding** | Constitutions emphasizing faith, moral values, social justice, and independence, mostly found in South America. | Argentina, Bolivia, Brazil, Chile, USA |
| **Civic Republic** | Influenced by USSR’s civic and renewal ideals emphasizing peace and responsibility. | India, Ukraine, Russia, Estonia |
| **Religious-Administrative** | Governance guided by religious principles and structured administrative order, mostly in Islamic nations. | Afghanistan, Pakistan, Iran, Iraq, Egypt |
| **Collective Progress** | Socialist or revolutionary constitutions centered on unity and collective progress. | Indonesia, Bangladesh, Bhutan, Thailand, China |
| **Parliamentary-Administrative** | European parliamentary and administrative constitutional systems. | Germany, Austria, Belgium, Norway, Italy |

---

## Visualization

The Streamlit app displays an interactive **world map** where each country is colored by its constitutional cluster.

### Features
- Hover to explore cluster membership and country name.  
- Automatically scales to window size.  
- Includes descriptive summaries for each cluster.  

---

## Run Locally

### **1. Clone the repository**
```bash
git clone https://github.com/ShailKPatel/Constitutional-Values.git
cd Constitutional-Values
```

### **2. Install dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run the Streamlit app**
```bash
streamlit run app.py
```

---

## Technologies Used
Python – Data processing and clustering

Pandas / NumPy – Data manipulation

Sentence-Transformers – Text embeddings

scikit-learn – KMeans clustering & PCA

GeoPandas – Country geometries

Plotly – Interactive choropleth visualization

Streamlit – Web app interface

---

### Data Source

Elkins, Zachary, Tom Ginsburg, and James Melton. *Comparative Constitutions Project (CCP).*  
[https://comparativeconstitutionsproject.org/](https://comparativeconstitutionsproject.org/)


> **Note:**  
> The presence or absence of any country in this map is **not** an ideological or political statement.  
> The countries shown were selected solely based on their availability in the **Comparative Constitutions Project (CCP)** and the **GeoPandas** library.

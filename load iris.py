import json
import requests
import zipfile
import io
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# The Croissant JSON metadata provided
croissant_metadata_str = """
{"@context":{"@language":"en","@vocab":"https://schema.org/","citeAs":"cr:citeAs","column":"cr:column","conformsTo":"dct:conformsTo","cr":"http://mlcommons.org/croissant/","data":{"@id":"cr:data","@type":"@json"},"dataBiases":"cr:dataBiases","dataCollection":"cr:dataCollection","dataType":{"@id":"cr:dataType","@type":"@vocab"},"dct":"http://purl.org/dc/terms/","extract":"cr:extract","field":"cr:field","fileProperty":"cr:fileProperty","fileObject":"cr:fileObject","fileSet":"cr:fileSet","format":"cr:format","includes":"cr:includes","isEnumeration":"cr:isEnumeration","jsonPath":"cr:jsonPath","key":"cr:key","md5":"cr:md5","parentField":"cr:parentField","path":"cr:path","personalSensitiveInformation":"cr:personalSensitiveInformation","recordSet":"cr:recordSet","references":"cr:references","regex":"cr:regex","repeated":"cr:repeated","replace":"cr:replace","sc":"https://schema.org/","separator":"cr:separator","source":"cr:source","subField":"cr:subField","transform":"cr:transform","wd":"https://www.wikidata.org/wiki/"},"alternateName":"","conformsTo":"http://mlcommons.org/croissant/1.0","license":{"@type":"sc:CreativeWork","name":"CC0: Public Domain","url":"https://creativecommons.org/publicdomain/zero/1.0/"},"distribution":[{"contentUrl":"https://www.kaggle.com/api/v1/datasets/download/saurabh00007/iriscsv?datasetVersionNumber=1","contentSize":"1.276 KB","md5":"4QvUUV/jrrk2qaCJ94ITpQ==","encodingFormat":"application/zip","@id":"archive.zip","@type":"cr:FileObject","name":"archive.zip","description":"Archive containing all the contents of the Iris.csv dataset"},{"contentUrl":"Iris.csv","containedIn":{"@id":"archive.zip"},"encodingFormat":"application/vnd.ms-excel","@id":"Iris.csv_fileobject","@type":"cr:FileObject","name":"Iris.csv"}],"recordSet":[{"field":[{"dataType":["sc:Text"],"source":{"fileObject":{"@id":"Iris.csv_fileobject"},"extract":{"column":"Id"}},"@id":"Iris.csv/Id","@type":"cr:Field","name":"Id"},{"dataType":["sc:Float"],"source":{"fileObject":{"@id":"Iris.csv_fileobject"},"extract":{"column":"SepalLengthCm"}},"@id":"Iris.csv/SepalLengthCm","@type":"cr:Field","name":"SepalLengthCm"},{"dataType":["sc:Float"],"source":{"fileObject":{"@id":"Iris.csv_fileobject"},"extract":{"column":"SepalWidthCm"}},"@id":"Iris.csv/SepalWidthCm","@type":"cr:Field","name":"SepalWidthCm"},{"dataType":["sc:Float"],"source":{"fileObject":{"@id":"Iris.csv_fileobject"},"extract":{"column":"PetalLengthCm"}},"@id":"Iris.csv/PetalLengthCm","@type":"cr:Field","name":"PetalLengthCm"},{"dataType":["sc:Float"],"source":{"fileObject":{"@id":"Iris.csv_fileobject"},"extract":{"column":"PetalWidthCm"}},"@id":"Iris.csv/PetalWidthCm","@type":"cr:Field","name":"PetalWidthCm"},{"dataType":["sc:Text"],"source":{"fileObject":{"@id":"Iris.csv_fileobject"},"extract":{"column":"Species"}},"@id":"Iris.csv/Species","@type":"cr:Field","name":"Species"}],"@id":"Iris.csv","@type":"cr:RecordSet","name":"Iris.csv"}],"version":1,"keywords":["subject > science and technology > internet"],"isAccessibleForFree":true,"includedInDataCatalog":{"@type":"sc:DataCatalog","name":"Kaggle","url":"https://www.kaggle.com"},"creator":{"@type":"sc:Person","name":"saurabh singh","url":"/saurabh00007","image":"https://storage.googleapis.com/kaggle-avatars/thumbnails/1301025-gp.jpg"},"publisher":{"@type":"sc:Organization","name":"Kaggle","url":"https://www.kaggle.com/organizations/kaggle","image":"https://storage.googleapis.com/kaggle-organizations/4/thumbnail.png"},"thumbnailUrl":"https://storage.googleapis.com/kaggle-datasets-images/new-version-temp-images/default-backgrounds-98.png-1301025/dataset-card.png","dateModified":"2017-11-09T07:34:35.167","datePublished":"2017-11-09T07:34:35.167","@type":"sc:Dataset","name":"Iris.csv","url":"https://www.kaggle.com/datasets/saurabh00007/iriscsv/versions/1","description":""}
"""

# 1. Parse Croissant JSON
metadata = json.loads(croissant_metadata_str)

# Extract download URL for the archive and the CSV filename
archive_url = None
csv_filename_in_archive = None

for dist_item in metadata.get("distribution", []):
    if dist_item.get("@id") == "archive.zip":
        archive_url = dist_item.get("contentUrl")
    elif dist_item.get("@id") == "Iris.csv_fileobject":
        if dist_item.get("containedIn", {}).get("@id") == "archive.zip":
            csv_filename_in_archive = dist_item.get("contentUrl") # or name

if not archive_url:
    raise ValueError("Could not find archive.zip URL in metadata.")
if not csv_filename_in_archive:
    raise ValueError("Could not find Iris.csv details in metadata.")

print(f"Archive URL: {archive_url}")
print(f"CSV filename in archive: {csv_filename_in_archive}")

# 2. Download the dataset
# Note: Kaggle API URLs often require authentication or specific headers.
# This direct download link might work, but if not, you might need to download manually
# or use the Kaggle API with credentials.
try:
    print(f"Downloading from {archive_url}...")
    response = requests.get(archive_url, stream=True)
    response.raise_for_status() # Raise an exception for HTTP errors

    # 3. Extract CSV from ZIP and load into pandas
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        if csv_filename_in_archive not in z.namelist():
            raise FileNotFoundError(f"{csv_filename_in_archive} not found in the zip archive. Found: {z.namelist()}")
        
        with z.open(csv_filename_in_archive) as csv_file:
            df = pd.read_csv(csv_file)
            print(f"\nSuccessfully loaded {csv_filename_in_archive} into a DataFrame.")

except requests.exceptions.RequestException as e:
    print(f"Error downloading file: {e}")
    print("Please try downloading 'archive.zip' manually from the Kaggle page or use the Kaggle API.")
    print("If downloaded manually, place 'Iris.csv' in the same directory as this script and uncomment the next lines:")
    # SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    # LOCAL_CSV_PATH = os.path.join(SCRIPT_DIR, "Iris.csv")
    # if os.path.exists(LOCAL_CSV_PATH):
    #     print(f"Loading local file: {LOCAL_CSV_PATH}")
    #     df = pd.read_csv(LOCAL_CSV_PATH)
    # else:
    #     print(f"Local file {LOCAL_CSV_PATH} not found. Exiting.")
    #     exit()
    # Fallback: if you have Iris.csv locally:
    if os.path.exists("Iris.csv"):
        print("Attempting to load local Iris.csv")
        df = pd.read_csv("Iris.csv")
    else:
        print("Download failed and local Iris.csv not found. Exiting.")
        exit()


# 4. Display information in the terminal
print("\n--- DataFrame Head ---")
print(df.head())

print("\n--- DataFrame Info ---")
df.info()

print("\n--- DataFrame Description (Numerical Columns) ---")
print(df.describe())

print("\n--- Value Counts for 'Species' ---")
print(df['Species'].value_counts())

# The 'Id' column is usually an index and not useful for analysis, let's drop it for plots
if 'Id' in df.columns:
    df_for_plotting = df.drop('Id', axis=1)
else:
    df_for_plotting = df.copy()


# 5. Generate visualizations

# Set a nice style for plots
sns.set_theme(style="whitegrid")

# a) Histograms for each numerical feature
print("\nGenerating Histograms...")
numerical_features = df_for_plotting.select_dtypes(include=['float64', 'int64']).columns
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten() # Flatten to 1D array for easy iteration
for i, col in enumerate(numerical_features):
    sns.histplot(data=df_for_plotting, x=col, hue="Species", kde=True, ax=axes[i])
    axes[i].set_title(f'Histogram of {col}')
plt.tight_layout()
plt.suptitle("Histograms of Numerical Features by Species", y=1.02, fontsize=16)
plt.show()

# b) Box plots for each numerical feature by Species
print("Generating Box Plots...")
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()
for i, col in enumerate(numerical_features):
    sns.boxplot(data=df_for_plotting, x="Species", y=col, ax=axes[i])
    axes[i].set_title(f'Box Plot of {col} by Species')
plt.tight_layout()
plt.suptitle("Box Plots of Numerical Features by Species", y=1.02, fontsize=16)
plt.show()

# c) Scatter plot: Sepal Length vs Sepal Width
print("Generating Sepal Length vs Sepal Width Scatter Plot...")
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_for_plotting, x="SepalLengthCm", y="SepalWidthCm", hue="Species", s=70)
plt.title('Sepal Length vs Sepal Width by Species')
plt.show()

# d) Scatter plot: Petal Length vs Petal Width
print("Generating Petal Length vs Petal Width Scatter Plot...")
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_for_plotting, x="PetalLengthCm", y="PetalWidthCm", hue="Species", s=70)
plt.title('Petal Length vs Petal Width by Species')
plt.show()

# e) Pair Plot (shows all pairwise relationships and histograms on diagonal)
print("Generating Pair Plot...")
# Select only numeric columns for correlation, exclude 'Id' if it was numeric
numeric_cols_for_pairplot = df_for_plotting.select_dtypes(include=['number']).columns.tolist()
if 'Species' in df_for_plotting.columns: # ensure species is available for hue
    cols_for_pairplot = numeric_cols_for_pairplot + ['Species']
    sns.pairplot(df_for_plotting[cols_for_pairplot], hue="Species", diag_kind="kde")
else:
    sns.pairplot(df_for_plotting[numeric_cols_for_pairplot], diag_kind="kde")
plt.suptitle("Pair Plot of Iris Features", y=1.02, fontsize=16)
plt.show()

# f) Correlation Heatmap for numerical features
print("Generating Correlation Heatmap...")
# Ensure only numeric columns are used for correlation
numeric_df = df_for_plotting.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_df.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title('Correlation Matrix of Numerical Features')
plt.show()

print("\nAnalysis complete. All plots have been displayed.")
import json
import requests
import zipfile
import io
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# The Croissant JSON-LD metadata provided by the user
CROISSANT_METADATA_STR = """
{
    "@context": {
        "@language": "en",
        "@vocab": "https://schema.org/",
        "citeAs": "cr:citeAs",
        "column": "cr:column",
        "conformsTo": "dct:conformsTo",
        "cr": "http://mlcommons.org/croissant/",
        "data": {
            "@id": "cr:data",
            "@type": "@json"
        },
        "dataBiases": "cr:dataBiases",
        "dataCollection": "cr:dataCollection",
        "dataType": {
            "@id": "cr:dataType",
            "@type": "@vocab"
        },
        "dct": "http://purl.org/dc/terms/",
        "extract": "cr:extract",
        "field": "cr:field",
        "fileProperty": "cr:fileProperty",
        "fileObject": "cr:fileObject",
        "fileSet": "cr:fileSet",
        "format": "cr:format",
        "includes": "cr:includes",
        "isEnumeration": "cr:isEnumeration",
        "jsonPath": "cr:jsonPath",
        "key": "cr:key",
        "md5": "cr:md5",
        "parentField": "cr:parentField",
        "path": "cr:path",
        "personalSensitiveInformation": "cr:personalSensitiveInformation",
        "recordSet": "cr:recordSet",
        "references": "cr:references",
        "regex": "cr:regex",
        "repeated": "cr:repeated",
        "replace": "cr:replace",
        "sc": "https://schema.org/",
        "separator": "cr:separator",
        "source": "cr:source",
        "subField": "cr:subField",
        "transform": "cr:transform",
        "wd": "https://www.wikidata.org/wiki/"
    },
    "alternateName": "Basic Regression Prediction",
    "conformsTo": "http://mlcommons.org/croissant/1.0",
    "license": {
        "@type": "sc:CreativeWork",
        "name": "CC0: Public Domain",
        "url": "https://creativecommons.org/publicdomain/zero/1.0/"
    },
    "distribution": [
        {
            "contentUrl": "https://www.kaggle.com/api/v1/datasets/download/vijayaadithyanvg/car-price-predictionused-cars",
            "contentSize": "3.758 KB",
            "encodingFormat": "application/zip",
            "@id": "archive.zip",
            "@type": "cr:FileObject",
            "name": "archive.zip",
            "description": "Archive containing all the contents of the Car price prediction(used cars) dataset"
        },
        {
            "contentUrl": "car data.csv",
            "containedIn": {
                "@id": "archive.zip"
            },
            "encodingFormat": "text/csv",
            "@id": "car+data.csv_fileobject",
            "@type": "cr:FileObject",
            "name": "car data.csv",
            "description": "This file is used to predict the used car price "
        }
    ],
    "recordSet": [
        {
            "field": [
                {
                    "dataType": [
                        "sc:Text"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "car+data.csv_fileobject"
                        },
                        "extract": {
                            "column": "Car_Name"
                        }
                    },
                    "@id": "car+data.csv/Car_Name",
                    "@type": "cr:Field",
                    "name": "Car_Name",
                    "description": "Name of the car"
                },
                {
                    "dataType": [
                        "sc:Integer"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "car+data.csv_fileobject"
                        },
                        "extract": {
                            "column": "Year"
                        }
                    },
                    "@id": "car+data.csv/Year",
                    "@type": "cr:Field",
                    "name": "Year",
                    "description": "year of the car"
                },
                {
                    "dataType": [
                        "sc:Float"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "car+data.csv_fileobject"
                        },
                        "extract": {
                            "column": "Selling_Price"
                        }
                    },
                    "@id": "car+data.csv/Selling_Price",
                    "@type": "cr:Field",
                    "name": "Selling_Price",
                    "description": "selling price"
                },
                {
                    "dataType": [
                        "sc:Float"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "car+data.csv_fileobject"
                        },
                        "extract": {
                            "column": "Present_Price"
                        }
                    },
                    "@id": "car+data.csv/Present_Price",
                    "@type": "cr:Field",
                    "name": "Present_Price",
                    "description": "present price"
                },
                {
                    "dataType": [
                        "sc:Integer"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "car+data.csv_fileobject"
                        },
                        "extract": {
                            "column": "Driven_kms"
                        }
                    },
                    "@id": "car+data.csv/Driven_kms",
                    "@type": "cr:Field",
                    "name": "Driven_kms",
                    "description": "kms driven"
                },
                {
                    "dataType": [
                        "sc:Text"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "car+data.csv_fileobject"
                        },
                        "extract": {
                            "column": "Fuel_Type"
                        }
                    },
                    "@id": "car+data.csv/Fuel_Type",
                    "@type": "cr:Field",
                    "name": "Fuel_Type",
                    "description": "fuel type"
                },
                {
                    "dataType": [
                        "sc:Text"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "car+data.csv_fileobject"
                        },
                        "extract": {
                            "column": "Selling_type"
                        }
                    },
                    "@id": "car+data.csv/Selling_type",
                    "@type": "cr:Field",
                    "name": "Selling_type",
                    "description": "selling price"
                },
                {
                    "dataType": [
                        "sc:Text"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "car+data.csv_fileobject"
                        },
                        "extract": {
                            "column": "Transmission"
                        }
                    },
                    "@id": "car+data.csv/Transmission",
                    "@type": "cr:Field",
                    "name": "Transmission",
                    "description": "transmission"
                },
                {
                    "dataType": [
                        "sc:Integer"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "car+data.csv_fileobject"
                        },
                        "extract": {
                            "column": "Owner"
                        }
                    },
                    "@id": "car+data.csv/Owner",
                    "@type": "cr:Field",
                    "name": "Owner",
                    "description": "no of owner"
                }
            ],
            "@id": "car+data.csv",
            "@type": "cr:RecordSet",
            "name": "car data.csv",
            "description": "This file is used to predict the used car price "
        }
    ],
    "keywords": [
        "data type > tabular",
        "subject > science and technology > transportation > automobiles and vehicles",
        "geography and places > asia > india",
        "audience > beginner",
        "task > regression"
    ],
    "isAccessibleForFree": true,
    "isLiveDataset": true,
    "includedInDataCatalog": {
        "@type": "sc:DataCatalog",
        "name": "Kaggle",
        "url": "https://www.kaggle.com"
    },
    "creator": {
        "@type": "sc:Person",
        "name": "vijayaadithyan V.G",
        "url": "/vijayaadithyanvg",
        "image": "https://storage.googleapis.com/kaggle-avatars/thumbnails/7642013-kg.jpg"
    },
    "publisher": {
        "@type": "sc:Organization",
        "name": "Kaggle",
        "url": "https://www.kaggle.com/organizations/kaggle",
        "image": "https://storage.googleapis.com/kaggle-organizations/4/thumbnail.png"
    },
    "thumbnailUrl": "https://storage.googleapis.com/kaggle-datasets-images/2491159/4226692/c0e620d8797cd338cbb30c3d36a5f80d/dataset-card.jpg?t=2022-09-20-06-39-07",
    "dateModified": "2022-09-20T06:35:39.007",
    "datePublished": "2022-09-20T06:37:14.268669",
    "@type": "sc:Dataset",
    "name": "Car price prediction(used cars)",
    "url": "https://www.kaggle.com/datasets/vijayaadithyanvg/car-price-predictionused-cars",
    "description": "The price of a car depends on a lot of factors like the goodwill of the brand of the car, features of the car, horsepower and the mileage it gives and many more. Car price prediction is one of the major research areas in machine learning. So if you want to learn how to train a car price prediction model"
}
"""

def main():
    # Load the Croissant metadata
    metadata = json.loads(CROISSANT_METADATA_STR)
    print(f"Dataset Name: {metadata.get('name')}")

    # Find the main archive file object and its download URL
    archive_file_object = None
    for dist in metadata.get("distribution", []):
        if dist.get("encodingFormat") == "application/zip":
            archive_file_object = dist
            break
    
    if not archive_file_object:
        print("Error: Could not find ZIP archive in metadata.")
        return

    archive_url = archive_file_object.get("contentUrl")
    archive_id = archive_file_object.get("@id")
    print(f"Found archive: {archive_file_object.get('name')} with ID: {archive_id}")
    print(f"Downloading from: {archive_url}")

    # Download the archive
    try:
        response = requests.get(archive_url, stream=True)
        response.raise_for_status() # Raise an exception for HTTP errors
        zip_content = io.BytesIO(response.content)
        print("Archive downloaded successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading archive: {e}")
        return

    # Find the CSV file object within the archive
    csv_file_object = None
    for dist in metadata.get("distribution", []):
        if dist.get("encodingFormat") == "text/csv" and \
           dist.get("containedIn", {}).get("@id") == archive_id:
            csv_file_object = dist
            break

    if not csv_file_object:
        print("Error: Could not find CSV file info in metadata for the downloaded archive.")
        return

    csv_filename_in_zip = csv_file_object.get("contentUrl") # This is the name inside the zip
    csv_file_id = csv_file_object.get("@id") # Used to link to recordSet
    print(f"Found CSV file in metadata: {csv_filename_in_zip} (ID: {csv_file_id})")

    # Extract and read the CSV file
    df = None
    try:
        with zipfile.ZipFile(zip_content) as zf:
            if csv_filename_in_zip in zf.namelist():
                with zf.open(csv_filename_in_zip) as csv_file:
                    df = pd.read_csv(csv_file)
                print(f"Successfully extracted and read '{csv_filename_in_zip}' into a DataFrame.")
                print("\nDataFrame head:")
                print(df.head())
                print("\nDataFrame info:")
                df.info()
            else:
                print(f"Error: CSV file '{csv_filename_in_zip}' not found in the archive.")
                print(f"Files in archive: {zf.namelist()}")
                return
    except Exception as e:
        print(f"Error processing ZIP file or reading CSV: {e}")
        return

    if df is None:
        print("DataFrame could not be loaded.")
        return

    # Find the corresponding RecordSet
    target_record_set = None
    for rs in metadata.get("recordSet", []):
        # The @id in recordSet for the CSV is "car+data.csv" (name)
        # The @id in distribution for the CSV FileObject is "car+data.csv_fileobject"
        # We need to match the FileObject's ID from the Field's source
        # A simpler way for this specific JSON is to match the recordSet's name
        # or iterate fields and check `source.fileObject.@id`
        # For this structure, matching recordSet name is easiest:
        if rs.get("name") == csv_filename_in_zip: # or rs.get("@id") == csv_filename_in_zip
            target_record_set = rs
            break
    
    if not target_record_set:
        # Fallback: check if any field points to our csv_file_id
        for rs in metadata.get("recordSet", []):
            for field_info in rs.get("field", []):
                if field_info.get("source", {}).get("fileObject", {}).get("@id") == csv_file_id:
                    target_record_set = rs
                    break
            if target_record_set:
                break
    
    if not target_record_set:
        print(f"Error: Could not find RecordSet associated with CSV file ID '{csv_file_id}' or name '{csv_filename_in_zip}'.")
        return

    print(f"\nProcessing RecordSet: {target_record_set.get('name')}")

    # Generate plots based on dataType from metadata
    # Ensure matplotlib uses a non-interactive backend if running in a headless environment
    # or just rely on plt.show() for interactive environments.
    
    # Use seaborn for nicer default styles
    sns.set_theme(style="whitegrid")

    for field_info in target_record_set.get("field", []):
        col_name_meta = field_info.get("name") # User-friendly name
        col_name_csv = field_info.get("source", {}).get("extract", {}).get("column") # Actual column name in CSV
        data_type_list = field_info.get("dataType", [])
        
        if not col_name_csv:
            print(f"Skipping field '{col_name_meta}' as CSV column name is not defined.")
            continue
        if col_name_csv not in df.columns:
            print(f"Warning: Column '{col_name_csv}' (from metadata field '{col_name_meta}') not found in DataFrame. Skipping.")
            continue

        print(f"\nPlotting for column: {col_name_csv} (Type: {data_type_list})")

        plt.figure(figsize=(10, 6))
        
        if any(dt in ["sc:Integer", "sc:Float"] for dt in data_type_list):
            # Numerical data: Histogram
            # Try to convert to numeric, coercing errors for robustness if data is messy
            numeric_col = pd.to_numeric(df[col_name_csv], errors='coerce')
            if numeric_col.isnull().all():
                print(f"Column '{col_name_csv}' could not be converted to numeric or is all NaN. Skipping histogram.")
                plt.close() # Close the unused figure
                continue

            sns.histplot(numeric_col.dropna(), kde=True)
            plt.title(f"Histogram of {col_name_csv}")
            plt.xlabel(col_name_csv)
            plt.ylabel("Frequency")

        elif "sc:Text" in data_type_list:
            # Categorical data: Bar chart of value counts
            # Check for high cardinality
            unique_values = df[col_name_csv].nunique()
            if unique_values > 50: # Arbitrary threshold for too many categories
                print(f"Column '{col_name_csv}' has {unique_values} unique values. Plotting top 20.")
                counts = df[col_name_csv].value_counts().nlargest(20)
                sns.barplot(x=counts.index, y=counts.values)
                plt.title(f"Top 20 Value Counts for {col_name_csv}")
            else:
                counts = df[col_name_csv].value_counts()
                sns.barplot(x=counts.index, y=counts.values)
                plt.title(f"Value Counts for {col_name_csv}")
            
            plt.xlabel(col_name_csv)
            plt.ylabel("Count")
            plt.xticks(rotation=45, ha='right') # Rotate labels if they are long
        else:
            print(f"Unsupported dataType {data_type_list} for column '{col_name_csv}'. Skipping plot.")
            plt.close() # Close the unused figure
            continue
        
        plt.tight_layout() # Adjust layout to prevent labels from overlapping

    if plt.get_fignums(): # Check if any figures were created
        print("\nDisplaying plots...")
        plt.show()
    else:
        print("\nNo plots were generated.")


if __name__ == "__main__":
    main()
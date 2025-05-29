import json
import networkx as nx
import matplotlib.pyplot as plt
import textwrap

# Paste the JSON data here
json_data = """
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
        "isLiveDataset": "cr:isLiveDataset",
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
    "alternateName": "during this darker times, we need to understand unemployment rate",
    "conformsTo": "http://mlcommons.org/croissant/1.0",
    "license": {
        "@type": "sc:CreativeWork",
        "name": "Other (specified in description)"
    },
    "distribution": [
        {
            "contentUrl": "https://www.kaggle.com/api/v1/datasets/download/gokulrajkmv/unemployment-in-india",
            "contentSize": "15.952 KB",
            "encodingFormat": "application/zip",
            "@id": "archive.zip",
            "@type": "cr:FileObject",
            "name": "archive.zip",
            "description": "Archive containing all the contents of the Unemployment in India dataset"
        },
        {
            "contentUrl": "Unemployment in India.csv",
            "containedIn": {
                "@id": "archive.zip"
            },
            "encodingFormat": "application/vnd.ms-excel",
            "@id": "Unemployment\\u002Bin\\u002BIndia.csv_fileobject",
            "@type": "cr:FileObject",
            "name": "Unemployment in India.csv",
            "description": "The datasets explains the unemployment and employment rate in percentage for different states in India for last one year"
        },
        {
            "contentUrl": "Unemployment_Rate_upto_11_2020.csv",
            "containedIn": {
                "@id": "archive.zip"
            },
            "encodingFormat": "application/vnd.ms-excel",
            "@id": "Unemployment_Rate_upto_11_2020.csv_fileobject",
            "@type": "cr:FileObject",
            "name": "Unemployment_Rate_upto_11_2020.csv"
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
                            "@id": "Unemployment\\u002Bin\\u002BIndia.csv_fileobject"
                        },
                        "extract": {
                            "column": "Region"
                        }
                    },
                    "@id": "Unemployment\\u002Bin\\u002BIndia.csv/Region",
                    "@type": "cr:Field",
                    "name": "Region",
                    "description": "States and UTs in India"
                },
                {
                    "dataType": [
                        "sc:Text"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "Unemployment\\u002Bin\\u002BIndia.csv_fileobject"
                        },
                        "extract": {
                            "column": "Date"
                        }
                    },
                    "@id": "Unemployment\\u002Bin\\u002BIndia.csv/Date",
                    "@type": "cr:Field",
                    "name": "Date"
                },
                {
                    "dataType": [
                        "sc:Text"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "Unemployment\\u002Bin\\u002BIndia.csv_fileobject"
                        },
                        "extract": {
                            "column": "Frequency"
                        }
                    },
                    "@id": "Unemployment\\u002Bin\\u002BIndia.csv/Frequency",
                    "@type": "cr:Field",
                    "name": "Frequency",
                    "description": "data collected Monthly"
                },
                {
                    "dataType": [
                        "sc:Float"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "Unemployment\\u002Bin\\u002BIndia.csv_fileobject"
                        },
                        "extract": {
                            "column": "Estimated Unemployment Rate (%)"
                        }
                    },
                    "@id": "Unemployment\\u002Bin\\u002BIndia.csv/Estimated\\u002BUnemployment\\u002BRate\\u002B(%25)",
                    "@type": "cr:Field",
                    "name": "Estimated Unemployment Rate (%)",
                    "description": "Unemployment rate"
                },
                {
                    "dataType": [
                        "sc:Float"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "Unemployment\\u002Bin\\u002BIndia.csv_fileobject"
                        },
                        "extract": {
                            "column": "Estimated Employed"
                        }
                    },
                    "@id": "Unemployment\\u002Bin\\u002BIndia.csv/Estimated\\u002BEmployed",
                    "@type": "cr:Field",
                    "name": "Estimated Employed",
                    "description": "Employment rate"
                },
                {
                    "dataType": [
                        "sc:Float"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "Unemployment\\u002Bin\\u002BIndia.csv_fileobject"
                        },
                        "extract": {
                            "column": "Estimated Labour Participation Rate (%)"
                        }
                    },
                    "@id": "Unemployment\\u002Bin\\u002BIndia.csv/Estimated\\u002BLabour\\u002BParticipation\\u002BRate\\u002B(%25)",
                    "@type": "cr:Field",
                    "name": "Estimated Labour Participation Rate (%)",
                    "description": "The labor force participation rate is a measure of an economy\\u0027s active workforce"
                },
                {
                    "dataType": [
                        "sc:Text"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "Unemployment\\u002Bin\\u002BIndia.csv_fileobject"
                        },
                        "extract": {
                            "column": "Area"
                        }
                    },
                    "@id": "Unemployment\\u002Bin\\u002BIndia.csv/Area",
                    "@type": "cr:Field",
                    "name": "Area",
                    "description": "Employment and unemployment rates in Urban and rural areas"
                }
            ],
            "@id": "Unemployment\\u002Bin\\u002BIndia.csv",
            "@type": "cr:RecordSet",
            "name": "Unemployment in India.csv",
            "description": "The datasets explains the unemployment and employment rate in percentage for different states in India for last one year"
        },
        {
            "field": [
                {
                    "dataType": [
                        "sc:Text"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "Unemployment_Rate_upto_11_2020.csv_fileobject"
                        },
                        "extract": {
                            "column": "Region"
                        }
                    },
                    "@id": "Unemployment_Rate_upto_11_2020.csv/Region",
                    "@type": "cr:Field",
                    "name": "Region"
                },
                {
                    "dataType": [
                        "sc:Text"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "Unemployment_Rate_upto_11_2020.csv_fileobject"
                        },
                        "extract": {
                            "column": "Date"
                        }
                    },
                    "@id": "Unemployment_Rate_upto_11_2020.csv/Date",
                    "@type": "cr:Field",
                    "name": "Date"
                },
                {
                    "dataType": [
                        "sc:Text"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "Unemployment_Rate_upto_11_2020.csv_fileobject"
                        },
                        "extract": {
                            "column": "Frequency"
                        }
                    },
                    "@id": "Unemployment_Rate_upto_11_2020.csv/Frequency",
                    "@type": "cr:Field",
                    "name": "Frequency"
                },
                {
                    "dataType": [
                        "sc:Float"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "Unemployment_Rate_upto_11_2020.csv_fileobject"
                        },
                        "extract": {
                            "column": "Estimated Unemployment Rate (%)"
                        }
                    },
                    "@id": "Unemployment_Rate_upto_11_2020.csv/Estimated\\u002BUnemployment\\u002BRate\\u002B(%25)",
                    "@type": "cr:Field",
                    "name": "Estimated Unemployment Rate (%)"
                },
                {
                    "dataType": [
                        "sc:Integer"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "Unemployment_Rate_upto_11_2020.csv_fileobject"
                        },
                        "extract": {
                            "column": "Estimated Employed"
                        }
                    },
                    "@id": "Unemployment_Rate_upto_11_2020.csv/Estimated\\u002BEmployed",
                    "@type": "cr:Field",
                    "name": "Estimated Employed"
                },
                {
                    "dataType": [
                        "sc:Float"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "Unemployment_Rate_upto_11_2020.csv_fileobject"
                        },
                        "extract": {
                            "column": "Estimated Labour Participation Rate (%)"
                        }
                    },
                    "@id": "Unemployment_Rate_upto_11_2020.csv/Estimated\\u002BLabour\\u002BParticipation\\u002BRate\\u002B(%25)",
                    "@type": "cr:Field",
                    "name": "Estimated Labour Participation Rate (%)"
                },
                {
                    "dataType": [
                        "sc:Text"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "Unemployment_Rate_upto_11_2020.csv_fileobject"
                        },
                        "extract": {
                            "column": "Region"
                        }
                    },
                    "@id": "Unemployment_Rate_upto_11_2020.csv/Region", 
                    "@type": "cr:Field",
                    "name": "Region"
                },
                {
                    "dataType": [
                        "sc:Text"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "Unemployment_Rate_upto_11_2020.csv_fileobject"
                        },
                        "extract": {
                            "column": "longitude"
                        }
                    },
                    "@id": "Unemployment_Rate_upto_11_2020.csv/longitude",
                    "@type": "cr:Field",
                    "name": "longitude"
                },
                {
                    "dataType": [
                        "sc:Float"
                    ],
                    "source": {
                        "fileObject": {
                            "@id": "Unemployment_Rate_upto_11_2020.csv_fileobject"
                        },
                        "extract": {
                            "column": "latitude"
                        }
                    },
                    "@id": "Unemployment_Rate_upto_11_2020.csv/latitude",
                    "@type": "cr:Field",
                    "name": "latitude"
                }
            ],
            "@id": "Unemployment_Rate_upto_11_2020.csv",
            "@type": "cr:RecordSet",
            "name": "Unemployment_Rate_upto_11_2020.csv"
        }
    ],
    "keywords": [
        "subject > health and fitness > health > health conditions > diseases > covid19",
        "subject > people and society > jobs and career > employment"
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
        "name": "Gokul raj K.",
        "url": "/gokulrajkmv",
        "image": "https://storage.googleapis.com/kaggle-avatars/thumbnails/5012903-kg.jpg"
    },
    "publisher": {
        "@type": "sc:Organization",
        "name": "Kaggle",
        "url": "https://www.kaggle.com/organizations/kaggle",
        "image": "https://storage.googleapis.com/kaggle-organizations/4/thumbnail.png"
    },
    "thumbnailUrl": "https://storage.googleapis.com/kaggle-datasets-images/752131/1300098/acc1b9b39cc1ad58a70ccd937b14bb1a/dataset-card.jpg?t=2020-07-02-11-29-54",
    "dateModified": "2020-11-05T12:41:41.57",
    "datePublished": "2020-07-28T06:17:32.7050309",
    "@type": "sc:Dataset",
    "name": "Unemployment in India",
    "url": "https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india",
    "description": "### Context\\n\\nThe story behind this datasets is how lock-down affects employment opportunities and how the unemployment rate increases during the Covid-19.\\n\\n### Content\\n\\nThis dataset contains the unemployment rate of all the states in India\\n\\nRegion                                                        =        states in India\\nDate                                                            = \\t      date which the unemployment rate observed \\nFrequency                                                  =        measuring frequency (Monthly)\\t \\nEstimated Unemployment Rate (%)          =       percentage of people unemployed in  each States of India\\nEstimated Employed\\t                            =        percentage of people employed\\nEstimated Labour Participation Rate (%) =\\t      labour force participation rate by dividing the number of people actively participating in the labour force by the \\n                                                                              total number of people eligible to participate in the labor force\\n force\\n\\n\\n### Acknowledgements\\n\\nI wouldn\\u0027t be here without the help of my friends. I owe you thanks !!\\n\\n\\n### Inspiration\\n\\nquestions?\\n1. How Covid-19 affects the employment\\n2. how far the unemployment rate will go\\n\\nsource of datasets\\nhttps://unemploymentinindia.cmie.com/"
}
"""

dataset = json.loads(json_data)

def print_dataset_summary(data):
    """Prints a summary of the dataset to the terminal."""
    print("="*50)
    print(f"Dataset Name: {data.get('name', 'N/A')}")
    print(f"Description: {data.get('description', 'N/A').splitlines()[0]}...") # First line
    print(f"URL: {data.get('url', 'N/A')}")
    print(f"License: {data.get('license', {}).get('name', 'N/A')}")
    print(f"Published: {data.get('datePublished', 'N/A')}")
    print(f"Modified: {data.get('dateModified', 'N/A')}")
    if data.get('creator'):
        print(f"Creator: {data['creator'].get('name', 'N/A')}")
    if data.get('publisher'):
        print(f"Publisher: {data['publisher'].get('name', 'N/A')}")
    print("="*50)

    print("\nDistribution (Files):")
    if "distribution" in data:
        for file_obj in data["distribution"]:
            print(f"  - File Name: {file_obj.get('name', 'N/A')}")
            print(f"    ID: {file_obj.get('@id', 'N/A')}")
            print(f"    Content URL: {file_obj.get('contentUrl', 'N/A')}")
            print(f"    Encoding: {file_obj.get('encodingFormat', 'N/A')}")
            if "containedIn" in file_obj:
                print(f"    Contained In: {file_obj['containedIn'].get('@id', 'N/A')}")
    else:
        print("  No distribution information found.")
    print("="*50)

    print("\nRecord Sets:")
    if "recordSet" in data:
        for rs_idx, record_set in enumerate(data["recordSet"]):
            print(f"\n  Record Set {rs_idx+1}: {record_set.get('name', 'N/A')}")
            print(f"  ID: {record_set.get('@id', 'N/A')}")
            print(f"  Description: {record_set.get('description', 'N/A')}")
            print("  Fields:")
            if "field" in record_set:
                for field_idx, field in enumerate(record_set["field"]):
                    field_name = field.get('name', f'Unnamed Field {field_idx+1}')
                    field_id = field.get('@id', 'N/A')
                    data_type = ', '.join(field.get('dataType', ['N/A']))
                    source_file = field.get('source', {}).get('fileObject', {}).get('@id', 'N/A')
                    source_column = field.get('source', {}).get('extract', {}).get('column', 'N/A')
                    
                    print(f"    - Field Name: {field_name}")
                    print(f"      ID: {field_id}")
                    print(f"      Data Type: {data_type}")
                    print(f"      Source File ID: {source_file}")
                    print(f"      Source Column: {source_column}")
                    if field.get('description'):
                        print(f"      Description: {field.get('description')}")
            else:
                print("    No fields defined for this record set.")
    else:
        print("  No record sets found.")
    print("="*50)

def visualize_dataset_structure(data):
    """Generates and displays a graph of the dataset structure."""
    G = nx.DiGraph()
    
    dataset_node_id = data.get('@id', data.get('name', 'Dataset'))
    dataset_label = data.get('name', 'Dataset')
    G.add_node(dataset_node_id, label=dataset_label, type='Dataset', color='skyblue')

    file_id_to_name = {}

    # Add FileObjects (distribution)
    if "distribution" in data:
        for file_obj in data["distribution"]:
            file_id = file_obj["@id"]
            file_name = file_obj["name"]
            file_id_to_name[file_id] = file_name # Store for later reference by fields
            
            # Wrap label for better display
            wrapped_label = '\n'.join(textwrap.wrap(f"File: {file_name}", width=20))
            G.add_node(file_id, label=wrapped_label, type='FileObject', color='lightgreen')
            G.add_edge(dataset_node_id, file_id, label='distributes')
            if "containedIn" in file_obj:
                container_id = file_obj["containedIn"]["@id"]
                # Ensure container node exists (it should from previous iterations if ordered)
                if container_id not in G:
                     # This case might happen if containedIn references an ID not yet processed
                     # For simplicity, we assume archive files are listed first in distribution.
                     # A more robust solution would be a two-pass approach or pre-populating all file nodes.
                    container_name = file_id_to_name.get(container_id, container_id) # Fallback to ID if name not found
                    wrapped_container_label = '\n'.join(textwrap.wrap(f"File: {container_name}", width=20))
                    G.add_node(container_id, label=wrapped_container_label, type='FileObject', color='lightgreen')
                G.add_edge(container_id, file_id, label='contains')

    # Add RecordSets and Fields
    if "recordSet" in data:
        for record_set in data["recordSet"]:
            rs_id = record_set["@id"]
            rs_name = record_set["name"]
            wrapped_rs_label = '\n'.join(textwrap.wrap(f"RecordSet: {rs_name}", width=25))
            G.add_node(rs_id, label=wrapped_rs_label, type='RecordSet', color='lightcoral')
            G.add_edge(dataset_node_id, rs_id, label='has_recordset')

            if "field" in record_set:
                for field in record_set["field"]:
                    field_id = field["@id"]
                    field_name = field["name"]
                    
                    # Handle potential duplicate field IDs within the same record set by making them unique for the graph
                    # Note: The input JSON has a duplicate @id for 'Region' in the second recordSet.
                    # NetworkX uses node IDs as unique identifiers.
                    graph_field_node_id = f"{rs_id}/{field_name}" # Simple way to make it unique per recordset for graph
                    count = 1
                    original_graph_field_node_id = graph_field_node_id
                    while G.has_node(graph_field_node_id): # Ensure unique node ID for graph
                        graph_field_node_id = f"{original_graph_field_node_id}_{count}"
                        count += 1

                    field_dtype_list = field.get('dataType', ['unknown'])
                    field_dtype = field_dtype_list[0] if isinstance(field_dtype_list, list) and field_dtype_list else str(field_dtype_list)
                    
                    wrapped_field_label = '\n'.join(textwrap.wrap(f"Field: {field_name}\n({field_dtype.split(':')[-1]})", width=20))
                    G.add_node(graph_field_node_id, label=wrapped_field_label, type='Field', color='gold')
                    G.add_edge(rs_id, graph_field_node_id, label='has_field')
                    
                    if "source" in field and "fileObject" in field["source"]:
                        source_file_id = field["source"]["fileObject"]["@id"]
                        source_column = field["source"].get("extract", {}).get("column", "N/A")
                        if source_file_id in G: # Check if the source file node exists
                            G.add_edge(graph_field_node_id, source_file_id, label=f'from col:\n"{source_column}"')
                        else:
                            print(f"Warning: Source file ID '{source_file_id}' for field '{field_name}' not found in distribution.")
    
    plt.figure(figsize=(16, 12))
    
    # Position nodes using a layout algorithm
    # pos = nx.spring_layout(G, k=0.9, iterations=50, seed=42) 
    # k controls distance, iterations for convergence
    # For hierarchical data, shell_layout or multipartite_layout can be better if types are well-defined layers
    # Let's try shell layout based on types
    shells = []
    dataset_nodes = [n for n, d in G.nodes(data=True) if d['type'] == 'Dataset']
    file_nodes = [n for n, d in G.nodes(data=True) if d['type'] == 'FileObject']
    recordset_nodes = [n for n, d in G.nodes(data=True) if d['type'] == 'RecordSet']
    field_nodes = [n for n, d in G.nodes(data=True) if d['type'] == 'Field']
    
    if dataset_nodes: shells.append(dataset_nodes)
    if file_nodes: shells.append(file_nodes)
    if recordset_nodes: shells.append(recordset_nodes)
    if field_nodes: shells.append(field_nodes)

    if shells:
        pos = nx.shell_layout(G, nlist=shells)
    else: # Fallback if no types or nodes
        pos = nx.spring_layout(G, k=0.9, iterations=50, seed=42)

    node_colors = [d['color'] for n, d in G.nodes(data=True)]
    node_labels = {n: d['label'] for n, d in G.nodes(data=True)}
    edge_labels = nx.get_edge_attributes(G, 'label')

    nx.draw_networkx_nodes(G, pos, node_size=3000, node_color=node_colors, alpha=0.9)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrowstyle='->', arrowsize=20, alpha=0.6)
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=8)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7, 
                                 bbox=dict(facecolor='white', alpha=0.5, edgecolor='none', boxstyle='round,pad=0.2'))

    plt.title("Dataset Structure Visualization", fontsize=16)
    plt.axis('off') # Turn off the axis
    plt.tight_layout() # Adjust layout to prevent labels from overlapping
    plt.show()


# --- Main execution ---
print("--- Terminal Output: Dataset Summary ---")
print_dataset_summary(dataset)

print("\n--- Generating Graph Visualization ---")
print("Note: A new window will open with the graph. Close it to continue.")
visualize_dataset_structure(dataset)
print("--- Graph generation complete. ---")
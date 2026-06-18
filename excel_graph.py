from dijkstra import shortest_path
import pandas as pd

# Read Excel sheets
nodes_df = pd.read_excel(
    "data\Road.xlsx",
    sheet_name="Nodes"
)

connections_df = pd.read_excel(
    "data\Road.xlsx",
    sheet_name="Connections"
)

destinations_df = pd.read_excel(
    "data\Road.xlsx",
    sheet_name="Destinations"
)

#print(nodes_df)
#print(connections_df)
#print(destinations_df)

graph = {}

for index, row in connections_df.iterrows():

    from_node = row["From"]
    to_node = row["To"]

    if from_node not in graph:
        graph[from_node] = []

    graph[from_node].append(to_node)

    # Reverse connection
    if to_node not in graph:
        graph[to_node] = []

    graph[to_node].append(from_node)

# Print graph
nodes = {}

for index, row in nodes_df.iterrows():

    node_id = row["NodeID"]

    nodes[node_id] = (
        row["X"],
        row["Y"]
    )

#print(nodes)
path = shortest_path(graph, "Gate2", "PlayGround")

print("Shortest Path:")
print(path)
##  Project Objective

R2D2 operates in a 2D world modeled as an **undirected graph**:
- **Vertices**: represent locations where R2D2 needs to place a cube.
- **Weighted edges**: represent the paths between locations (travel distance).
- Each vertex is also assigned **Euclidean coordinates** (2D position).

The mission: **place a colored cube at each location**, ensuring that **neighboring locations (connected by an edge) have cubes of different colors**.

##  Project Tasks

1. **Check if 3 colors are enough**  
   R2D2 starts by trying to use only 3 colors and reasons whether that’s sufficient to satisfy the color constraint.

2. **Optimize movement**  
   He looks for the shortest possible routes (in terms of travel distance) to place all the cubes.

3. **Determine the minimal number of colors**  
   He figures out the minimum number of colors required to correctly color the graph.

## Use

```python
# Path to libtbb.so.2
tbb_path = '/snap/blender/4300/lib'

# Add the path to LD_LIBRARY_PATH
os.environ['LD_LIBRARY_PATH'] = f"{tbb_path}:{os.environ.get('LD_LIBRARY_PATH', '')}"
```

Run the program.
```bash
make all
```
Les résultats seront affichés dans le fichier log

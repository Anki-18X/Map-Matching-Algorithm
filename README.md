# Development of a Map-Matching Algorithm for Distinguishing Vehicular Movement on Highways and Service Roads
Overview
This project develops a map-matching algorithm to accurately distinguish vehicular movements between highways and adjacent service roads. By processing GPS data, road network maps, and vehicle trajectories, it ensures precise classification for applications like traffic management, toll collection, route optimization, and accident monitoring. Using classical computer vision and rule-based geometric techniques, the algorithm prioritizes computational efficiency and reliability in low-resource settings, avoiding modern ML/DL methods.
Features

Dataset: GPS trajectories, OpenStreetMap (OSM) road networks, and vehicle movement patterns.
Algorithm: Rule-based map-matching using geometric and topological analysis.
Processing: Aligns noisy GPS data to correct road segments (highway vs. service road).
Visualization: Trajectory and matching results plotted for validation.

Tech Stack

Python: Core programming language.
GeoPandas/OSMnx: Road network data processing and map handling.
NumPy/Pandas: Numerical and data manipulations.
Matplotlib/Seaborn: Visualization of trajectories and matching accuracy.
Shapely: Geometric computations for map-matching.

Installation

Clone the repository:git clone https://github.com/your-username/map-matching-algorithm.git


Install dependencies:pip install geopandas osmnx numpy pandas matplotlib seaborn shapely


Run the main script:python map_matching.py



Usage

Execute map_matching.py to process GPS data, perform map-matching.raffic management and navigation systems.

Results

The algorithm accurately distinguishes highway and service road movements with high precision.
Visualizations confirm correct alignment of trajectories to road networks.

Contributing
Fork the repository, report issues, or submit pull requests for improvements.
License
This project is licensed under the MIT License.

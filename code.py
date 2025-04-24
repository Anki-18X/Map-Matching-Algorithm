Pipe line


Display and download map

# STEP 1: Install required libraries
!pip install folium geopy

# STEP 2: Upload your .plt file
from google.colab import files
uploaded = files.upload()

# STEP 3: Import and define all functions
import folium
from datetime import datetime
import geopy.distance

def load_plt_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()[6:]

    trajectory = []
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) < 7:
            continue
        lat, lon = float(parts[0]), float(parts[1])
        timestamp_str = parts[5] + ' ' + parts[6]
        try:
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            trajectory.append({'lat': lat, 'lon': lon, 'time': timestamp})
        except ValueError:
            continue
    return trajectory

def compute_speeds(trajectory):
    speeds = [0]
    for i in range(1, len(trajectory)):
        prev, curr = trajectory[i-1], trajectory[i]
        dist = geopy.distance.geodesic((prev['lat'], prev['lon']), (curr['lat'], curr['lon'])).meters
        time_diff = (curr['time'] - prev['time']).total_seconds()
        speeds.append(dist / time_diff if time_diff > 0 else 0)
    return speeds

def classify_points(speeds, speed_thresh=15):
    return ['highway' if speed > speed_thresh else 'service_road' for speed in speeds]

def visualize(trajectory, classifications, output_file="trajectory_map.html"):
    fmap = folium.Map(location=[trajectory[0]['lat'], trajectory[0]['lon']], zoom_start=14)
    fmap = folium.Map(
    location=[trajectory[0]['lat'], trajectory[0]['lon']],
    zoom_start=14,
    tiles='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    attr='Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors'
)
    for point, label in zip(trajectory, classifications):
        color = 'blue' if label == 'highway' else 'green'
        folium.CircleMarker(
            location=[point['lat'], point['lon']],
            radius=3,
            color=color,
            fill=True,
            fill_opacity=0.6,
            popup=label
        ).add_to(fmap)
    fmap.save(output_file)
    return output_file

# STEP 4: Process the uploaded file
import os
plt_filename = list(uploaded.keys())[0]
trajectory = load_plt_file(plt_filename)
speeds = compute_speeds(trajectory)
classes = classify_points(speeds)
html_path = visualize(trajectory, classes)

# STEP 5: Download the interactive map
files.download(html_path)


#Required Libraries

# STEP 1: Install required libraries
!pip install folium geopy


# Upload .plt File

# STEP 2: Upload your .plt file
from google.colab import files
uploaded = files.upload()


# Importing Modules and Defining Helper Functions

# STEP 3: Import and define all functions
import folium
from datetime import datetime
import geopy.distance

def load_plt_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()[6:]

    trajectory = []
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) < 7:
            continue
        lat, lon = float(parts[0]), float(parts[1])
        timestamp_str = parts[5] + ' ' + parts[6]
        try:
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            trajectory.append({'lat': lat, 'lon': lon, 'time': timestamp})
        except ValueError:
            continue
    return trajectory

def compute_speeds(trajectory):
    speeds = [0]
    for i in range(1, len(trajectory)):
        prev, curr = trajectory[i-1], trajectory[i]
        dist = geopy.distance.geodesic((prev['lat'], prev['lon']), (curr['lat'], curr['lon'])).meters
        time_diff = (curr['time'] - prev['time']).total_seconds()
        speeds.append(dist / time_diff if time_diff > 0 else 0)
    return speeds

def classify_points(speeds, speed_thresh=15):
    return ['highway' if speed > speed_thresh else 'service_road' for speed in speeds]

def visualize(trajectory, classifications, output_file="trajectory_map.html"):
    fmap = folium.Map(
        location=[trajectory[0]['lat'], trajectory[0]['lon']],
        zoom_start=14,
        tiles='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        attr='Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors'
    )

    for point, label in zip(trajectory, classifications):
        color = 'blue' if label == 'highway' else 'green'
        folium.CircleMarker(
            location=[point['lat'], point['lon']],
            radius=3,
            color=color,
            fill=True,
            fill_opacity=0.6,
            popup=label
        ).add_to(fmap)

    fmap.save(output_file)
    return output_file


# Processing the Uploaded File

# STEP 4: Process the uploaded file
import os
plt_filename = list(uploaded.keys())[0]
trajectory = load_plt_file(plt_filename)
speeds = compute_speeds(trajectory)
classes = classify_points(speeds)
html_path = visualize(trajectory, classes)

# Download the Output Mapping

# STEP 5: Download the interactive map
files.download(html_path)

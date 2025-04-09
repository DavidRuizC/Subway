import unittest
from SearchAlgorithm import (
    __author__, expand, calculate_cost, calculate_heuristics, remove_cycles, depth_first_search,
    breadth_first_search, uniform_cost_search, remove_redundant_paths, distance_to_stations, Astar)
from SubwayMap import Path
from utils import print_list_of_path, print_list_of_path_with_cost, read_station_information, read_cost_table, read_information
import os
import math

ROOT_FOLDER = './CityInformation/Lyon_smallCity/'

subway_map = read_station_information(os.path.join(ROOT_FOLDER, 'Stations.txt'))
connections = read_cost_table(os.path.join(ROOT_FOLDER, 'Time.txt'))
subway_map.add_connection(connections)

info_velocity_clean = read_information(os.path.join(ROOT_FOLDER, 'InfoVelocity.txt'))
subway_map.add_velocity(info_velocity_clean)

map = subway_map

expanded_paths = [Path([12, 8, 7]), Path([12, 8, 9]), Path([12, 8, 13])]
updated_paths = calculate_heuristics(expanded_paths, map, destination_id=9, type_preference=0)
print([path.h for path in updated_paths], [1, 0, 1])


expanded_paths = [Path([12, 8, 7]), Path([12, 8, 9]), Path([12, 8, 13])]
updated_paths = calculate_heuristics(expanded_paths, map, destination_id=9, type_preference=1)
print([path.h for path in updated_paths], [1.8544574262244504, 0.0, 0.6273597428219158])

expanded_paths = [Path([12, 8, 7]), Path([12, 8, 9]), Path([12, 8, 13])]
updated_paths = calculate_heuristics(expanded_paths, map, destination_id=9, type_preference=2)
print([path.h for path in updated_paths], [83.45058418010026, 0.0, 28.231188426986208])

expanded_paths = [Path([12, 8, 7]), Path([12, 8, 9]), Path([12, 8, 13])]
updated_paths = calculate_heuristics(expanded_paths, map, destination_id=9, type_preference=3)
print([path.h for path in updated_paths], [0, 0, 1])

def get_station_pairs(stations):
    """
    Generate all possible pairs of stations from a tuple of stations.
    Exclude pairs where both elements are the same station.

    Args:
        stations (tuple): Tuple containing station indices.

    Returns:
        list: List of tuples representing all possible pairs of stations.
    """
    pairs = [(station1, station2) for station1 in map.stations.keys() for station2 in map.stations.keys() if station1 != station2]
    return pairs

# Example usage:
stations_tuple = (1, 2, 3, 4)
pairs = get_station_pairs(stations_tuple)
print(pairs)

stations_tuple = (1, 2, 3, 4)
pairs = get_station_pairs(stations_tuple)

for (station1, station2) in pairs:
    # Do something with the pair of stations
    print(f"Stations: {station1}, {station2}")

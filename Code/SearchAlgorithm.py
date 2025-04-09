# This file contains all the required routines to make an A* search algorithm.
#
__author__ = '1672891'
# _________________________________________________________________________________________
# Intel.ligencia Artificial
# Curs 2023 - 2024
# Universitat Autonoma de Barcelona
# _______________________________________________________________________________________

from SubwayMap import *
from utils import *
import os
import math
import copy


def expand(path, map):
    """
    It expands a SINGLE station and returns the list of class Path.
    Format of the parameter is:
        Args:
            path (object of Path class): Specific path to be expanded
            map (object of Map class):: All the information needed to expand the node
        Returns:
            path_list (list): List of paths that are connected to the given path.
    """
    paths=[]
    for connection in map.connections[path.route[-1]].keys():
        new_path=copy.deepcopy(path)
        new_path.g=path.g
        new_path.add_route(connection)
        paths.append(new_path)
    return paths


def remove_cycles(path_list):
    """
     It removes from path_list the set of paths that include some cycles in their path.
     Format of the parameter is:
        Args:
            path_list (LIST of Path Class): Expanded paths
        Returns:
            path_list (list): Expanded paths without cycles.
    """
    removed_cycles_path_list = []
    for path in path_list:
        if (len(set(path.route)) == len(path.route)):
            removed_cycles_path_list.append(path)
    return removed_cycles_path_list
            
    


def insert_depth_first_search(expand_paths, list_of_path):
    """
     expand_paths is inserted to the list_of_path according to DEPTH FIRST SEARCH algorithm
     Format of the parameter is:
        Args:
            expand_paths (LIST of Path Class): Expanded paths
            list_of_path (LIST of Path Class): The paths to be visited
        Returns:
            list_of_path (LIST of Path Class): List of Paths where Expanded Path is inserted
    """
    for path in expand_paths[::-1]:
        list_of_path.insert(0,path)
    return list_of_path


def depth_first_search(origin_id, destination_id, map):
    """
     Depth First Search algorithm
     Format of the parameter is:
        Args:
            origin_id (int): Starting station id
            destination_id (int): Final station id
            map (object of Map class): All the map information
        Returns:
            list_of_path[0] (Path Class): the route that goes from origin_id to destination_id
    """
    list_of_path = [Path(origin_id)]

    while list_of_path[0].route[-1] != destination_id and list_of_path != []:
        C = list_of_path[0]
        E = expand(C,map)
        E = remove_cycles(E)
        list_of_path = insert_depth_first_search(E,list_of_path[1:].copy())
    
    if list_of_path != []:
        return list_of_path[0]
    
    return []

    


def insert_breadth_first_search(expand_paths, list_of_path):
    """
        expand_paths is inserted to the list_of_path according to BREADTH FIRST SEARCH algorithm
        Format of the parameter is:
           Args:
               expand_paths (LIST of Path Class): Expanded paths
               list_of_path (LIST of Path Class): The paths to be visited
           Returns:
               list_of_path (LIST of Path Class): List of Paths where Expanded Path is inserted
    """
    for path in expand_paths:
        list_of_path.append(path)
    return list_of_path
    


def breadth_first_search(origin_id, destination_id, map):
    """
     Breadth First Search algorithm
     Format of the parameter is:
        Args:
            origin_id (int): Starting station id
            destination_id (int): Final station id
            map (object of Map class): All the map information
        Returns:
            list_of_path[0] (Path Class): The route that goes from origin_id to destination_id
    """
    list_of_path = [Path(origin_id)]
    while list_of_path[0].route[-1] != destination_id and list_of_path != []:
        C = list_of_path[0]
        E = expand(C,map)
        E = remove_cycles(E)
        list_of_path = insert_breadth_first_search(E,list_of_path[1:].copy())
    if list_of_path != []:
        return list_of_path[0]
    return []

"""-------------------------------------------------------SEGONA PART---------------------------------------------------"""

def calculate_cost(expand_paths, map, type_preference=0):
    """
    DONE
         Calculate the cost according to type preference
         Format of the parameter is:
            Args:
                expand_paths (LIST of Paths Class): Expanded paths
                map (object of Map class): All the map information
                type_preference: INTEGER Value to indicate the preference selected:
                                0 - Adjacency
                                1 - minimum Time
                                2 - minimum Distance
                                3 - minimum Transfers
            Returns:
                expand_paths (LIST of Paths): Expanded path with updated cost
    """
    for path in expand_paths:
        if(type_preference < 3):
            if(type_preference==0):
                    cost_g=1
            elif(type_preference==1):
                cost_g=map.connections[path.route[-2]][path.route[-1]]
            elif(type_preference==2):
                if map.stations[path.last]['line']==map.stations[path.route[-2]]['line']:
                    cost_g=map.connections[path.route[-2]][path.last]*map.velocity[map.stations[path.route[-1]]['line']]
                else:
                    cost_g=0
            path.update_g(cost_g)
        elif(type_preference==3):
                if map.stations[path.route[-1]]['line']!=map.stations[path.route[-2]]['line']:
                    cost_g=1
                    path.update_g(cost_g)
    return expand_paths
    
    
def insert_cost(expand_paths, list_of_path):
    """
    DONE
        expand_paths is inserted to the list_of_path according to COST VALUE
        Format of the parameter is:
           Args:
               expand_paths (LIST of Path Class): Expanded paths
               list_of_path (LIST of Path Class): The paths to be visited
           Returns:
               list_of_path (LIST of Path Class): List of Paths where expanded_path is inserted according to cost
    """
    combined_list = list_of_path + expand_paths
    sorted_list = sorted(combined_list, key=lambda x: x.g)
    return sorted_list


def uniform_cost_search(origin_id, destination_id, map, type_preference=0):
    """
     Uniform Cost Search algorithm
     Format of the parameter is:
        Args:
            origin_id (int): Starting station id
            destination_id (int): Final station id
            map (object of Map class): All the map information
            type_preference: INTEGER Value to indicate the preference selected:
                            0 - Adjacency
                            1 - minimum Time
                            2 - minimum Distance
                            3 - minimum Transfers
        Returns:
            list_of_path[0] (Path Class): The route that goes from origin_id to destination_id
    """
    Path_list = [Path(origin_id)]

    while Path_list != [] and (Path_list[0]).last != destination_id:
        C = Path_list.pop(0)
        E = expand(C,map)
        E = remove_cycles(E)
        E = calculate_cost(E, map, type_preference)
        Path_list = insert_cost(E,Path_list)
    if Path_list != []:
        return Path_list[0]
    return []


def calculate_heuristics(expand_paths, map, destination_id, type_preference=0):
    """
     Calculate and UPDATE the heuristics of a path according to type preference
     WARNING: In calculate_cost, we didn't update the cost of the path inside the function
              for the reasons which will be clear when you code Astar (HINT: check remove_redundant_paths() function).
     Format of the parameter is:
        Args:
            expand_paths (LIST of Path Class): Expanded paths
            map (object of Map class): All the map information
            destination_id (int): Final station id
            type_preference: INTEGER Value to indicate the preference selected:
                            0 - Adjacency
                            1 - minimum Time
                            2 - minimum Distance
                            3 - minimum Transfers
        Returns:
            expand_paths (LIST of Path Class): Expanded paths with updated heuristics
    """
    for path in expand_paths:
        h = 0
        if type_preference == 0:  
            if path.route[-1] != destination_id:
                h = 1
        elif type_preference == 1:  
            if path.route[-1] != destination_id:
                distancia = euclidean_dist([map.stations[path.route[-1]]['x'], map.stations[path.route[-1]]['y']], [map.stations[destination_id]['x'], map.stations[destination_id]['y']])
                h = distancia / max(map.velocity.values())
        elif type_preference == 2:
            station_data = map.stations[path.route[-1]]
            dest_data = map.stations[destination_id]
            dist = euclidean_dist([station_data['x'], station_data['y']], [dest_data['x'], dest_data['y']])
            h = dist
        elif type_preference == 3:  
            if map.stations[path.route[-1]]['line'] != map.stations[destination_id]['line']:
                h = 1
        path.update_h(h)
    return expand_paths
    


def update_f(expand_paths):
    """
      Update the f of a path
      Format of the parameter is:
         Args:
             expand_paths (LIST of Path Class): Expanded paths
         Returns:
             expand_paths (LIST of Path Class): Expanded paths with updated costs
    """
    for path in expand_paths:
        path.update_f()
    return expand_paths
    


def remove_redundant_paths(expand_paths, list_of_path, visited_stations_cost):
    """
      It removes the Redundant Paths. They are not optimal solution!
      If a station is visited and have a lower g-cost at this moment, we should remove this path.
      Format of the parameter is:
         Args:
             expand_paths (LIST of Path Class): Expanded paths
             list_of_path (LIST of Path Class): All the paths to be expanded
             visited_stations_cost (dict): All visited stations cost
         Returns:
             new_paths (LIST of Path Class): Expanded paths without redundant paths
             list_of_path (LIST of Path Class): list_of_path without redundant paths
             visited_stations_cost (dict): Updated visited stations cost
    """
    returning_paths = []
    for path in expand_paths:
        current_station = path.route[-1]
        if current_station not in visited_stations_cost or path.g < visited_stations_cost[current_station]:
            visited_stations_cost[current_station] = path.g
            returning_paths.append(path)
    list_of_path = [path for path in list_of_path if path.route[-1] not in visited_stations_cost or path.g <= visited_stations_cost[path.route[-1]]]
    return returning_paths, list_of_path, visited_stations_cost
    


def insert_cost_f(expand_paths, list_of_path):
    """
        expand_paths is inserted to the list_of_path according to f VALUE
        Format of the parameter is:
           Args:
               expand_paths (LIST of Path Class): Expanded paths
               list_of_path (LIST of Path Class): The paths to be visited
           Returns:
               list_of_path (LIST of Path Class): List of Paths where expanded_path is inserted according to f
    """
    combined_list = list_of_path + expand_paths
    sorted_list = sorted(combined_list, key=lambda x: x.f)
    return sorted_list
    


def distance_to_stations(coord, map):
    """
        From coordinates, it computes the distance to all stations in map.
        Format of the parameter is:
        Args:
            coord (list):  Two REAL values, which refer to the coordinates of a point in the city.
            map (object of Map class): All the map information
        Returns:
            (dict): Dictionary containing as keys, all the Indexes of all the stations in the map, and as values, the
            distance between each station and the coord point
    """
    dist_dictionary = {}
    for ids, station in map.stations.items():
        dist_dictionary[ids] = euclidean_dist(coord,[station['x'],station['y']])
    dist_dictionary = dict(sorted(dist_dictionary.items(), key=lambda item: (item[1], item[0])))
    return dist_dictionary


def Astar(origin_id, destination_id, map, type_preference=0):
    """
     A* Search algorithm
     Format of the parameter is:
        Args:
            origin_id (int): Starting station id
            destination_id (int): Final station id
            map (object of Map class): All the map information
            type_preference: INTEGER Value to indicate the preference selected:
                            0 - Adjacency
                            1 - minimum Time
                            2 - minimum Distance
                            3 - minimum Transfers
        Returns:
            list_of_path[0] (Path Class): The route that goes from origin_id to destination_id
"""    
    Path_list = [Path(origin_id)]
    costs_from_already_visited_stations = {}
    
    while Path_list and Path_list[0].route[-1] != destination_id:
        C = Path_list.pop(0)
        E = expand(C, map)
        E = remove_cycles(E)
        E = calculate_cost(E, map, type_preference)
        E = calculate_heuristics(E, map, destination_id, type_preference)
        E = update_f(E)
        E, Path_list, costs_from_already_visited_stations = remove_redundant_paths(E, Path_list, costs_from_already_visited_stations)
        Path_list = insert_cost_f(E, Path_list)
        
    if Path_list:
        return Path_list[0]
    
    return []

    
    
def Astar_improved(origin_coord, destination_coord, map):
    """
     A* Search algorithm
     Format of the parameter is:
        Args:
            origin_coord (list): Two REAL values, which refer to the coordinates of the starting position
            destination_coord (list): Two REAL values, which refer to the coordinates of the final position
            map (object of Map class): All the map information

        Returns:
            list_of_path[0] (Path Class): The route that goes from origin_coord to destination_coord
    """
    
    distance_to_origin = distance_to_stations(origin_coord, map)
    distance_to_dest = distance_to_stations(destination_coord, map)
    map.stations[0]={"name": "origin", "line": -1,"x":origin_coord[0],"y":origin_coord[1], "velocity": 5}
    map.stations[-1]={"name": "destination_", "line": -1,"x":destination_coord[0],"y":destination_coord[1], "velocity": 5}
    map.velocity[-1]= 5
    map.connections[0] = {k: v / 5 for k, v in distance_to_origin.items() if k>0}
    map.connections[0][-1] = euclidean_dist(origin_coord,destination_coord)/5
    for k,v in distance_to_dest.items():
        if k > 0: map.connections[k][-1] = v/5

    return Astar(0, -1, map, 1)
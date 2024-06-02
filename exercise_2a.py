import json
from math import sqrt

FILE_PATH = 'company_locations.man'
CPH = (7, 9)

def load_json_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def find_smallest_office():
    data = load_json_data(FILE_PATH)
    longest_distance = 0
    farthest_point = None

    for _, value in data.items():
        point = (value['x_coordinate'], value['y_coordinate'])
        distance = calculate_distance(CPH, point)
        if(distance > longest_distance):
            longest_distance=distance
            farthest_point= value
    return farthest_point

def calculate_distance(point1, point2):
    return sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    
if __name__ == "__main__":
    office = find_smallest_office()
    print(f"The smallest office is {office['city']} in {office['country']}")


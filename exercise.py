import csv
import json
from math import sqrt
from operator import itemgetter

FILE_PATH = 'company_locations.man'
CPH = (7, 9)

def load_json_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

data = load_json_data(FILE_PATH)

# should calculate all distance, and put in global?

# exercise_2a
def find_smallest_office():

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

# exercise_2c
def get_offices():
    cph_office={'codename':'HQ', 'employees_amount' : 2000}
    offices=[]
    inverted_distances_sum=0
    result = []
 
    #calculate sum of inverted_distances and put every inverted_distance into list. 
    for _, value in data.items():
        point = (value['x_coordinate'], value['y_coordinate'])
        inverse_distance = 1 / calculate_distance(CPH, point)
        inverted_distances_sum += inverse_distance
        offices.append({
            'codename': value['codename'],
            'inverse_distance': inverse_distance
        })
    # calculate every employees amount, and put it into city_info
    for office in offices:
        result.append({
            'codename': office['codename'],
            'employees_amount' : round((office['inverse_distance'] / inverted_distances_sum * 3000), -1)
        })
    
    result.append(cph_office)

    # Sort city_info by employees_amount
    result = sorted(result, key=lambda x: x['employees_amount'])

    # Add ID for each object
    for index, item in enumerate(result):
        new_item = {'id': index}
        new_item.update(item)
        result[index] = new_item
    return result

def save_to_csv(array, filename):
    fieldnames = array[0].keys()
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in array:
            writer.writerow(item)

    
if __name__ == "__main__":
    # Exercise 2a 
    office = find_smallest_office()
    print(f"The smallest office is {office['city']} in {office['country']}")
    
    # Exercise 2b 
    # office= get_offices()
    # save_to_csv(office, 'office_info.csv')

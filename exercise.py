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

# should calculate all distance, and put in global?

# exercise_2a
def find_smallest_office(data):

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

# exercise_2b
def convert(data):
    cph_office={'codename':'HQ', 'employees_amount' : 2000, 'x_coordinate': 7, 'y_coordinate': 9, 'diameter' : 1.2 * (2000 / 1500) ** 0.5}
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
            'inverse_distance': inverse_distance,
            'x_coordinate': value['x_coordinate'],
            'y_coordinate': value['y_coordinate']
        })
    # calculate every employees amount, and put it into city_info
    for office in offices:
        employees_amount = round((office['inverse_distance'] / inverted_distances_sum * 3000), -1)
        diameter = 1.2 * (employees_amount / 1500) ** 0.5
        result.append({
            'codename': office['codename'],
            'employees_amount' : employees_amount,
            'x_coordinate': value['x_coordinate'],
            'y_coordinate': value['y_coordinate'],
            'diameter' : diameter
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
    data = load_json_data(FILE_PATH)
    # Exercise 2a 
    # office = find_smallest_office(data)
    # print(f"The smallest office is {office['city']} in {office['country']}")
    
    # Exercise 2b 
    offices = convert(data)
    # necessary_data_csv = [{'codename': item['codename'], 'employees_amount': item['employees_amount']} for item in offices]
    # save_to_csv(necessary_data_csv, 'offices_info.csv')

    # Exercise 2c
    print(offices)


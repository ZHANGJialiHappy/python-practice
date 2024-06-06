import csv
import json
from math import sqrt

from matplotlib import pyplot as plt

from invitation_module import read_csv_and_generate_invivations

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
    cph_office={'codename':'HQ', 'employees_amount' : 2000, 'x_coordinate': 7, 'y_coordinate': 9, 'diameter' : 1.2 * (2000 / 1500) ** 0.5, 'city' : 'Copenhagen', 'country': "Denmark", 'distance': 0}
    offices=[]
    inverted_distances_sum=0
    result = []
 
    #calculate sum of inverted_distances and put every inverted_distance into list. 
    for _, value in data.items():
        point = (value['x_coordinate'], value['y_coordinate'])
        distance=calculate_distance(CPH, point)
        inverse_distance = 1 / distance
        inverted_distances_sum += inverse_distance
        offices.append({
            'codename': value['codename'],
            'inverse_distance': inverse_distance,
            'x_coordinate': value['x_coordinate'],
            'y_coordinate': value['y_coordinate'],
            'city': value['city'],
            'country': value['country'],
            'distance': distance
        })
    # calculate every employees amount, and put it into city_info
    for office in offices:
        employees_amount = round((office['inverse_distance'] / inverted_distances_sum * 3000), -1)
        diameter = 1.2 * (employees_amount / 1500) ** 0.5
        result.append({
            'codename': office['codename'],
            'employees_amount' : employees_amount,
            'x_coordinate': office['x_coordinate'],
            'y_coordinate': office['y_coordinate'],
            'diameter' : diameter,
            'city': office['city'],
            'country' : office['country'],
            'distance': office['distance']
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
    if isinstance(array, dict):
        array = list(array.values())

    fieldnames = array[0].keys()
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in array:
            writer.writerow(item)

# Exercise 2c

def save_to_image(data, filename):

    fig, ax = plt.subplots(figsize=(8, 8))

    for item in data:
        id = item['id']
        x = item['x_coordinate']
        y = item['y_coordinate']
        diameter = item['diameter']
        codename = item['codename']
        employees_amount = item['employees_amount']
        label = f"{id},{codename}={employees_amount}"
        # Plot the point
        ax.scatter(x, y, label=label)

        # Draw the circle
        circle = plt.Circle((x, y), diameter / 2, color='blue', fill=False)
        ax.add_artist(circle)

        # Annotate the point with its codename
        ax.annotate(codename, (x, y), textcoords="offset points", xytext=(0,10), ha='center')

    # Set limits for x and y axis
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)

    # Add grid
    ax.grid(True)

    # Add labels and title
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("Locations of the offices")

    # Add legend
    plt.legend()

    # Save plot as an image
    plt.savefig(filename)

    # Show plot
    plt.show()


# Exercise 2d
def party_info(data, party_point):
    result = {}
    for value in data:
        result[value['codename']] = {
            'A': value['city'],
            'B': value['country'],
            'C': party_point[0],
            'D': party_point[1],
            'E': value['distance']*100,
            'employees_amount': value['employees_amount']
        }
    return result


if __name__ == "__main__":
    data = load_json_data(FILE_PATH)
    # Exercise 2a 
    # office = find_smallest_office(data)
    # print(f"The smallest office is {office['city']} in {office['country']}")
    
    # Exercise 2b 
    # offices = convert(data)
    # necessary_data_csv = [{'codename': item['codename'], 'employees_amount': item['employees_amount']} for item in offices]
    # save_to_csv(necessary_data_csv, 'exercise_2b.csv')

    # Exercise 2c
    # offices = convert(data)
    # necessary_data_image=[{'codename': item['codename'], 'employees_amount': item['employees_amount'], 'x_coordinate': item['x_coordinate'], 'y_coordinate': item['y_coordinate'], 'diameter': item['diameter']} for item in offices]
    # save_to_image(offices,"exercise_2c.png")

    # Exercise 2d
    # offices = convert(data)
    # party_point= CPH
    # necessary_data_party=party_info(offices, party_point)
    # print(necessary_data_party)
    # save_to_csv(necessary_data_party, 'exercise_2d.csv')

    # Exercise 2e
    '''
    If the dinner cost 500dkk per employee, what is the total cost for the company
    Answer: 
        we should know the responds of the employees, so that we know how many people will attend the party.
        max: 500dkk*5000 = 2500000 dkk
    '''

    #  Exercise 2f
    offices = convert(data)
    party_point= CPH
    necessary_data_party=party_info(offices, party_point)
    save_to_csv(necessary_data_party, 'exercise_2d.csv')
    csv_filename='exercise_2d.csv'
    read_csv_and_generate_invivations(csv_filename)
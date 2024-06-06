# How to start?

1. pip install -r requirements.txt
2. open the file exercise.py, or warm_up_exercise.py for the warm_up exercise
3. check the result: codes to generate answers are after "if \_\_name\_\_ == "\_\_main\_\_":", not comment out the related code to check the answer.

# explanation of answers

## exercise 2a

scan the whole data -> caculate the distance between Copenhagen and each office -> record the farthest office -> return it(farthest office have least employee amount)

## exercise 2b

1. develpe a **reuseable function** convert(data): scan the whole data -> calculate inverted_distances_sum, put inverse_distance, codename and other infomation (it will be needed in other exercises) into offices[] -> scan offices[] append calculated diameter and employees_amount and other infos into result[] -> append cph_office to result[] (because employee amount of cph is constant) -> sort by employees_amount -> add id in ascending order
2. develop a **reuseable function** save_to_csv(array, filename). It can accept array or dict, then write information into csv file

## Exercise 2c

1. import pyplot from matplotlib
2. develop save_to_image(data, filename) within pyplot
3. extract the necessary data from convert(data)
4. pass the necessary data into save_to_image()

## Exercise 2d

1. develop party_info(data, party_point): add related information from convert(data) and the coordination of the place holding party, reimburse should the distance\*100, the returned data should be **dict**
2. pass the party_info(data, party_point) to save_to_csv(data, filename)

## Exercise 2e

If I understand exercise correctly, calculate by heard.

## Exercise 2f

1. create invitation_module.py for the class and function about invitation.
2. create invitation class to generate invitations
3. create read_csv_and_generate_invivations(filename) to read file created by exercise 2d, then use the information of 2d to generate invitation -> write them into txt file

## Exercise 2g

What's the given format of coordination? coordinates (7,9)?

1. develop function total_travel_distance_from_location(location, data) to calculate the total travel distance of all employees between the given location and other location.
2. develop find_optimal_location(data) to scan all data -> calculate all total_travel_distance_from_location -> find the smallest total_travel_distance_from_location (it's where to holde party) -> print coorination into txt file

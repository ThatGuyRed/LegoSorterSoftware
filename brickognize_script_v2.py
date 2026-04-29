import cv2
import requests
import json
import time
import csv
import datetime
import os  # DELETE

# public variables
brick_counter = 0

categories = {
    "Standard Bricks and Plates": 1,
    "Tiles and Slopes": 2,
    "Minifigures, Animals, and Figures": 3,
    "Technic and Mechanical Parts": 4,
    "Vehicles and Transportation": 5,
    "Windows, Doors, and Architectural Elements": 6,
    "Specialized and Miscellaneous Parts": 7,
    "BIONICLE and Hero Factory": 8,

    # THIS HAS BEEN REMOVED FROM categories.csv (merged with 7)
    "Miscellaneous and Promotional Items": 9,

    # This does not exist in categories.csv
    "Unrecognized (DUPLO)": 10
}


# Read categories from categories.csv
reader = csv.DictReader(open('categories.csv', 'r', newline=''))
categories_mapping = list(reader)


def get_category_number(category):
    """ Returns category number of an item
    Args:
        Category (list(dictionary)): A list of dictionaries.

    Returns:
        ???
    """
    for item in categories_mapping:
        if item['name'] == category:
            # print(f"Category name: {item['name']}, Category number: {item[category]}")
            return item['category']
    return 9


def capture_image():
    """ Captures image and stores it to the local filesystem.
    Returns:
        filename (string): Output file name.
    """
    filename = 'lego_piece' + datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f") + ".jpg"
    # Open defualt video capture device. 0 is the default camera]
    cap = cv2.VideoCapture(0)

    # If camera cannot be opened, run this code.
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return -1

    ret, frame = cap.read()
    cap.release()

    if brick_counter == 0:
        cv2.imwrite(filename, frame)  # Writes image to file system
        cv2.imshow('Captured Image', frame)
        # cv2.waitKey(0)  # Wait for a key press to close the window
        cv2.destroyAllWindows()
    return filename


def recognize_lego_piece(image_path):
    """ Queries the Brickognize API for piece information.
    Args:
        image_path (str): Path of an image.

    Returns:
        category_number (str): Category number of the recognized piece.
        piece_name (str): Name of the recognized piece.
        piece_img (str): URL to an image of the category_numberognized piece.
        piece_id (str): ID of the recognized piece.

    """
    url = 'https://api.brickognize.com/predict'  # Updated API endpoint
    files = {'query_image': (image_path, open(image_path, 'rb'), 'image/jpeg')}
    headers = {'accept': 'application/json'}
    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        result = response.json()
        print('Full response:', result)

        if 'items' in result and len(result['items']) > 0:
            collection = result['items'][0]
            category_name = collection['category']
            piece_name = collection['name']
            piece_img = collection['img_url']
            piece_id = collection['id']

            print('\nDEBUG INFO', '\nURL: ', piece_img, '\nName: ',
                  piece_name, '\nID: ', piece_id, '\n')  # debug

            category_number = get_category_number(category_name)

            return int(category_number), piece_name, piece_img, piece_id
        else:
            # Default to Miscellaneous and Promotional Items if no items found
            category_number = 9
            return 9, -1, -1, -1
    else:
        print('Error:', response.status_code, response.text)
        category_number = 10
        return 10, -1, -1, -1


# Placeholder size, used to check max index
num_containers = 9
# This should be an array storing dictionaries [key: piece_id] storing class scan_piece (class contains piece info) and count
containers = []
for i in range(num_containers):
    containers.append({})

# Dictionary has built in hashing
# O(1) time complexity for updating, checking.
# O(n) when iterating; fetch all/copying


def store_data(data, container):
    """ Stores brick info in a dictionary.
    Args:
        data (scan_piece): Piece data.
        container (int): Container the piece will go in.
    Returns:
        None.
    """
    # This probably doesn't work
    key = data.piece_id
    if (key in containers[container]):
        containers[container][key].increment()
    else:
        containers[container][key] = data
# Need some sort of output for stored data


def print_data():
    for container in containers:
        if container:  # Empty check
            print('Container ', containers.index(container), ':\n')
            for key in container:
                data = container[key]
                print('key:', key, ', name:', data.piece_name,
                      ', count:', data.count, '\n')


def sort_piece(category_number):
    # Implement your sorting logic here
    sort_piece_action(category_number)


def sort_piece_action(category_number):
    # Implement your sorting logic (ELECTRONICS)
    # For example, control motors or actuators to direct the piece to the correct bin
    print(f"Sorting piece into category number: {category_number}")


class scan_piece:
    def __new__(cls):
        return super(scan_piece, cls).__new__(cls)

    def __init__(self):
        # Run image recognition in a loop for now
        self.run = True
        self.count = 1
        while self.run:

            self.image_path = capture_image()  # Run capture image method
            if self.image_path == -1:
                self.run = False

            self.category_number, self.piece_name, self.piece_img, self.piece_id = recognize_lego_piece(
                self.image_path)  # Run image recognition

            # Get data
            # category_number, name, img, id = recognize_lego_piece(image_path)
            if (self.category_number != 10):
                sort_piece(self.category_number)
                '''
                all functionality relating to brick_counter should be moved to app.py or a separate class?
                '''
                # global brick_counter  # Increment the brick counter
                # brick_counter += 1
                # print(f"Total bricks logged: {brick_counter}", flush=True)
                # Stops the while loop (move this elsewhere when we need the program to run more than one iteration)
                self.run = False
            time.sleep(1)  # Add a delay to avoid overwhelming the API

            # Cleanup
            os.remove(self.image_path)

    def increment(self):
        self.count = self.count + 1

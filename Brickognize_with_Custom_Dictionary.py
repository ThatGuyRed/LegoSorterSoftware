import cv2
import requests
import json
import time
import csv

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


def capture_image(cap, filename='lego_piece.jpg'):
    """ Captures image and stores it to the local filesystem.
    Args:
        cap (???): ???
        filename (str): Output file name.

    Returns:
        filename (string): Output file name.
    """
    ret, frame = cap.read()
    cap.release()

    if brick_counter == 0:
        cv2.imwrite(filename, frame)  # Writes image to file system
        cv2.imshow('Captured Image', frame)

        # cv2.waitKey(0)  # Wait for a key press to close the window

        cv2.destroyAllWindows()

    return filename


def recognize_lego_piece(image_path):
    url = 'https://api.brickognize.com/predict'  # Updated API endpoint
    files = {'query_image': (image_path, open(image_path, 'rb'), 'image/jpeg')}
    headers = {'accept': 'application/json'}
    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        result = response.json()
        print('Full response:', result)

        if 'items' in result and len(result['items']) > 0:
            # All the important data we want on the frontend
            #
            # Issue: If the API does not return items,
            #        the code below bugs out
            #
            collection = result['items'][0]
            category_name = collection['category']
            piece_name = collection['name']
            piece_img = collection['img_url']
            piece_id = collection['id']

            print('\nDEBUG INFO', '\nURL: ', piece_img, '\nName: ',
                  piece_name, '\nID: ', piece_id, '\n')  # debug

            category_number = get_category_number(category_name)
            # print('\nDEBUG INFO', '\nURL: ', piece_img, '\nName: ',
            #     piece_name, '\nID: ', piece_id, '\n')  # debug
            # return category_number, piece_name, piece_img, piece_id
            return int(category_number), piece_name, piece_img, piece_id
        # This else block might not do anything
        else:
            # Default to Miscellaneous and Promotional Items if no items found
            # return 9
            category_number = 9
            # This will almost certainly bug out the code when we have a category 9
            return 9, -1, -1, -1
    else:
        print('Error:', response.status_code, response.text)
        category_number = 10
        return 10, -1, -1, -1


def sort_piece(category_number):
    # Implement your sorting logic here
    # For example, control motors or actuators to direct the piece to the correct bin
    print(f"Sorting piece into category number: {category_number}")


def exec():
    # Note: We might want to have a separate method to call main() in loop, possibly linked to cv2 functionality

    # Run image recognition in a loop for now
    run = True
    while run:

        # Open defualt video capture device. 0 is the default camera]
        cap = cv2.VideoCapture(0)

        # If camera cannot be opened, run this code.
        if not cap.isOpened():
            print("Error: Could not open camera.")
            return

        image_path = capture_image(cap)  # Run capture image method
        category_number, piece_name, piece_img, piece_id = recognize_lego_piece(
            image_path)  # Run image recognition

        # Get data
        # category_number, name, img, id = recognize_lego_piece(image_path)
        print("sfsfsdf", piece_img)
        if (category_number != 10):
            sort_piece(category_number)
            global brick_counter  # Increment the brick counter
            brick_counter += 1
            print(f"Total bricks logged: {brick_counter}", flush=True)
            run = False
        time.sleep(1)  # Add a delay to avoid overwhelming the API
    # Stops the while loop (move this elsewhere when we need the program to run more than one iteration)

    return category_number, piece_name, piece_img, piece_id

# DEBUG, doesn't do anything


def main():
    exec()


class scan_piece:
    def __new__(cls):
        return super(scan_piece, cls).__new__(cls)

    def __init__(self):
        self.category_number, self.piece_name, self.piece_img, self.piece_id = exec()


if __name__ == '__main__':
    main()

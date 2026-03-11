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
    "Miscellaneous and Promotional Items": 9,
    "Unrecognized (DUPLO)": 10
}


# Read categories from categories.csv
# Note: categories.csv does not contain "Unrecognized (DUPLO)"
reader = csv.DictReader(open('categories.csv', 'r', newline=''))
categories_mapping = list(reader)


def get_category_number(category):
    for item in categories_mapping:
        if item['name'] == category:
            # print(f"Category name: {item['name']}, Category number: {item[category]}")
            return item['category']


def capture_image(cap, filename='lego_piece.jpg'):
    ret, frame = cap.read()
    cap.release()

    if brick_counter == 0:
        cv2.imwrite(filename, frame)
        cv2.imshow('Captured Image', frame)
        cv2.waitKey(0)  # Wait for a key press to close the window
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
            category_name = result['items'][0]['category']
            category_number = get_category_number(category_name)
            return category_number
        else:
            return 9  # Default to Miscellaneous and Promotional Items if no items found
    else:
        print('Error:', response.status_code, response.text)
        return 10


def sort_piece(category_number):
    # Implement your sorting logic here
    # For example, control motors or actuators to direct the piece to the correct bin
    print(f"Sorting piece into category number: {category_number}")


def main():
    # Open defualt video capture device. 0 is the default camera]
    cap = cv2.VideoCapture(0)

    # If camera cannot be opened, run this code.
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Run image recognition in a loop for now
    while True:
        image_path = capture_image(cap)  # Run capture image method

        if image_path:
            category_number = recognize_lego_piece(image_path)
            sort_piece(category_number)

            global brick_counter  # Increment the brick counter
            brick_counter += 1
            print(f"Total bricks logged: {brick_counter}", flush=True)
        time.sleep(1)  # Add a delay to avoid overwhelming the API


if __name__ == '__main__':
    main()

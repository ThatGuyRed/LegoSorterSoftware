# Lego Sorter Repository

## The files and what they do:

<code>Brickognize_with_Custom_Dictionary.py</code>
- The main program, contains the following components:
  - CSV reader
    - Status: Complete
      - Description: Reads .csv file(s) containing:
        - Brick categories
  - Function to retrieve category number
  - Function to capture images & write to fs
  - Function to interface with the Brickognize API
  - Function to sort pieces by category number
    - Status: Incomplete
      - Awaiting mechanical & electrical components

<code>app.py</code>
- Graphical User Interface (GUI) written with the PyQt6 library.
  - The UI can be designed graphically using the Qt Widgets Designer
    - Qt Widgets Designer download: 
      Arch Linux: qt6-tools
      **please add package source for your OS here**
    - The .ui file will have to be converted into .py in order to allow for it to be imported as a python class:
    ```shell
      pyside6-uic <filename>.ui -o <filename>.py
    ```
      You will need the <code>pyside6-uic</code> package for this conversion.
    - Actions of UI elements should be called from within <code>app.py</code>, and under no circumstance should the <code>main.py</code> be modified manually.



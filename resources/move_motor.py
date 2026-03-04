positions = 12

## 24 possible positions
## 
current_position = 0

def moveTo(position):
    steps_needed = (position - current_position)
    return steps_needed
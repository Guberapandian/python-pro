from datetime import datetime

# Function to map named colors to hex codes
def get_color_hex(color_name):
    colors = {
        "black": "000000",
        "red": "ff0000",
        "green": "00ff00",
        "yellow": "ffff00",
        "blue": "0000ff",
        "magenta": "ff00ff",
        "cyan": "00ffff",
        "white": "ffffff"
    }
    return colors.get(color_name.lower(), color_name)  # If not found, assume it's a hex color

# Convert hex color to RGB values
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# ANSI escape code for setting background color using RGB values
def rgb_bg_color(rgb_color):
    return f"\033[48;2;{rgb_color[0]};{rgb_color[1]};{rgb_color[2]}m"

# ANSI escape code for setting text color using RGB values
def rgb_text_color(rgb_color):
    return f"\033[38;2;{rgb_color[0]};{rgb_color[1]};{rgb_color[2]}m"

# Function to print the details with custom text and background colors using ANSI codes
def print_details(name, id_no, id_text_color, id_background_color, due_date_str):
    # Convert due date string to date object
    due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
    today = datetime.today().date()

    # Convert input to either hex or RGB color
    id_background_color = get_color_hex(id_background_color)
    id_text_color = get_color_hex(id_text_color)

    # If due date is overdue, use the custom hex color 'fa00bc' for the background
    if due_date < today:
        rgb_bg = hex_to_rgb('fa00bc')  # Custom color for overdue
        bg_color_code = rgb_bg_color(rgb_bg)
        id_no = ''  # Hide ID number for overdue entries
    else:
        # Use the user-provided background color (if the due date is valid)
        rgb_bg = hex_to_rgb(id_background_color)
        bg_color_code = rgb_bg_color(rgb_bg)

    # Convert text color to ANSI escape code
    rgb_text = hex_to_rgb(id_text_color)
    text_color_code = rgb_text_color(rgb_text)

    # ANSI escape code for resetting color
    reset_color = "\033[0m"

    # Print details
    print(f"Name                 : {name}")
    print(f"Due Date             : {due_date_str} ({'Overdue' if due_date < today else 'Upcoming'})")

    # Print the text and background color (with or without ID based on overdue status)
    if id_no:  # If ID number exists, print with background and text color
        print(f"ID Text colour       : {text_color_code}{bg_color_code}{id_no}{reset_color}")
    else:  # If overdue, print background color only (no ID number)
        print(f"ID Text colour       : {bg_color_code}          {reset_color}")

# Input from user
name = input("Enter Name: ")
id_no = input("Enter ID No: ")
id_text_color = input("Enter ID Text Colour (e.g., red, green, blue): ").strip()
id_background_color = input("Enter ID Background Colour (hex or name, e.g., fa00bc or blue): ").strip()
due_date = input("Enter Due Date (YYYY-MM-DD): ").strip()

# Call the function to print the details
print_details(name, id_no, id_text_color, id_background_color, due_date)

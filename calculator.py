import tkinter as tk


def translate_region(old_res, new_res, old_coords):
    # Calculate the scale factor between the old and new resolutions
    scale_factor = new_res[0] / old_res[0]

    # Calculate the new coordinates of the region in the new resolution
    new_left = round(old_coords[0] * scale_factor)
    new_top = round(old_coords[1] * scale_factor)
    new_width = round(old_coords[2] * scale_factor)
    new_height = round(old_coords[3] * scale_factor)

    # Return the new coordinates as a tuple
    return new_left, new_top, new_width, new_height


def translate_point(old_res, new_res, old_point):
    # Calculate the scale factor between the old and new resolutions
    scale_factor_x = new_res[0] / old_res[0]
    scale_factor_y = new_res[1] / old_res[1]

    # Calculate the new coordinates of the point in the new resolution
    new_x = round(old_point[0] * scale_factor_x)
    new_y = round(old_point[1] * scale_factor_y)

    # Return the new coordinates as a tuple
    return new_x, new_y


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Resolution Calculator")
        self.master.geometry("600x500")

        # Create input fields for screen size and region coordinates
        self.screen_width_label = tk.Label(self.master, text="Current Reso X:")
        self.screen_width_label.grid(row=0, column=0, padx=5, pady=5)
        self.screen_width_entry = tk.Entry(self.master)
        self.screen_width_entry.insert(0, "-1")  # Set default value to -1
        self.screen_width_entry.grid(row=0, column=1, padx=5, pady=5)

        self.screen_height_label = tk.Label(self.master, text="Current Reso Y:")
        self.screen_height_label.grid(row=1, column=0, padx=5, pady=5)
        self.screen_height_entry = tk.Entry(self.master)
        self.screen_height_entry.insert(0, "-1")  # Set default value to -1
        self.screen_height_entry.grid(row=1, column=1, padx=5, pady=5)

        self.region_x_label = tk.Label(self.master, text="Coords X:")
        self.region_x_label.grid(row=2, column=0, padx=5, pady=5)
        self.region_x_entry = tk.Entry(self.master)
        self.region_x_entry.insert(0, "-1")  # Set default value to -1
        self.region_x_entry.grid(row=2, column=1, padx=5, pady=5)

        self.region_y_label = tk.Label(self.master, text="Coords Y:")
        self.region_y_label.grid(row=3, column=0, padx=5, pady=5)
        self.region_y_entry = tk.Entry(self.master)
        self.region_y_entry.insert(0, "-1")  # Set default value to -1
        self.region_y_entry.grid(row=3, column=1, padx=5, pady=5)

        self.region_top_label = tk.Label(self.master, text="Region top:")
        self.region_top_label.grid(row=4, column=0, padx=5, pady=5)
        self.region_top_entry = tk.Entry(self.master)
        self.region_top_entry.insert(0, "-1")  # Set default value to -1
        self.region_top_entry.grid(row=4, column=1, padx=5, pady=5)

        self.region_left_label = tk.Label(self.master, text="Region left:")
        self.region_left_label.grid(row=5, column=0, padx=5, pady=5)
        self.region_left_entry = tk.Entry(self.master)
        self.region_left_entry.insert(0, "-1")  # Set default value to -1
        self.region_left_entry.grid(row=5, column=1, padx=5, pady=5)

        self.region_width_label = tk.Label(self.master, text="Region width:")
        self.region_width_label.grid(row=6, column=0, padx=5, pady=5)
        self.region_width_entry = tk.Entry(self.master)
        self.region_width_entry.insert(0, "-1")  # Set default value to -1
        self.region_width_entry.grid(row=6, column=1, padx=5, pady=5)

        self.region_height_label = tk.Label(self.master, text="Region height:")
        self.region_height_label.grid(row=7, column=0, padx=5, pady=5)
        self.region_height_entry = tk.Entry(self.master)
        self.region_height_entry.insert(0, "-1")  # Set default value to -1
        self.region_height_entry.grid(row=7, column=1, padx=5, pady=5)

        # Create input fields for target resolution
        self.target_width_label = tk.Label(self.master, text="Target Reso X:")
        self.target_width_label.grid(row=0, column=2, padx=5, pady=5)
        self.target_width_entry = tk.Entry(self.master)
        self.target_width_entry.insert(0, "-1")  # Set default value to -1
        self.target_width_entry.grid(row=0, column=3, padx=5, pady=5)

        self.target_height_label = tk.Label(self.master, text="Target Reso Y:")
        self.target_height_label.grid(row=1, column=2, padx=5, pady=5)
        self.target_height_entry = tk.Entry(self.master)
        self.target_height_entry.insert(0, "-1")  # Set default value to -1
        self.target_height_entry.grid(row=1, column=3, padx=5, pady=5)

        # Create button to perform the calculation
        self.calculate_button = tk.Button(self.master, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=8, column=1, padx=5, pady=5)

        # Create label to display the result
        self.result_label = tk.Label(self.master, text="")
        self.result_label.grid(row=9, column=1, padx=5, pady=5)

    def calculate(self):
        # Get input values
        screen_width = int(self.screen_width_entry.get())
        screen_height = int(self.screen_height_entry.get())
        coords_x = int(self.region_x_entry.get())
        coords_y = int(self.region_y_entry.get())
        region_top = int(self.region_top_entry.get())
        region_left = int(self.region_left_entry.get())
        region_width = int(self.region_width_entry.get())
        region_height = int(self.region_height_entry.get())
        target_width = int(self.target_width_entry.get())
        target_height = int(self.target_height_entry.get())

        # Calculate scaling factors
        x_scale = target_width / screen_width
        y_scale = target_height / screen_height

        if (coords_x == -1 or coords_y == -1) and (
                region_top != -1 and region_width != -1 and
                region_left != -1 and region_height != -1):
            # Calculate new region coordinates and dimensions
            left, top, width, height = translate_region((screen_width, screen_height), (target_width, target_height),
                                                        (region_left, region_top, region_width, region_height))
            # Display the result
            result_text = f"New region coordinates: ({top}, {left}, {width}, {height})"
            self.result_label.config(text=result_text)
        elif (coords_x != -1 and coords_y != -1) and (
                region_top == -1 and region_width == -1 and
                region_left == -1 and region_height == -1):
            # Calculate new region coordinates and dimensions
            new_x, new_y = translate_point((screen_width, screen_height), (target_width, target_height),
                                           (coords_x, coords_y))
            # Display the result
            result_text = f"New coordinates: ({new_x}, {new_y})"
            self.result_label.config(text=result_text)
        else:
            # Display the result
            result_text = "Bad info given.."
            self.result_label.config(text=result_text)


root = tk.Tk()
app = Calculator(root)
root.mainloop()

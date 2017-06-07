"""This module is used for the calculation and generation of
coordinates used to create a cross section of a topography image"""

class CrossSection:
    """Main class for the return of coordinates"""
    def __init__(self):
        """Initialise variables"""
        self.top_coordinates = []
        self.bottom_coordinates = []
        self.image_size = []

    def reset_coordinates(self):
        """Delete all stored coordinates"""
        self.top_coordinates = []
        self.bottom_coordinates = []
        self.image_size = []

    def return_coordinates(self, return_x=True, return_y=True, return_image=True):
        """Returns the coordinates or heights"""
        response = []
        if return_x:
            response.append(self.top_coordinates)
        if return_y:
            response.append(self.bottom_coordinates)
        if return_image:
            response.append(self.image_size)
        return response

    def calculate(self, path):
        """Calculate the cross section"""
        graph = SectionCalculation()
        graph.open_image(path)
        graph.graph_heights()
        coordinates = graph.calculate_coordinates()
        self.image_size = graph.get_image()
        self.top_coordinates = coordinates[0]
        self.bottom_coordinates = coordinates[1]


class SectionCalculation:
    """Main class for the generation of coordinates"""
    def __init__(self):
        """Initialise variables"""
        self.topography_darkness = []
        self.highest = 0
        self.image = None

    def return_darkness(self):
        """Returns the list of pixel scores"""
        return self.topography_darkness

    def open_image(self, path):
        """Opens the image from path and gets depth of each pixel"""
        self.image = ImgLoad.open(path)
        self.image.rotate(180)
        topography = self.image.load()
        for x_image in reversed(range(0, self.image.size[0])):
            self.topography_darkness.append([])
            #Change to swap what side of the image
            for y_image in range(0, int(self.image.size[1])):
                x_var = self.image.size[0]-x_image-1
                self.topography_darkness[x_var].append(topography[x_var, y_image])
        self.image.close()

    def graph_heights(self):
        """Calculates the highest point and lowest"""
        for rows in range(len(self.topography_darkness)):
            pin_high = max(self.topography_darkness[rows])
            if pin_high > self.highest:
                self.highest = pin_high

        for rows in range(len(self.topography_darkness)):
            for pins in range(len(self.topography_darkness[rows])):
                self.topography_darkness[rows][pins] = int(
                    (self.topography_darkness[rows][pins]/self.highest)*100)

    def get_image(self):
        """Returns the size of the image"""
        return (self.image.size[0], int(self.image.size[1]))

    def calculate_coordinates(self):
        """Returns the coordinates for Tkinter Generation"""
        a_coordinates = []
        b_coordinates = []

        for rows in range(0, len(self.topography_darkness)):
            for darkness in range(0, len(self.topography_darkness[rows])):
                a_coordinates.append([darkness+rows, 100-self.topography_darkness[rows][darkness]])
                b_coordinates.append([darkness+rows, 100])

        return [a_coordinates, b_coordinates]

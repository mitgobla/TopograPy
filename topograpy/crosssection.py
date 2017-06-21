from PIL import Image as ImgLoad

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

    def calculate(self, image_path, graph):
        """Calculate the cross section"""
        graph.open_image(image_path)
        graph.graph_heights()
        coordinates = graph.calculate_coordinates()
        self.image_size = graph.get_image()
        self.top_coordinates = coordinates[0]
        self.bottom_coordinates = coordinates[1]

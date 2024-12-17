class Figure:

    @property
    def get_area(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("not a Figure")
        return self.get_area + other_figure.get_area

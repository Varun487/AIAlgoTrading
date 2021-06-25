from ..Utils.converter import Converter


class Visualization(object):
    def __init__(self, df=None, columns=None, height=-1, width=-1):
        self.df = df
        self.height = height
        self.width = width
        self.columns = columns

        self.valid_df = False
        self.valid_height = False
        self.valid_width = False
        self.valid_columns = False
        self.valid = False

    def validate_height(self):
        self.valid_height = (type(self.height) == int) and (self.height > 0)

    def validate_width(self):
        self.valid_width = (type(self.width) == int) and (self.width > 0)

    def validate_columns(self):
        self.valid_columns = (self.columns is not None) and (type(self.columns) == list)

    def validate_df(self):
        self.valid_df = (Converter(df=self.df).validate_df()) and (set(self.columns) == set(self.df.columns))

    def validate(self):
        self.validate_height()
        self.validate_width()
        self.validate_columns()
        if self.valid_columns:
            self.validate_df()
        self.valid = self.valid_height and self.valid_width and self.valid_columns and self.valid_df

    def generate_visualization(self):
        pass

    def get_visualization(self):
        self.validate()
        if self.valid:
            return self.generate_visualization()
        else:
            raise ValueError("One of the inputs given are invalid!")

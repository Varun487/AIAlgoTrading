import pandas as pd


class Converter(object):
    """Used to covert a list of DB objects to a DataFrame and vice versa"""

    def __init__(self, df=None, obj_list=None):
        self.df = df
        self.obj_list = obj_list
        self.__is_valid_obj_list = None
        self.__is_valid_df = None

    def validate_obj_list(self):
        return (self.obj_list is not None) and (type(self.obj_list) == list) and (self.obj_list != [])

    def __set_is_valid_obj_list(self):
        self.__is_valid_obj_list = self.validate_obj_list()

    def __get_df(self):
        # Decide columns
        columns = list(self.obj_list[0].__dict__)
        columns.remove('_state')

        # Initialize empty df
        df = pd.DataFrame(columns=columns)

        # create dictionary to hold data
        obj_data = {}
        for col in columns:
            obj_data[col] = []

        # populate dictionary
        for obj in self.obj_list:
            for attr in obj.__dict__:
                if attr != "_state":
                    obj_data[attr].append(obj.__dict__[attr])

        # populate df
        for col in obj_data:
            df[col] = obj_data[col]

        return df

    def to_df(self):
        # Ensure object list is valid
        self.__set_is_valid_obj_list()

        # return df
        if self.__is_valid_obj_list:
            self.df = self.__get_df()
            return self.df

        else:
            raise ValueError("Object List given is not valid! Ensure that the object list is of type 'list' and is not empty.")

    def validate_df(self):
        return (self.df is not None) and (type(self.df) == pd.DataFrame) and (not self.df.empty)

    def __set_is_valid_df(self):
        self.__is_valid_df = self.validate_df()

    def __get_obj_list(self, base_obj):

        # initialize object list
        obj_list = []

        # create object list
        for row in range(len(self.df)):

            # create temp dict to store object attr
            temp = {}
            for col in self.df.columns:
                # print(col)
                temp[col] = self.df[col][row]

            obj_list.append(base_obj(**temp))

        return obj_list

    def to_obj_list(self, base_obj):
        # Ensure df is valid
        self.__set_is_valid_df()

        # return obj_list
        if self.__is_valid_df:
            self.obj_list = self.__get_obj_list(base_obj)
            return self.obj_list

        else:
            raise ValueError("DataFrame given is not valid! Ensure that the object list is of the correct type and is not empty.")

from .converter import Converter


class Getter(object):
    '''Used to get data from the database according to parameters'''

    def __init__(self, table_name=None, df_flag=False, param_list=None):
        self.table_name = table_name
        self.param_list = param_list

        self.__is_valid_param_list = None
        self.__is_valid_table_name = None

        self.df_flag = df_flag
        self.df = None
        self.obj_list = None

    def validate_df_flag(self):
        return self.df_flag in [True, False]

    def validate_param_list(self):
        return (self.param_list is not None) and (type(self.param_list) == dict) and (self.param_list != {})

    def validate_table_name(self):
        return self.table_name is not None

    def __set_is_valid_param_list(self):
        self.__is_valid_param_list = self.validate_param_list()

    def __set_is_valid_table_name(self):
        self.__is_valid_table_name = self.validate_table_name()

    def __set_df_flag(self):
        if not self.validate_df_flag():
            self.df_flag = False

    def get_data(self):
        self.__set_df_flag()
        self.__set_is_valid_table_name()
        self.__set_is_valid_param_list()

        if self.__is_valid_table_name and self.__is_valid_param_list:
            try:
                obj_list = list(self.table_name.objects.filter(**self.param_list))

                if self.df_flag:
                    return Converter(obj_list=obj_list).to_df()
                else:
                    return obj_list

            except Exception as e:
                raise TypeError(f"Incorrect parameters given! {e}")

        else:
            raise TypeError("Incorrect table name or parameter list!")

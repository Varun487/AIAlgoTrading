import pandas as pd

from services.Utils.pusher import Pusher


class AddDBObject(object):
    def __init__(self, step=0, msg="", obj=None, obj_data=None):
        self.obj = obj
        self.obj_data = obj_data
        self.step = step
        self.msg = msg

        # Create an empty dataframe
        self.df = pd.DataFrame()

    def run(self):

        # Build dataframe to push
        for key in self.obj_data.keys():
            self.df[key] = self.obj_data[key]

        # Push objects to DB
        Pusher(df=self.df).push(self.obj)

        print(f"STEP {self.step}: {self.msg}")

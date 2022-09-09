


# import numpy as np
import pandas as pd
# import multiprocessing
# import psutil
# import io
# import boto3
# from os import path
# import joblib
# import tempfile
# import os
# import pickle
# import json
# from datetime import datetime
# from botocore.errorfactory import ClientError

class BaseClass(object):
    """
    This is a base class or utility class for general functions for
    various operations.


    """

    def __init__(
        self,
        msg=False,
        mode="Ntest"
    ):
        """
        Parameters
        ----------
        msg : bool
            Whether selected intermediate results and related comments will be
            displayed in the terminal or not (default: True).

        datetime_format : str, constant
            Date and time format. To reduce moving part of the program and this
             format has been kept fixed (default: "%m/%d/%Y %H:%M:%S").

        date_format : str, constant
            Only date format.
        """

        self.mode = mode
        self.msg = msg
        self.text_df=pd.read_csv('text_source_for_web.csv')



    def provide_options2_list(self):
        """
        Provides system memory status and version information of key packages.
        Version information of any installed package can be implemented.

        Parameters
        ----------
            None
        """
        options2 = [
                    "Undergraduate Student in Engineering",
                    "Undergraduate Student in Science",
                    "Undergraduate Student in Business/Commerce ",
                    "Undergraduate Student in Arts",
                    "Bachelor in Engineering",
                    "Bachelor in Science",
                    "Bachelor in Business/Commerce ",
                    "Bachelor in Arts",
                    "Master in Engineering",
                    "Master in Science",
                    "Master in Business/Commerce ",
                    "Master in Arts",
                    "PhD in Engineering",
                    "PhD in Science",
                    "PhD in Business/Commerce ",
                    "PhD in Arts",

                    ]
        return options2

    def generate_text_for_hightest_degree(self, skill_category):

        if skill_category == self.text_df['Main_Category'][0]:
            im_path='images/1_ug.jpg'
            return self.text_df.iloc[0], im_path
        elif skill_category == self.text_df['Main_Category'][1]:
            im_path='images/2_g.jpg'
            return self.text_df.iloc[1], im_path
        elif skill_category == self.text_df['Main_Category'][2]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[2], im_path
        elif skill_category == self.text_df['Main_Category'][3]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[3], im_path
        elif skill_category == self.text_df['Main_Category'][4]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[4], im_path
        elif skill_category == self.text_df['Main_Category'][5]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[5], im_path
        elif skill_category == self.text_df['Main_Category'][6]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[6], im_path
        elif skill_category == self.text_df['Main_Category'][7]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[7], im_path
        elif skill_category == self.text_df['Main_Category'][8]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[8], im_path
        elif skill_category == self.text_df['Main_Category'][9]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[9], im_path
        elif skill_category == self.text_df['Main_Category'][10]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[10], im_path
        elif skill_category == self.text_df['Main_Category'][11]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[11], im_path
        elif skill_category == self.text_df['Main_Category'][12]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[12], im_path
        elif skill_category == self.text_df['Main_Category'][13]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[13], im_path
        elif skill_category == self.text_df['Main_Category'][14]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[14], im_path
        elif skill_category == self.text_df['Main_Category'][15]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[15], im_path
        elif skill_category == self.text_df['Main_Category'][16]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[16], im_path
        elif skill_category == self.text_df['Main_Category'][17]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[17], im_path
        elif skill_category == self.text_df['Main_Category'][18]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[18], im_path
        elif skill_category == self.text_df['Main_Category'][19]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[19], im_path
        elif skill_category == self.text_df['Main_Category'][20]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[20], im_path
        elif skill_category == self.text_df['Main_Category'][21]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[21], im_path
        elif skill_category == self.text_df['Main_Category'][22]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[22], im_path
        elif skill_category == self.text_df['Main_Category'][23]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[23], im_path
        elif skill_category == self.text_df['Main_Category'][24]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[24], im_path

        elif skill_category == self.text_df['Main_Category'][25]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[25], im_path
        elif skill_category == self.text_df['Main_Category'][26]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[26], im_path
        elif skill_category == self.text_df['Main_Category'][27]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[27], im_path
        elif skill_category == self.text_df['Main_Category'][28]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[28], im_path
        elif skill_category == self.text_df['Main_Category'][29]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[29], im_path
        elif skill_category == self.text_df['Main_Category'][30]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[30], im_path
        elif skill_category == self.text_df['Main_Category'][31]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[31], im_path
        elif skill_category == self.text_df['Main_Category'][32]:
            im_path='images/ug_stud.jpg'
            return self.text_df.iloc[32], im_path
        # elif skill_category == self.text_df['Main_Category'][33]:
            #im_path='images/ug_stud.jpg'
        #     return self.text_df.iloc[33]

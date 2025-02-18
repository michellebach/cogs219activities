gen_trials 

import random
import os

def generate_trials(subj_code, seed):
    separator = ","

    # do cool stuff
    # open a file 
    trial_file = open(os.path.join(os.getcwd(), "trials", subj_code"_trials.csv), "w")

    #set seed
    random.seed(int(seed))

    # define key params
    angle_list = ["0", "50", "100", "150"]
    num_item = 40
    #create a list holding all trials 
    trial = []
    for i in range(num_items):
        item = str(1+1)
        for angle in angle_list:
            for match in match_list:
            if match == "same":
                image_name = item+image_name_sep+angle
                correct_response = "z"
            else: 
                imange_name = item+image_name)sep+angle + image_name_sep + "R"
                correct_response = "m"
            
            trials.append([subj_code, seed, ])
   
    # shuffle list


    # write the trials to the trial file 
    for cur_trial in trial:
        

    #close the trials file 


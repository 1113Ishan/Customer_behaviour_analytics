import os
from loader import load_shared_articles, load_users_interactions
from cleaning_functions import *

raw_path = "Dataset/Raw/"
cleaned_path = "Dataset/Cleaned/"

def main():

    # load data

    interactions = load_users_interactions(raw_path+"users_interactions.csv")
    articles = load_shared_articles(raw_path + "shared_articles.csv")

    interactions = fix_id(interactions)
    interactions = fix_time(interactions, "event_time")
    interactions = time_feature(interactions, "event_time")
    interactions = clean_event(interactions)
    interactions = filter_event(interactions)

    # create users table
    users = create_user_table(interactions)

    # clean articles

    articles = fix_id(articles)
    articles = fix_time(articles, "content_time")

    # keeping only useful columns

    articles = articles[[
        "content_id",
        "title",
        "contentType",
        "lang"
    ]]

    # save files

    os.makedirs(cleaned_path, exist_ok=True)

    interactions.to_csv(cleaned_path + "events_cleaned.csv", index=False)
    users.to_csv(cleaned_path+"users_cleaned.csv", index = False)
    articles.to_csv(cleaned_path + "content_cleaned.csv", index= False)

    print("Data cleaned and saved!!!")

if __name__ == "__main__":
    main()

    



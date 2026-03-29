import pandas as pd

#fix ID columns

def fix_id(df):
    id_cols = [
        "user_id",
        "content_id",
        "session_id"
    ]
    for col in id_cols:
        if col in df.columns:
             df[col] = df[col].apply(lambda x: format(x, '.0f') if pd.notnull(x) else x)
    
    return df

# convert timestamp to date_time

def fix_time(df, col):
    df[col] = pd.to_datetime(df[col], unit='s')
    return df


# extract date (year, month, and date)

def time_feature(df, col):
    df["date"] = df[col].dt.date
    df["year"] = df[col].dt.year
    df["month"] = df[col].dt.month

    return df

# clean event types

def clean_event(df):
    df["event_type"] = df["event_type"].str.upper().str.strip()
    return df

# filter event types (keep only required data)

def filter_event(df):
    valid_events = [
        "VIEW",
        "COMMENT CREATED",
        "LIKE",
        "BOOKMARK",
        "FOLLOW"
    ]
    return df[df["event_type"].isin(valid_events)]


# create a user table for signup date. The signup date is derieved from event_time, where 1st interaction is taken as the signup date

def create_user_table(df):
    users = df.groupby("user_id")["event_time"].min().reset_index()
    users = users.rename(columns = {
        "event_time": "signup_date"
    })
    return users





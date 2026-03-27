import pandas as pd

def load_users_interactions(path):
    df = pd.read_csv(path)
    df = df.rename(columns={
        "personId": "user_id",
        "contentId": "content_id",
        "eventType": "event_type",
        "timestamp": "event_time",
        "sessionId": "session_id"
    })
    return df

def load_shared_articles(path):
    df = pd.read_csv(path)
    df = df.rename(columns={
        "contentId": "content_id",
        "timestamp": "content_time",
        "eventType": "event_type"
    })
    return df


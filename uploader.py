import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def upload_to_youtube(video_file, title="Auto Video", description="Uploaded by Bot", channel_id=None):
    creds = Credentials(None,
                        refresh_token=os.getenv("REFRESH_TOKEN"),
                        client_id=os.getenv("CLIENT_ID"),
                        client_secret=os.getenv("CLIENT_SECRET"),
                        token_uri="https://oauth2.googleapis.com/token")

    youtube = build("youtube", "v3", credentials=creds)
    body = {
        "snippet": {
            "title": title,
            "description": description,
        },
        "status": {
            "privacyStatus": "public",
        }
    }
    if channel_id:
        body["snippet"]["channelId"] = channel_id

    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=video_file
    )
    response = request.execute()
    print("✅ Uploaded video ID:", response["id"])

from youtube_transcript_api import YouTubeTranscriptApi

ytt_api = YouTubeTranscriptApi()
fetched_transcript = ytt_api.fetch(video_id='0p4RCJ8P5ko', languages=['de'])

with open('A1-Level-German/text/A1-Level-German.txt', 'w') as f:
    for snippet in fetched_transcript:
        print(snippet.text)
        f.write("\n" + str(snippet.text))

 # indexable
last_snippet = fetched_transcript[-1]
print("\n" + str(last_snippet))

# provides a length
snippet_count = len(fetched_transcript)
print("Count: " + str(snippet_count))
        
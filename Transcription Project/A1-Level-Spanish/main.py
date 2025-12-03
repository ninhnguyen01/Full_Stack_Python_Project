from youtube_transcript_api import YouTubeTranscriptApi

ytt_api = YouTubeTranscriptApi()
fetched_transcript = ytt_api.fetch(video_id='bp9OZoQu3A0', languages=['es'])

with open('A1-Level-Spanish/text/A1-Level-Spanish.txt', 'w') as f:
    for snippet in fetched_transcript:
        print(snippet.text)
        f.write("\n" + str(snippet.text))

 # indexable
last_snippet = fetched_transcript[-1]
print("\n" + str(last_snippet))

# provides a length
snippet_count = len(fetched_transcript)
print("Count: " + str(snippet_count))
        
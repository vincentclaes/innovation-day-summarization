# transcript = open("./shiva-metadata-meeting.txt", "r").read()
transcript = open("./innovation-day-noon-meeting.txt", "r").read()


from transformers import pipeline

summarizer = pipeline(
                    "summarization", 
                    model="knkarthick/MEETING_SUMMARY", 
                    truncation=True
)
_summary = summarizer(transcript)
# cutoff unfinished sentence
# summary = _summary[0]["summary_text"].rsplit(".")[0] + "."
print("")
summary = _summary[0]["summary_text"]
print(summary)
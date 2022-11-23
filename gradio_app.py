import gradio as gr
from gradio.mix import Series

summarizer = gr.Interface.load("huggingface/knkarthick/MEETING_SUMMARY")

examples = [
    open("innovation-day-noon-meeting-david.txt").read(),
    open("innovation-day-noon-meeting-dimitri.txt").read(),
    open("innovation-day-noon-meeting-thiago.txt").read(),
    open("innovation-day-noon-meeting-tomas.txt").read()
]

Series(summarizer, 
        inputs = gr.inputs.Textbox(lines=10, label="Meeting Transcript"), 
        examples=examples).launch()

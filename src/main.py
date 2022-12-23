import os
import whisper
import gradio
from pyChatGPT import ChatGPT
from gtts import gTTS
from secret import SESSION_TOKEN

api = ChatGPT(SESSION_TOKEN)
model = whisper.load_model("base")


def transcribe(in_audio):
    f_audio = whisper.pad_or_trim(whisper.load_audio(in_audio))
    mel = whisper.log_mel_spectrogram(f_audio).to(model.device)

    options = whisper.DecodingOptions(fp16=False)
    _, probs = model.detect_language(mel)

    input_txt = whisper.decode(model, mel, options).text
    resp_text = api.send_message(input_txt)["message"]

    gTTS(resp_text).save(os.path.join(
        os.path.dirname(__file__), "resp_audio.mp3"))
    resp_path = os.path.join(os.path.dirname(__file__), "resp_audio.mp3")

    return [input_txt, resp_path, resp_text]


def gr_display():
    user_audio = gradio.inputs.Audio(
        source="microphone", type="filepath", label="Say Something...")

    user_text = gradio.Textbox(label="User Input")
    bella_audio = gradio.Audio(label="Bella (Audio)")
    bella_text = gradio.Textbox(label="Bella (Text)")

    gradio.Interface(
        title="Hi, I'm Bella, your AI Virtual Assistant.",
        fn=transcribe,
        allow_flagging="never",
        inputs=[user_audio],
        outputs=[user_text, bella_audio, bella_text], live=True).launch()


def main():
    gr_display()


if __name__ == "__main__":
    main()

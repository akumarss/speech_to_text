import argparse
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torchaudio
from summarizer import generate_summary

model_name = "openai/whisper-small"
processor = WhisperProcessor.from_pretrained(model_name)
model = WhisperForConditionalGeneration.from_pretrained(model_name).to("cuda")

def transcribe(audio_path):
    audio, sr = torchaudio.load(audio_path)
    audio = torchaudio.functional.resample(audio, sr, 16000)
    inputs = processor(audio.squeeze().numpy(), sampling_rate=16000, return_tensors="pt")
    pred_ids = model.generate(inputs.input_features.to("cuda"))
    text = processor.batch_decode(pred_ids, skip_special_tokens=True)[0]
    return text

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--audio", type=str, required=True)
    args = parser.parse_args()
    transcript = transcribe(args.audio)
    summary = generate_summary(transcript)
    print({"transcript": transcript, "summary": summary})

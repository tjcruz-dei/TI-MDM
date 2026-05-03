import sounddevice as sd
from scipy.io.wavfile import write
import whisper


SAMPLE_RATE = 16000
DURATION_SECONDS = 5
AUDIO_FILE = "recording.wav"


def record_audio(filename: str, duration: int, sample_rate: int):
    print(f"Recording for {duration} seconds...")
    
    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32"
    )
    
    sd.wait()
    write(filename, sample_rate, audio)
    
    print(f"Saved audio to {filename}")


def transcribe_audio(filename: str):
    print("Loading Whisper model...")
    model = whisper.load_model("base")

    print("Transcribing...")
    result = model.transcribe(filename,language="pt")

    return result["text"]


if __name__ == "__main__":
    record_audio(
        filename=AUDIO_FILE,
        duration=DURATION_SECONDS,
        sample_rate=SAMPLE_RATE
    )

    text = transcribe_audio(AUDIO_FILE)

    print("\nTranscription:")
    print(text)

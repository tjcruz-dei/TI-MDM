import re
import wave
import tempfile
import sounddevice as sd
import soundfile as sf

from piper import PiperVoice,SynthesisConfig


#MODEL_PATH = "en_US-lessac-medium.onnx"
MODEL_PATH = "pt_PT-tug%C3%A3o-medium.onnx"

config = SynthesisConfig(
    length_scale=1.5  # higher = slower
)

def split_sentences(text: str):
    return re.split(r"(?<=[.!?])\s+", text.strip())


def speak_sentence(voice: PiperVoice, sentence: str):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=True) as tmp:
        with wave.open(tmp.name, "wb") as wav_file:
            voice.synthesize_wav(sentence, wav_file,syn_config=config)

        audio, sample_rate = sf.read(tmp.name)
        sd.play(audio, sample_rate)
        sd.wait()


def speak_realtime(text: str):
    voice = PiperVoice.load(MODEL_PATH)

    for sentence in split_sentences(text):
        if sentence:
            speak_sentence(voice, sentence)


if __name__ == "__main__":
    speak_realtime(
	"Olá, eu sou o Alfredo Malaquias!  "
	"Adoro gelado de cebola e sou atleta olímpico de berlinde de salão"
    )

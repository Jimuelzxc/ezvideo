# Available Voices: af_alloy, af_aoede, af_bella, af_heart, af_jadzia, af_jessica, af_kore, af_nicole, af_nova, af_river, af_sarah, af_sky, af_v0, af_v0bella, af_v0irulan, af_v0nicole, af_v0sarah, af_v0sky, am_adam, am_echo, am_eric, am_fenrir, am_liam, am_michael, am_onyx, am_puck, am_santa, am_v0adam, am_v0gurney, am_v0michael, bf_alice, bf_emma, bf_lily, bf_v0emma, bf_v0isabella, bm_daniel, bm_fable, bm_george, bm_lewis, bm_v0george, bm_v0lewis, ef_dora, em_alex, em_santa, ff_siwis, hf_alpha, hf_beta, hm_omega, hm_psi, if_sara, im_nicola, jf_alpha, jf_gongitsune, jf_nezumi, jf_tebukuro, jm_kumo, pf_dora, pm_alex, pm_santa, zf_xiaobei, zf_xiaoni, zf_xiaoxiao, zf_xiaoyi, zm_yunjian, zm_yunxi, zm_yunxia, zm_yunyang"

import requests
import re
import librosa
import os

def generateAudio(text, title):
    print("CREATING AUDIO NOW")

    # Prepare the JSON payload for the POST request
    json_payload = {
        "model": "kokoro",
        "input": text,
        "voice": "am_adam",
        "response_format": "mp3"
    }

    try:
        # Make the POST request with streaming enabled
        response = requests.post(
            "https://api.kokorotts.com/v1/audio/speech",
            json=json_payload,
            stream=True
        )

        # Check if the request was successful
        if response.status_code == 200:
            # Sanitize the title and construct the audio file path
            title = re.sub(r'[^\w-]', '', title.lower().replace(" ", "_"))
            audio_path = f"./raw/audios/{title}.mp3"

            # Stream the response content to the file
            with open(audio_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:  # Filter out keep-alive chunks
                        f.write(chunk)
            print("Audio saved.")

            # Verify the file exists and is not empty, then calculate duration
            if os.path.exists(audio_path) and os.path.getsize(audio_path) > 0:
                duration = librosa.get_duration(path=audio_path)
                print("AUDIO CREATED")
                return {"path": audio_path, "duration": int(duration)}
            else:
                print("Generated audio file is empty or not found.")
                return None
        else:
            print(f"Request failed with status code {response.status_code}: {response.text}")
            return None

    except Exception as e:
        print(f"Error while generating audio: {e}")
        return None

        
        
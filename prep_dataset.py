import os
import pandas as pd
from pydub import AudioSegment

# --- Configuration Paths ---
ESC50_META = "ESC-50/meta/esc50.csv"
ESC50_AUDIO = "ESC-50/audio"

COUGHVID_META = "public_dataset/metadata_compiled.csv"
COUGHVID_AUDIO = "public_dataset"

OUTPUT_DIR = "edge_impulse_dataset"

# Create output folders which will act as our Edge Impulse classes
for label in ["cough", "sneeze", "noise"]:
    os.makedirs(os.path.join(OUTPUT_DIR, label), exist_ok=True)

def process_audio(input_path, output_path):
    """Converts any audio file to 16kHz, 16-bit PCM Mono WAV"""
    try:
        # pydub auto-detects the format (wav, webm, ogg)
        audio = AudioSegment.from_file(input_path)
        
        # 1. Force Mono (1 channel)
        audio = audio.set_channels(1)
        # 2. Force 16,000 Hz sample rate
        audio = audio.set_frame_rate(16000)
        # 3. Export as 16-bit WAV
        audio.export(output_path, format="wav", parameters=["-acodec", "pcm_s16le"])
        return True
    except Exception as e:
        print(f"Failed to process {input_path}: {e}")
        return False

# ==========================================
# 1. Process ESC-50 (Sneezes & Noise)
# ==========================================
print("Processing ESC-50 (Sneezes and Background Noise)...")
esc50_df = pd.read_csv(ESC50_META)

# We combine a few non-vocal categories to create a robust "noise" class
noise_categories = ['rain', 'keyboard_typing', 'mouse_click', 'breathing']

for index, row in esc50_df.iterrows():
    filename = row['filename']
    category = row['category']
    input_path = os.path.join(ESC50_AUDIO, filename)
    
    if category == 'sneezing':
        output_path = os.path.join(OUTPUT_DIR, "sneeze", filename)
        process_audio(input_path, output_path)
    
    elif category in noise_categories:
        output_path = os.path.join(OUTPUT_DIR, "noise", filename)
        process_audio(input_path, output_path)

# ==========================================
# 2. Process COUGHVID (Coughs) - DYNAMIC SEARCH
# ==========================================
print("\nProcessing COUGHVID (High-confidence Coughs)...")
coughvid_df = pd.read_csv(COUGHVID_META)

# Get a list of UUIDs for high-confidence coughs
clean_coughs = coughvid_df[coughvid_df['cough_detected'] >= 0.95]
valid_uuids = set(clean_coughs['uuid'].astype(str).tolist())
print(f"Found {len(valid_uuids)} high-confidence cough UUIDs in the CSV metadata.")

found_coughs = []

# Scan the entire public_dataset directory and all its subfolders
print("Scanning hard drive for matching audio files...")
for root, dirs, files in os.walk(COUGHVID_AUDIO):
    for file in files:
        # Get the filename without the extension (this is the UUID)
        file_uuid, ext = os.path.splitext(file)
        
        # If this file's UUID is in our high-confidence list, grab it!
        if file_uuid in valid_uuids:
            found_coughs.append(os.path.join(root, file))
            # Stop searching once we have 200 to balance the dataset
            if len(found_coughs) >= 200:
                break
    if len(found_coughs) >= 200:
        break

print(f"Found {len(found_coughs)} matching audio files on your hard drive.")

# Process the found files
if len(found_coughs) == 0:
    print("ERROR: Could not find ANY audio files matching the metadata.")
    print("Please check your 'public_dataset' folder. Did you download the full 2.3 GB audio dataset, or just the metadata CSV by accident?")
else:
    processed = 0
    for input_path in found_coughs:
        file_uuid, _ = os.path.splitext(os.path.basename(input_path))
        output_path = os.path.join(OUTPUT_DIR, "cough", f"{file_uuid}.wav")
        
        if process_audio(input_path, output_path):
            processed += 1
            print(f"Converting... {processed}/200", end="\r")

    print(f"\nSUCCESS: Converted {processed} cough files into the 'cough' folder!")
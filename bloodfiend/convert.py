import os
import subprocess

# Get the current folder where the script is located
folder_path = os.getcwd()

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.wav'):
        # Define the full file path
        wav_file = os.path.join(folder_path, filename)
        
        # Define the new file name with mp3 extension
        mp3_file = os.path.splitext(wav_file)[0] + '.mp3'
        
        # Run ffmpeg to convert the file
        command = [
            'ffmpeg', 
            '-i', wav_file,          # Input file
            '-ar', '44100',          # Set the sample rate to 44100 Hz
            mp3_file                 # Output file
        ]
        
        try:
            subprocess.run(command, check=True)
            os.remove(wav_file)
            print(f'Converted {filename} to mp3 with 44100 Hz sample rate')
        except subprocess.CalledProcessError as e:
            print(f'Error converting {filename}: {e}')

# Keep the script from closing immediately
input("Conversion complete. Press Enter to exit...")

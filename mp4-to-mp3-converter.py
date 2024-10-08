import os
from moviepy.editor import VideoFileClip

def is_valid_mp4(file_path):
    """Check if the file is a valid MP4 file."""
    return os.path.isfile(file_path) and file_path.lower().endswith('.mp4')

def extract_audio(input_file, output_file):
    """Extract audio from MP4 and save as MP3."""
    try:
        video = VideoFileClip(input_file)
        audio = video.audio
        audio.write_audiofile(output_file)
        audio.close()
        video.close()
        return True
    except Exception as e:
        print(f"Conversion error: {str(e)}")
        return False

def main():
    print("MP4 to MP3 Converter")
    
    while True:
        # Choose MP4 file
        input_file = input("Enter the path to the MP4 file (or 'q' to quit): ")
        
        if input_file.lower() == 'q':
            print("Thank you for using the MP4 to MP3 Converter. Goodbye!")
            break
        
        # Check if it's a valid MP4 file
        if not is_valid_mp4(input_file):
            print("Error: Invalid MP4 file. Please choose a valid MP4 file.")
            continue
        
        # Extract audio from MP4
        output_file = os.path.splitext(input_file)[0] + '.mp3'
        print("Extracting audio... This may take a while depending on the file size.")
        
        if extract_audio(input_file, output_file):
            print(f"Conversion successful! MP3 file saved as: {output_file}")
        else:
            print("Conversion failed. Please try again with a different file.")

if __name__ == "__main__":
    main()

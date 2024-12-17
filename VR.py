import cv2
import numpy as np
from moviepy.editor import ImageSequenceClip
from PIL import Image

# Function to create a zoom effect for a single photo
def create_zoom_effect(image, num_frames=30, zoom_factor=1.1):
    height, width, _ = image.shape
    frames = []
    
    for i in range(num_frames):
        # Calculate the scale for zooming
        scale = zoom_factor ** (i / num_frames)  # Increase the scale for zoom-in effect
        new_width = int(width * scale)
        new_height = int(height * scale)
        
        # Resize image to simulate zoom effect
        resized_image = cv2.resize(image, (new_width, new_height))
        
        # Crop the center of the resized image to keep original aspect ratio
        center_x, center_y = new_width // 2, new_height // 2
        cropped_image = resized_image[
            center_y - height // 2 : center_y + height // 2,
            center_x - width // 2 : center_x + width // 2
        ]
        
        frames.append(cropped_image)

    return frames

# Function to create a video from a list of frames
def create_video_from_frames(frames, output_filename="output_video.mp4", fps=24):
    # Create a video clip using moviepy from frames
    video_clip = ImageSequenceClip(frames, fps=fps)
    video_clip.write_videofile(output_filename, codec="libx264")

# Load the image
image_file = 'your_image.jpg'  # Change this to your image path
image = np.array(Image.open(image_file))  # Convert to NumPy array for OpenCV processing

# Create a zoom effect
print("Generating video...")
frames = create_zoom_effect(image, num_frames=60, zoom_factor=1.05)

# Create a video from the frames
create_video_from_frames(frames, output_filename="photo_to_video.mp4", fps=24)

print("Video created successfully!")

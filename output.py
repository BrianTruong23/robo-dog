import subprocess

package_name1 = "deepface"
package_name2 = "opencv-python"
package_name3 = "transformers"

try:
    # Try to import the package to see if it's already installed
    import deepface
    import transformers
    import cv2
    print(f"{package_name1} is already installed.")
    print(f"{package_name2} is already installed.")
except ImportError:
    # If the package is not installed, try to install it
    try:
        subprocess.check_call(["pip", "install", package_name1])
        subprocess.check_call(["pip", "install", package_name2])
        subprocess.check_call(["pip", "install", package_name3])
        print(f"{package_name1} has been successfully installed.")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package_name1}. Please install it manually.")




import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace

# Read the image
img = cv2.imread('random.jpeg')

# Call imshow() using plt object
plt.imshow(img[:, :, ::-1])

# Display the image
plt.show()

# Analyze the image for emotions
result = DeepFace.analyze(img, actions=['emotion'])

# Print the emotion analysis result
print(result)


print(result[0]['emotion'])

def get_the_emotion(dict_emotion):
  emotion, max_value = max(dict_emotion.items(), key=lambda item: item[1])
  return emotion

dict_emo = result[0]['emotion']
get_the_emotion(dict_emo)

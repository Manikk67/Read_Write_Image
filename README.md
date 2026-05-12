# Read_Write_Image

A simple Python project to **read and write images using OpenCV**.
This demonstrates basic image I/O operations — loading an image from disk and saving it back after processing.

---

## 📦 Requirements
- Python 3.x
- OpenCV library (`opencv-python`)

Install OpenCV:
```bash
pip install opencv-python
🚀 Usage
Example code:

python
import cv2

# Read an image
img = cv2.imread("input.jpg")

# Display the image (optional)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Write the image to a new file
cv2.imwrite("output.jpg", img)


📂 Project Structure
Code
Read_Write_Image/
│── main.py          # Python script to read/write image
│── README.md        # Project documentation
│── LICENSE          # License file
│── .gitignore       # Ignore unnecessary files
📝 License
This project is licensed under the MIT License – you are free to use, modify, and distribute it with attribution.

✨ Author
Created by Manikandan K

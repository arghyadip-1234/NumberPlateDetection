import cv2
import easyocr
import os
import re

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Haarcascade file path
harcascade = "model/haarcascade_russian_plate_number.xml"

# Dictionary to store car numbers and owner's names
car_data = {
    "HR26BP3543": "Aditya Das",
    "HR26CT4063": "Sima Paul",
    "DL3CAY9324": "Prithviraj Singh",
    "MH20EJ0364": "Sayam Dogra",
    "MH14EU3498": "Abhigyan Sengupta",
    # Add more car numbers and owner's names as needed
}

# Function to process image
def process_image(img_path):
    img = cv2.imread(img_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Initialize plate cascade classifier
    plate_cascade = cv2.CascadeClassifier(harcascade)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    min_area = 500
    result_text = ""
    count = 0

    for (x, y, w, h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            img_roi = img[y: y+h, x:x+w]

            # Perform OCR on the detected plate region
            result = reader.readtext(img_roi)

            if result:
                plate_text = result[0][1]
                # Remove special characters
                plate_text = re.sub(r'\W+', '', plate_text)
                owner_name = car_data.get(plate_text, "Unknown")
                cv2.putText(img, f"Owner: {owner_name}", (x, y-50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 255), 2)
                cv2.putText(img, f"Plate: {plate_text}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 255), 2)
                result_text += f"Plate {count + 1}: {plate_text} (Owner: {owner_name})\n"

            count += 1

    # Save processed image
    cv2.imwrite("static/result.jpg", img)

    return result_text

# Route for home page
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            if image.filename == "":
                return redirect(request.url)
            image.save(os.path.join("uploads", image.filename))
            img_path = os.path.join("uploads", image.filename)
            result_text = process_image(img_path)
            return render_template("result.html", result_text=result_text)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

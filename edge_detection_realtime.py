import cv2

# Start the webcam (0 is the default camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Read frame from webcam

    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Canny Edge Detection
    edges = cv2.Canny(gray, 50,150)

    # Display the result
    cv2.imshow('Edge Detection - Real Time', edges)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
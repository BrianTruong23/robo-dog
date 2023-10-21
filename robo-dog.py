
# import deepface

# # # Load an image in grayscale (0) or color (1)
# # img = cv2.imread('assets/logo.jpeg', 1)  # Use 0 for grayscale or 1 for color

# # # Resize the image to a specific width and height
# # resized_img = cv2.resize(img, (400, 400), fx = 0.5, fy = 0.5)


# # cv2.imshow('Image', resized_img)

# # # Wait for 5000 milliseconds (5 seconds)
# # cv2.waitKey(5000)

# # cv2.destroyAllWindows()

# # import cv2

# # cap = cv2.VideoCapture(0)  # Open the default camera (usually webcam)

# # while True:
# #     ret, frame = cap.read()

# #     cv2.imshow('frame', frame)

# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break

# # cap.release()
# # cv2.destroyAllWindows()
# import cv2
# import matplotlib.pyplot as plt
# from deepface import DeepFace

# # Read the image
# img = cv2.imread('assets/logo.jpeg')

# # Call imshow() using plt object
# plt.imshow(img[:, :, ::-1])

# # Display the image
# plt.show()

# # Analyze the image for emotions
# result = DeepFace.analyze(img, actions=['emotion'])

# # Print the emotion analysis result
# print(result['emotion'])


# import openai
# openai.api_key = "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"
# # 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
# # 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
# completion = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)



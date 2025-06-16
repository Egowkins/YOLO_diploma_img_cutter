import cv2
import os


def video_to_frames(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)

    frame_count = 0

    while True:

        ret, frame = cap.read()


        if not ret:
            break

        frame_name = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_name, frame)

        frame_count += 1

    cap.release()




video_path = "C:/Users/Егошка/Videos/T-90/For_dataset_t90_2.mkv"
output_folder = "T90_arma_3_frames_1"

video_to_frames(video_path, output_folder)




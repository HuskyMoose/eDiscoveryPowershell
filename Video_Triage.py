import cv2

video_file = input('Enter the video file: ')
video = cv2.VideoCapture(video_file)

nr_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
fps = video.get(cv2.CAP_PROP_FPS)
interval_choice = input("Do you want to seek by minutes or seconds? /nEnter 'm' for minutes or 's' for seconds: ")

    
def get_images ():
    timestamp = f"00:0{t}:0{s}"
    timestamp_list = timestamp.split(':')
    hh, mm, ss = timestamp_list 
    timestamp_list_floats = [float(i) for i in timestamp_list]
    hours, minutes, seconds = timestamp_list_floats
    global frame_nr
    frame_nr = hours * 3600 * fps + minutes * 60 * fps + seconds * fps
    video.set(1, frame_nr)
    success, frame = video.read()
    cv2.imwrite(f'{video_file}_{hh}h{mm}m{ss}s.jpg', frame)
    
frame_nr = 1
t = 0
s = 0

if interval_choice == 'm':
    timestamp_second_interval = 0
    timestamp_minute_interval = input(f"Please enter the interval in minutes (eg '01' or '20'): ")
    while t <= frame_nr:
        t= t + int(timestamp_minute_interval)
        get_images()
else: 
    timestamp_minute_interval = 0
    timestamp_second_interval = input(f"Please enter the interval in seconds (eg '01' or '59'): ")
    while t <= frame_nr:
        s= s + int(timestamp_second_interval)
        get_images()
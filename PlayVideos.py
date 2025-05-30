#A code for playing video files. Space key is used for pausing the video, a and d keys can be used to move backward/forward one frame. Press Esc to close video.
#frame numbers in the top left corner are presented as a sum of frames of both videos to make it easier to find them from the matlab file
#Each frame is turned to grayscale and jet colormap is added. 
import cv2

# Initialize pause state
pause = False
current_frame_index = 0

step_size = 1  # Number of frames to step forward/backward



#------------functions for pausing and moving through frames--------------------------
def toggle_pause():
    global pause
    pause = not pause

def step_forward(frames=1):
    global current_frame_index
    global total_frame_index
    if video == video_1:
        current_frame_index = min(current_frame_index + frames, total_frames - 1)
        video.set(cv2.CAP_PROP_POS_FRAMES, current_frame_index)
    elif video == video_2:
        current_frame_index = min(current_frame_index + frames, total_frames - 1)
        total_frame_index = min(total_frame_index + frames, total_frames - 1)
        video.set(cv2.CAP_PROP_POS_FRAMES, total_frame_index)

def step_backward(frames=1):
    global current_frame_index
    global total_frame_index
    global video_1_frames
    if video == video_1:
        current_frame_index = max(0, current_frame_index - frames)
        video.set(cv2.CAP_PROP_POS_FRAMES, current_frame_index)
    elif video == video_2:
        current_frame_index = max(0, current_frame_index - frames)
        total_frame_index = max(video_1_frames, total_frame_index - frames)
        video.set(cv2.CAP_PROP_POS_FRAMES, total_frame_index)
#-------------------------------------------------------
#---------function for displaying frame, adding colormap and sizing the frame to fit the window-------------------
def display_frame():
    global current_frame_index
    video.set(cv2.CAP_PROP_POS_FRAMES, current_frame_index)
    ret, frame = video.read()
    if not ret:
        return False

#make frame grayscale then add colormap
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    color_mapped_frame = cv2.applyColorMap(gray_frame, cv2.COLORMAP_JET)
    #color_mapped_frame = frame #to play videos in original color comment out the two lines above this

#size the frame to fit the window
    aspect_ratio = original_width / original_height
    if window_width / window_height > aspect_ratio:
        new_height = window_height
        new_width = int(aspect_ratio * window_height)
    else:
        new_width = window_width
        new_height = int(window_width / aspect_ratio)
    resized_frame = cv2.resize(color_mapped_frame, (new_width, new_height))

# Calculate the total and current time in the video
    if video == video_1:
        total_time = video_1_frames / fps
        total_minutes = int(total_time // 60)
        total_seconds = int(total_time % 60)
        total_milliseconds = int((total_time % 1) * 1000)

    elif video == video_2:
        total_time = video_2_frames / fps
        total_minutes = int(total_time // 60)
        total_seconds = int(total_time % 60)
        total_milliseconds = int((total_time % 1) * 1000)

    current_time = current_frame_index / fps
    minutes = int(current_time // 60)
    seconds = int(current_time % 60)
    milliseconds = int((current_time % 1) * 1000)
    time_text = f'Time: {minutes:02}:{seconds:02}.{milliseconds:03}/{total_minutes:02}:{total_seconds:02}.{total_milliseconds:03}'

# Font settings
    font = cv2.FONT_HERSHEY_PLAIN
    font_scale = 1  # Increase this value for larger font size
    font_color = (255, 255, 255)
    font_thickness = 1
    line_type = cv2.LINE_AA

#add timer and frame counter to the upper left corner
    if video == video_1:
        cv2.putText(resized_frame, f'Frame: {current_frame_index}/{total_frames}', (20, 20), font, font_scale, font_color, font_thickness, line_type)
    elif video == video_2:
        cv2.putText(resized_frame, f'Frame: {total_frame_index}/{total_frames}', (20, 20), font, font_scale, font_color, font_thickness, line_type)
    cv2.putText(resized_frame, time_text, (20, 40), font, font_scale, font_color, font_thickness, line_type)

#show the final processed frame   

    cv2.imshow('Video Frame with Colormap', resized_frame)
    return True

#---------------- Open video file-----------------------
#Input paths to all videos here
#exp2
# video_1 = cv2.VideoCapture(r'F:\MPIE OES data and codes\Magnetite data\Magnetite_Exp2_filter 440_5 g_900 mbar_continuous flow_10%H2_200 A_10 mm_6 min\Magnetite Exp2 440 nm filter_1.avi')
# video_2 = cv2.VideoCapture(r'F:\MPIE OES data and codes\Magnetite data\Magnetite_Exp2_filter 440_5 g_900 mbar_continuous flow_10%H2_200 A_10 mm_6 min\Magnetite Exp2 440 nm filter_2.avi')
#exp3
# video_1 = cv2.VideoCapture(r'E:\MPIE OES data and codes\Magnetite data\Magnetite_Exp3_filter 480_5 g_900 mbar_continuous flow_10%H2_200 A_10 mm_6 min\Magnetite Exp3 480 nm filter_1.avi')
# video_2 = cv2.VideoCapture(r'E:\MPIE OES data and codes\Magnetite data\Magnetite_Exp3_filter 480_5 g_900 mbar_continuous flow_10%H2_200 A_10 mm_6 min\Magnetite Exp3 480 nm filter_2.avi')
#exp4
video_1 = cv2.VideoCapture(r'F:\MPIE OES data and codes\Magnetite data\Magnetite_Exp4_filter 515_5 g_900 mbar_continuous flow_10%H2_200 A_10 mm_6 min\Magnetite Exp4 515 nm filter_1.avi')
video_2 = cv2.VideoCapture(r'F:\MPIE OES data and codes\Magnetite data\Magnetite_Exp4_filter 515_5 g_900 mbar_continuous flow_10%H2_200 A_10 mm_6 min\Magnetite Exp4 515 nm filter_2.avi')
#exp5
# video_1 = cv2.VideoCapture(r'E:\MPIE OES data and codes\Magnetite data\Magnetite_Exp5_filter 590_5 g_900 mbar_continuous flow_10%H2_200 A_10 mm_6 min\Magnetite Exp5 590 nm filter_1.avi')
# video_2 = cv2.VideoCapture(r'E:\MPIE OES data and codes\Magnetite data\Magnetite_Exp5_filter 590_5 g_900 mbar_continuous flow_10%H2_200 A_10 mm_6 min\Magnetite Exp5 590 nm filter_2.avi')

#change index depending on which video you wish to watch
video = video_2

# Check if video opened successfully
if not video.isOpened():
    print("Error: Could not open video.")
    exit()
 
# Get the total number of frames in the video
video_1_frames = int(video_1.get(cv2.CAP_PROP_FRAME_COUNT))
video_2_frames = int(video_2.get(cv2.CAP_PROP_FRAME_COUNT))
total_frames = video_1_frames + video_2_frames
total_frame_index = video_1_frames + current_frame_index

# Get the frames per second (FPS) of the video
fps = video.get(cv2.CAP_PROP_FPS)
#---------------------------------------------------

#---------- window size control---------------------
# Get the original width and height of the video
original_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
original_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Set initial window size
window_width = 800
window_height = 600

# Create a named window and make it resizable
cv2.namedWindow('Video Frame with Colormap', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Video Frame with Colormap', window_width, window_height)

# Move the window to position (20, 60) - adjust the coordinates as needed
cv2.moveWindow('Video Frame with Colormap', 20, 60)
#---------------------------------------------------------



#-------------key controls-------------------------------
while video.isOpened():
    if not pause:
        if not display_frame():
            break
        if video == video_1:
            current_frame_index += 1
        elif video == video_2:
            current_frame_index += 1
            total_frame_index += 1

    key = cv2.waitKey(11) & 0xFF
    if key == ord(' '):
        toggle_pause()
    elif key == 27:
        break
    elif key == ord('a'):
        step_backward(step_size)
        display_frame()
        pause = True
    elif key == ord('d'):
        step_forward(step_size)
        display_frame()
        pause = True

    while pause:
        key = cv2.waitKey(11) & 0xFF
        if key == ord(' '):
            toggle_pause()
            break
        elif key == 27:
            pause = False
            break
        elif key == ord('a'):
            step_backward(step_size)
            display_frame()
        elif key == ord('d'):
            step_forward(step_size)
            display_frame()
#------------------------------------------------------------------


#release video to save resources and to make it accessible in other applications
video.release()
cv2.destroyAllWindows()
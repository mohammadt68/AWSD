import cv2
import numpy as np



def get_awsd(frames, normalized=True):
    num_channels = frames[0].shape[2]
    channel_frames = _get_channel_frames(frames, num_channels)
    channel_wsd = [_compute_wsd(channel) for channel in channel_frames]

    awsd = cv2.merge(tuple(channel_wsd))
    if normalized:
        awsd = cv2.normalize(awsd, None, 0, 255, norm_type=cv2.NORM_MINMAX)
        awsd = awsd.astype('uint8')

    return awsd


def _get_channel_frames(iter_frames, num_channels):
    """ Takes a list of frames and returns a list of frame lists split by channel. """
    frames = [[] for channel in range(num_channels)]

    for frame in iter_frames:
        for channel_frames, channel in zip(frames, cv2.split(frame)):
            channel_frames.append(channel.reshape((*channel.shape[0:2], 1)))
    for i in range(len(frames)):
        frames[i] = np.array(frames[i])
    return frames


def _compute_wsd(frames):
    num_frames, h, w, depth = frames.shape

    # Compute the coefficients for the frames.
    coefficients = np.zeros(num_frames)
    for n in range(num_frames):
        cumulative_indices = np.array(range(n, num_frames)) + 1
        coefficients[n] = np.sum(((2*cumulative_indices) - num_frames) / cumulative_indices)

    # Multiply by the frames by the coefficients and sum the result.
    x1 = np.expand_dims(frames, axis=0)
    x2 = np.reshape(coefficients, (num_frames, 1, 1, 1))
    result = x1 * x2
    return np.sum(result[0], axis=0).squeeze()


def get_video_frames(video_path):
    # Initialize the frame number and create empty frame list
    video = cv2.VideoCapture(video_path)
    frame_list = []

    # Loop until there are no frames left.
    try:
        while True:
            more_frames, frame = video.read()

            if not more_frames:
                break
            else:
                frame_list.append(frame)

    finally:
        video.release()

    return frame_list

# noinspection DuplicatedCode
dataset_info = dict(
    dataset_name='breaststroke',
    keypoint_info={
        0: dict(name='right_ankle', id=0, color=[255, 128, 0], type='lower'),
        1: dict(name='right_knee', id=1, color=[255, 128, 0], type='lower'),
        2: dict(name='right_hip', id=2, color=[255, 128, 0], type='lower'),
        3: dict(name='right_shoulder', id=3, color=[255, 128, 0], type='upper'),
        4: dict(name='right_elbow', id=4, color=[255, 128, 0], type='upper'),
        5: dict(name='right_wrist', id=5, color=[255, 128, 0], type='upper'),
        6: dict(name='nose', id=6, color=[51, 153, 255], type='upper')
    },
    skeleton_info={
        0: dict(link=('right_ankle', 'right_knee'), id=0, color=[255, 128, 0]),
        1: dict(link=('right_shoulder', 'right_hip'), id=1, color=[51, 153, 255]),
        2: dict(link=('right_knee', 'right_hip'), id=2, color=[255, 128, 0]),
        3: dict(link=('right_shoulder', 'right_elbow'), id=3, color=[255, 128, 0]),
        4: dict(link=('right_elbow', 'right_wrist'), id=4, color=[255, 128, 0]),
        5: dict(link=('right_shoulder', 'nose'), id=5, color=[255, 128, 0])
    },
    joint_weights=[1.5, 1.2, 1., 1., 1.2, 1.5, 1],
    sigmas=[0.089, 0.087, 0.107, 0.079, 0.072, 0.062, 0.026]
)
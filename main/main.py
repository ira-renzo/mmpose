from mmpose.apis import MMPoseInferencer

if __name__ == '__main__':
    img_path = 'images/frame_000000.PNG'  # replace this with your own image path

    # create the inferencer using the model alias
    inferencer = MMPoseInferencer('vitpose-h')

    # The MMPoseInferencer API employs a lazy inference approach,
    # creating a prediction generator when given input
    result_generator = inferencer(img_path, show=True)
    result = next(result_generator)

    # for file in os.listdir("images"):
    #     print(file)
    #     # test a single image
    #     pose_results, _ = inference_bottom_up_pose_model(pose_model, 'images/' + file)
    #     # show the results
    #     res = vis_pose_result(pose_model, 'images/' + file, pose_results, out_file='images_output/' + file)
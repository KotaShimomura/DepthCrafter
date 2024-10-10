import os
import cv2
import os
import glob

def create_videos_from_images(image_folder, output_folder, fps):
    # 画像ファイルのリストを取得し、ソート
    images = [img for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))]
    images.sort()  # 名前順にソート
    os.makedirs(output_folder, exist_ok=True)

    # 画像のサイズ取得
    sample_image = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, _ = sample_image.shape
    size = (width, height)

    # 30枚ごとに動画を作成
    for i in range(0, len(images), 30):
        video_name = os.path.join(output_folder, f'video_{i//30 + 1}.mp4')
        video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
        
        for j in range(i, min(i + 30, len(images))):
            img_path = os.path.join(image_folder, images[j])
            frame = cv2.imread(img_path)
            video.write(frame)

        video.release()
        print(f'{video_name} saved successfully!')



if __name__ == "__main__":

    class CFG:
        img_sizeh=512
        img_sizew = 1024


    for split in ["train", "val", "test"]:
        leftImg8bit_sequence_dir = f"/workspace/data2/UniRisk/cityscapes/leftImg8bit_sequence/{split}/"

        city_dirs = sorted(glob.glob(os.path.join(leftImg8bit_sequence_dir, '*')))

        for i in city_dirs:
            image_dir = i
            output_dir = f"/workspace/data2/UniRisk/cityscapes_video/{split}/"+i.split("/")[-1]+"/"
            create_videos_from_images(image_dir, output_dir, 17)
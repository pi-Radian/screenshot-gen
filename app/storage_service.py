import os
import cloudinary

cloudinary.config(
    cloud_name=str(os.getenv("CLOUDINARY_CLOUD_NAME")),
    api_key=str(os.getenv("CLOUDINARY_API_KEY")),
    api_secret=str(os.getenv("CLOUDINARY_API_SECRET")),
    # api_proxy = "http://proxy.server:9999"
)

import cloudinary.uploader
import cloudinary.api


# cloudinary.uploader.upload("dog.mp4",
#   folder = "myfolder/mysubfolder/",
#   public_id = "my_dog",
#   overwrite = true,
#   notification_url = "https://mysite.example.com/notify_endpoint",
#   resource_type = "video")


def save_img_to_bucket(random_path):
    # file_name = random_path.split('/')[-1]
    res = cloudinary.uploader.upload(
        random_path,
        folder="scgen",
        public_id=random_path.split("/")[-1].split(".")[0],
        resource_type="image",
    )
    return res["secure_url"]

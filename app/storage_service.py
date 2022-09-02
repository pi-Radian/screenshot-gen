import cloudinary

cloudinary.config(
cloud_name = "xxxx",
api_key = "xxxxxxxxxxxx",
api_secret = "xxxxxxxxxxx",
api_proxy = "http://proxy.server:9999"
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
    print(random_path)
    return 'cloudinary_uri'

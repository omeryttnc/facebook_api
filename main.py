from src.api import refresh_tokens,create_facebook_post
from src.utils import get_random_comment
from src.config import  PAGE_ACCESS_TOKEN, USER_ACCESS_TOKEN, POST_ID, PAGE_ID, VERSION,OPENAI_API_KEY
from src.api import create_facebook_post, get_facebook_posts, get_group_Ids, comment_on_post, create_facebook_post, create_facebook_photo_post, create_facebook_video_post, delete_facebook_post
from src.ai import generate_ai_content, generate_ai_image
if __name__ == "__main__":
    
    content = generate_ai_content("Yapay zeka ve gelecek")
    contentForImage = generate_ai_content("A beautiful sunset over the mountains")

    url=generate_ai_image("A beautiful sunset over the mountains")

    create_facebook_post(content)
 
    create_facebook_photo_post(url, contentForImage)



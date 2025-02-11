from src.api import refresh_tokens,create_facebook_post
from src.utils import get_random_comment
from src.config import  PAGE_ACCESS_TOKEN, USER_ACCESS_TOKEN, POST_ID, PAGE_ID, VERSION


if __name__ == "__main__":
    # refresh_tokens()
    create_facebook_post(get_random_comment())
    # refresh_access_token()
    # posts = get_facebook_posts()
    # posts = get_group_Ids()
    # posts = comment_on_post(POST_ID, get_random_comment())
    # posts = create_facebook_post( get_random_comment())
    # posts = create_facebook_photo_post("https://picsum.photos/500", get_random_comment())
    # posts = create_facebook_video_post("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExejlyM2MxazdpeG42OXA3dHAyanNndDNjbTJsaHpiemJ0NzA2NmFpZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2IudUHdI075HL02Pkk/giphy.gif", get_random_comment())
    # posts = delete_facebook_post("558661603998461_122101579652762991")
    
    # if posts:
    #     post_id = posts[0]["id"]  # İlk posta yorum yapalım
    #    # comment_on_post(post_id, get_random_comment())
    # else:
    #     print("Yorum yapılacak post bulunamadı!")

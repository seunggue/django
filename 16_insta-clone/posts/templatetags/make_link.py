from django import template
import re
register = template.Library()

@register.filter
def hashtag_link(post):
    content = post.content # #고양이 #개 #강아지
    hashtags = post.hashtags.all() # QuerySet [HashTag object (1:고양이), HashTag object (2:강아지)]
    
    for hashtag in hashtags:
        # content = content.replace(
        #     f'{hashtag.content}',
        #     f'<a href="/posts/hashtags/{hashtag.id}/">{hashtag.content}</a>'
        # )
        content = re.sub(
            fr'{hashtag.content}\b', 
            f'<a href="/posts/hashtags/{hashtag.id}/">{hashtag.content}</a>',
            content
        )
    return content
from instapy import InstaPy
from instapy.util import smart_run

# Write your automation here
# Stuck? Look at the github page https://github.com/InstaPy/instapy-quickstart

insta_username = "Email Here"
insta_password = "Password Here"

dont_like = ["food", "girl", "hot"]
ignore_words = ["pizza"]
friend_list = ["midhunvnadh"]

# If you want to enter your Instagram Credentials directly just enter
# username=<your-username-here> and password=<your-password> into InstaPy
# e.g like so InstaPy(username="instagram", password="test1234")

bot = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
with smart_run(bot):
    bot.set_relationship_bounds(
        enabled=True,
        potency_ratio=-1.21,
        delimit_by_numbers=True,
        max_followers=4590,
        max_following=5555,
        min_followers=45,
        min_following=77,
    )
    bot.set_do_comment(True, percentage=70)
    bot.set_do_follow(True, percentage=60)
    bot.set_comments(["Cool! Can you checkout my accout?", "Awesome! Can you checkout my account?", "Nice! Can you checkout my profile?"])
    bot.set_dont_include(friend_list)
    bot.set_dont_like(dont_like)
    bot.set_ignore_if_contains(ignore_words)
    bot.like_by_tags(["oneui", "#tech", "#technology", "#raspberrypi", "#google", "#youtube"], amount=100)
    bot.end()

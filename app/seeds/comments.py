from app.models import db, Comment

def seed_comments():
    comments = [
        Comment(
            user_id=12,
            post_id=80,
            comment="You are so cute!",
        ),
        Comment(
            user_id=11,
            post_id=79,
            comment="OMG adorable!",
        ),
        Comment(
            user_id=10,
            post_id=78,
            comment="This is amazing!",
        ),
        Comment(
            user_id=9,
            post_id=77,
            comment="Can i adopt you!",
        ),
        Comment(
            user_id=8,
            post_id=76,
            comment="<3",
        ),
        Comment(
            user_id=7,
            post_id=75,
            comment="You look so good here!",
        ),
        Comment(
            user_id=6,
            post_id=74,
            comment="mhm slayyyy",
        ),
        Comment(
            user_id=5,
            post_id=73,
            comment="caption game on point",
        ),
        Comment(
            user_id=4,
            post_id=72,
            comment="Adorbs"
        ),
        Comment(
            user_id=3,
            post_id=71,
            comment="ily <3"
        ),
        Comment(
            user_id=2,
            post_id=70,
            comment="You look so good here!"
        ),
        Comment(
            user_id=1,
            post_id=69,
            comment="Let me adopt you pls <3"
        ),
        Comment(
            user_id=12,
            post_id=68,
            comment="So cute"
        ),
        Comment(
            user_id=11,
            post_id=67,
            comment="Soooo cute"
        ),
        Comment(
            user_id=10,
            post_id=66,
            comment="Yes i love it!"
        ),
        Comment(
            user_id=9,
            post_id=65,
            comment="You are so cute!",
        ),
        Comment(
            user_id=8,
            post_id=64,
            comment="OMG adorable!",
        ),
        Comment(
            user_id=7,
            post_id=63,
            comment="This is amazing!",
        ),
        Comment(
            user_id=6,
            post_id=62,
            comment="Can i adopt you!",
        ),
        Comment(
            user_id=5,
            post_id=61,
            comment="<3",
        ),
        Comment(
            user_id=4,
            post_id=60,
            comment="You look so good here!",
        ),
        Comment(
            user_id=3,
            post_id=59,
            comment="mhm slayyyy",
        ),
        Comment(
            user_id=2,
            post_id=58,
            comment="caption game on point",
        ),
        Comment(
            user_id=1,
            post_id=57,
            comment="Adorbs"
        ),
        Comment(
            user_id=12,
            post_id=56,
            comment="ily <3"
        ),
        Comment(
            user_id=11,
            post_id=55,
            comment="You look so good here!"
        ),
        Comment(
            user_id=10,
            post_id=54,
            comment="Let me adopt you pls <3"
        ),
        Comment(
            user_id=9,
            post_id=53,
            comment="So cute"
        ),
        Comment(
            user_id=8,
            post_id=52,
            comment="Soooo cute"
        ),
        Comment(
            user_id=7,
            post_id=51,
            comment="Yes i love it!"
        ),
        Comment(
            user_id=6,
            post_id=50,
            comment="You are so cute!",
        ),
        Comment(
            user_id=5,
            post_id=49,
            comment="OMG adorable!",
        ),
        Comment(
            user_id=4,
            post_id=48,
            comment="This is amazing!",
        ),
        Comment(
            user_id=3,
            post_id=47,
            comment="Can i adopt you!",
        ),
        Comment(
            user_id=2,
            post_id=46,
            comment="<3",
        ),
        Comment(
            user_id=1,
            post_id=45,
            comment="You look so good here!",
        ),
        Comment(
            user_id=12,
            post_id=44,
            comment="mhm slayyyy",
        ),
        Comment(
            user_id=11,
            post_id=43,
            comment="caption game on point",
        ),
        Comment(
            user_id=10,
            post_id=42,
            comment="Adorbs"
        ),
        Comment(
            user_id=9,
            post_id=41,
            comment="ily <3"
        ),
        Comment(
            user_id=8,
            post_id=40,
            comment="You look so good here!"
        ),
        Comment(
            user_id=7,
            post_id=39,
            comment="Let me adopt you pls <3"
        ),
        Comment(
            user_id=6,
            post_id=38,
            comment="So cute"
        ),
        Comment(
            user_id=5,
            post_id=37,
            comment="Soooo cute"
        ),
        Comment(
            user_id=4,
            post_id=36,
            comment="Yes i love it!"
        ),
        Comment(
            user_id=3,
            post_id=35,
            comment="You are so cute!",
        ),
        Comment(
            user_id=2,
            post_id=34,
            comment="OMG adorable!",
        ),
        Comment(
            user_id=1,
            post_id=33,
            comment="This is amazing!",
        ),
        Comment(
            user_id=12,
            post_id=32,
            comment="Can i adopt you!",
        ),
        Comment(
            user_id=11,
            post_id=31,
            comment="<3",
        ),
        Comment(
            user_id=10,
            post_id=30,
            comment="You look so good here!",
        ),
        Comment(
            user_id=9,
            post_id=29,
            comment="mhm slayyyy",
        ),
        Comment(
            user_id=8,
            post_id=28,
            comment="caption game on point",
        ),
        Comment(
            user_id=7,
            post_id=27,
            comment="Adorbs"
        ),
        Comment(
            user_id=6,
            post_id=26,
            comment="ily <3"
        ),
        Comment(
            user_id=5,
            post_id=25,
            comment="You look so good here!"
        ),
        Comment(
            user_id=4,
            post_id=24,
            comment="Let me adopt you pls <3"
        ),
        Comment(
            user_id=3,
            post_id=23,
            comment="So cute"
        ),
        Comment(
            user_id=2,
            post_id=22,
            comment="Soooo cute"
        ),
        Comment(
            user_id=1,
            post_id=21,
            comment="Yes i love it!"
        ),
        Comment(
            user_id=12,
            post_id=20,
            comment="You are so cute!",
        ),
        Comment(
            user_id=11,
            post_id=19,
            comment="OMG adorable!",
        ),
        Comment(
            user_id=10,
            post_id=18,
            comment="This is amazing!",
        ),
        Comment(
            user_id=9,
            post_id=17,
            comment="Can i adopt you!",
        ),
        Comment(
            user_id=8,
            post_id=16,
            comment="<3",
        ),
        Comment(
            user_id=7,
            post_id=15,
            comment="You look so good here!",
        ),
        Comment(
            user_id=6,
            post_id=14,
            comment="mhm slayyyy",
        ),
        Comment(
            user_id=5,
            post_id=13,
            comment="caption game on point",
        ),
        Comment(
            user_id=4,
            post_id=12,
            comment="Adorbs"
        ),
        Comment(
            user_id=3,
            post_id=11,
            comment="ily <3"
        ),
        Comment(
            user_id=2,
            post_id=10,
            comment="You look so good here!"
        ),
        Comment(
            user_id=1,
            post_id=9,
            comment="Let me adopt you pls <3"
        ),
        Comment(
            user_id=12,
            post_id=7,
            comment="So cute"
        ),
        Comment(
            user_id=11,
            post_id=6,
            comment="Soooo cute"
        ),
        Comment(
            user_id=10,
            post_id=5,
            comment="Yes i love it!"
        ),
        Comment(
            user_id=9,
            post_id=4,
            comment="You are so cute!",
        ),
        Comment(
            user_id=8,
            post_id=3,
            comment="OMG adorable!",
        ),
        Comment(
            user_id=7,
            post_id=2,
            comment="This is amazing!",
        ),
        Comment(
            user_id=6,
            post_id=1,
            comment="Can i adopt you!",
        ),
        Comment(
            user_id=5,
            post_id=80,
            comment="<3",
        ),
        Comment(
            user_id=4,
            post_id=79,
            comment="You look so good here!",
        ),
        Comment(
            user_id=3,
            post_id=78,
            comment="mhm slayyyy",
        ),
        Comment(
            user_id=2,
            post_id=58,
            comment="caption game on point",
        ),
        Comment(
            user_id=1,
            post_id=57,
            comment="Adorbs"
        ),
        Comment(
            user_id=12,
            post_id=56,
            comment="ily <3"
        ),
        Comment(
            user_id=11,
            post_id=55,
            comment="You look so good here!"
        ),
        Comment(
            user_id=10,
            post_id=54,
            comment="Let me adopt you pls <3"
        ),
        Comment(
            user_id=9,
            post_id=53,
            comment="So cute"
        ),
        Comment(
            user_id=8,
            post_id=52,
            comment="Soooo cute"
        ),
        Comment(
            user_id=7,
            post_id=51,
            comment="Yes i love it!"
        ),
        Comment(
            user_id=6,
            post_id=50,
            comment="You are so cute!",
        ),
        Comment(
            user_id=5,
            post_id=49,
            comment="OMG adorable!",
        ),
        Comment(
            user_id=4,
            post_id=48,
            comment="This is amazing!",
        ),
        Comment(
            user_id=3,
            post_id=47,
            comment="Can i adopt you!",
        ),
        Comment(
            user_id=2,
            post_id=46,
            comment="<3",
        ),
        Comment(
            user_id=1,
            post_id=45,
            comment="You look so good here!",
        ),
        Comment(
            user_id=12,
            post_id=44,
            comment="mhm slayyyy",
        ),
        Comment(
            user_id=11,
            post_id=43,
            comment="caption game on point",
        ),
        Comment(
            user_id=10,
            post_id=42,
            comment="Adorbs"
        ),
        Comment(
            user_id=9,
            post_id=41,
            comment="ily <3"
        ),
        Comment(
            user_id=8,
            post_id=40,
            comment="You look so good here!"
        ),
        Comment(
            user_id=7,
            post_id=39,
            comment="Let me adopt you pls <3"
        ),
        Comment(
            user_id=6,
            post_id=38,
            comment="So cute"
        ),
        Comment(
            user_id=5,
            post_id=37,
            comment="Soooo cute"
        ),
        Comment(
            user_id=4,
            post_id=36,
            comment="Yes i love it!"
        ),
        Comment(
            user_id=3,
            post_id=35,
            comment="You are so cute!",
        ),
        Comment(
            user_id=2,
            post_id=34,
            comment="OMG adorable!",
        ),
        Comment(
            user_id=1,
            post_id=33,
            comment="This is amazing!",
        ),
        Comment(
            user_id=12,
            post_id=32,
            comment="Can i adopt you!",
        ),
        Comment(
            user_id=11,
            post_id=31,
            comment="<3",
        ),
        Comment(
            user_id=10,
            post_id=30,
            comment="You look so good here!",
        ),
        Comment(
            user_id=9,
            post_id=29,
            comment="mhm slayyyy",
        ),
        Comment(
            user_id=8,
            post_id=28,
            comment="caption game on point",
        ),
        Comment(
            user_id=7,
            post_id=27,
            comment="Adorbs"
        ),
        Comment(
            user_id=6,
            post_id=26,
            comment="ily <3"
        ),
        Comment(
            user_id=5,
            post_id=25,
            comment="You look so good here!"
        ),
        Comment(
            user_id=4,
            post_id=24,
            comment="Let me adopt you pls <3"
        ),
        Comment(
            user_id=3,
            post_id=23,
            comment="So cute"
        ),
        Comment(
            user_id=2,
            post_id=22,
            comment="Soooo cute"
        ),
        Comment(
            user_id=1,
            post_id=21,
            comment="Yes i love it!"
        ),

    ]

    for comment in comments:
        db.session.add(comment)
        
    db.session.commit()

def undo_comments():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()

define s = Character(_("Sylvie"), color="#c8ffc8")
define m = Character(_("Me"), color="#c8c8ff")
default book = False

label start:

    play music "audio/illurock.wav"

    scene bg lecturehall
    with fade

    show me blue normal

    "It's only when I hear the sounds of shuffling feet and supplies being put away that I realize that the lecture's over."

    "Professor Eileen's lectures are usually interesting, but today I just couldn't concentrate on it."

    "I've had a lot of other thoughts on my mind...thoughts that culminate in a question."

    "It's a question that I've been meaning to ask a certain someone."

    stop music

    scene bg uni
    with fade

    play music "audio/crowd.mp3"

    show me blue smile at left

    "When we come out of the university, I spot her right away."

    show sylvie green normal at right
    with dissolve

    "I've known Sylvie since we were kids. She's got a big heart and she's always been a good friend to me."

    "But recently... I've felt that I want something more."

    "More than just talking, more than just walking home together when our classes end."

    menu:

        "As soon as she catches my eye, I decide..."

        "To ask her right away.":

            jump rightaway

        "To ask her later.":

            jump later


label rightaway:

    show sylvie green smile at right

    show me blue smile at left

    s "Hi there! How was class?"

    m "Good..."

    hide sylvie

    "I can't bring myself to admit that it all went in one ear and out the other."

    m "Are you going home now? Wanna walk back with me?"

    show sylvie green smile at right

    s "Sure!"

    scene bg meadow
    with fade

    stop music

    play music "audio/birds.mp3"

    "After a short while, we reach the meadows just outside the neighborhood where we both live."

    "It's a scenic view I've grown used to. Autumn is especially beautiful here."

    "When we were children, we played in these meadows a lot, so they're full of memories."

    show me blue normal at left

    m "Hey... Umm..."

    show sylvie green smile at right
    with dissolve

    "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."

    "I'll ask her...!"

    m "Ummm... Will you..."

    m "Will you be my artist for a visual novel?"

    show sylvie green surprised at right

    "Silence."

    "She looks so shocked that I begin to fear the worst. But then..."

    show sylvie green smile at right

    menu:

        s "Sure, but what's a \"visual novel?\""

        "It's a videogame.":
            jump game

        "It's an interactive book.":
            jump book


label game:

    show me blue smile at left

    m "It's a kind of videogame you can play on your computer or a console."

    m "Visual novels tell a story with pictures and music."

    m "Sometimes, you also get to make choices that affect the outcome of the story."

    s "So it's like those choose-your-adventure books?"

    m "Exactly! I've got lots of different ideas that I think would work."

    m "And I thought maybe you could help me...since I know how you like to draw."

    m "It'd be hard for me to make a visual novel alone."

    s "Well, sure! I can try. I just hope I don't disappoint you."

    m "You know you could never disappoint me, Sylvie."

    jump marry


label book:

    $ book = True

    show me blue smile at left

    m "It's like an interactive book that you can read on a computer or a console."

    show sylvie green surprised at right

    s "Interactive?"

    m "You can make choices that lead to different events and endings in the story."

    s "So where does the \"visual\" part come in?"

    m "Visual novels have pictures and even music, sound effects, and sometimes voice acting to go along with the text."

    show sylvie green smile at right

    s "I see! That certainly sounds like fun. I actually used to make webcomics way back when, so I've got lots of story ideas."

    m "That's great! So...would you be interested in working with me as an artist?"

    s "I'd love to!"

    jump marry

label marry:

    scene black
    with dissolve

    "And so, we become a visual novel creating duo."

    scene bg club
    with dissolve

    show me blue smile

    "Over the years, we make lots of games and have a lot of fun making them."

    if book:

        "Our first game is based on one of Sylvie's ideas, but afterwards I get to come up with stories of my own, too."

    "We take turns coming up with stories and characters and support each other to make some great games!"

    hide me

    "{b}Good Ending{/b}."

    return

label later:

    scene black
    with dissolve

    hide sylvie

    show me blue sad

    "I can't get up the nerve to ask right now. With a gulp, I decide to ask her later."

    "But I'm an indecisive person."

    "I couldn't ask her that day and I end up never being able to ask her."

    "I guess I'll never know the answer to my question now..."

    hide me

    "{b}Bad Ending{/b}."

    return

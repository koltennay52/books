from flask import Flask, render_template

content = {

    "Fantasy": {

        "name": "Fantasy",
        "description": "Fantasy is a genre that uses magic and other supernatural forms as a primary element of plot, theme, and/or setting. Fantasy is generally distinguished from science fiction and horror by the expectation that it steers clear of technological and macabre themes, respectively, though there is a great deal of overlap between the three (collectively known as speculative fiction or science fiction/fantasy) In its broadest sense, fantasy comprises works by many writers, artists, filmmakers, and musicians, from ancient myths and legends to many recent works embraced by a wide audience today, including young adults, most of whom are represented by the works below",

        "books": [
            {
                "title": "A Deadly Education",
                "author": "Naomi Novik",
                "description": "A Deadly Education is set at Scholomance, a school for the magically gifted where failure means certain death (for real) — until one girl, El, begins to unlock its many secrets. There are no teachers, no holidays, and no friendships, save strategic ones. Survival is more important than any letter grade, for the school won’t allow its students to leave until they graduate… or die! The rules are deceptively simple: Don’t walk the halls alone. And beware of the monsters who lurk everywhere. El is uniquely prepared for the school’s dangers. She may be without allies, but she possesses a dark power strong enough to level mountains and wipe out millions. It would be easy enough for El to defeat the monsters that prowl the school. The problem? Her powerful dark magic might also kill all the other students."
            },
            {
                "title": "Piranesi",
                "author": "Susanna Clarke",
                "description": "Piranesi's house is no ordinary building: its rooms are infinite, its corridors endless, its walls are lined with thousands upon thousands of statues, each one different from all the others. Within the labyrinth of halls an ocean is imprisoned; waves thunder up staircases, rooms are flooded in an instant. But Piranesi is not afraid; he understands the tides as he understands the pattern of the labyrinth itself. He lives to explore the house. There is one other person in the house—a man called The Other, who visits Piranesi twice a week and asks for help with research into A Great and Secret Knowledge. But as Piranesi explores, evidence emerges of another person, and a terrible truth begins to unravel, revealing a world beyond the one Piranesi has always known. For readers of Neil Gaiman's The Ocean at the End of the Lane and fans of Madeline Miller's Circe, Piranesi introduces an astonishing new world, an infinite labyrinth, full of startling images and surreal beauty, haunted by the tides and the clouds."
            },
            {
                "title": "To Sleep in a Sea of Stars",
                "author": "Christopher Paolini",
                "description": "During a routine survey mission on an uncolonized planet, Kira finds an alien relic. At first she's delighted, but elation turns to terror when the ancient dust around her begins to move.As war erupts among the stars, Kira is launched into a galaxy-spanning odyssey of discovery and transformation. First contact isn't at all what she imagined, and events push her to the very limits of what it means to be human.While Kira faces her own horrors, Earth and its colonies stand upon the brink of annihilation. Now, Kira might be humanity's greatest and final hope"
            }
            ]       
        
    }, 
    "Science Fiction": {

        "name": "Science Fiction",
        "description": "Science fiction (abbreviated SF or sci-fi with varying punctuation and capitalization) is a broad genre of fiction that often involves speculations based on current or future science or technology. Science fiction is found in books, art, television, films, games, theatre, and other media. In organizational or marketing contexts, science fiction can be synonymous with the broader definition of speculative fiction, encompassing creative works incorporating imaginative elements not found in contemporary reality; this includes fantasy, horror and related genres.Although the two genres are often conflated as science fiction/fantasy, science fiction differs from fantasy in that, within the context of the story, its imaginary elements are largely possible within scientifically established or scientifically postulated laws of nature (though some elements in a story might still be pure imaginative speculation). Exploring the consequences of such differences is the traditional purpose of science fiction, making it a 'literature of ideas'. Science fantasy is largely based on writing entertainingly and rationally about alternate possibilities in settings that are contrary to known reality. ",

        "books": [
            {
                "title": "Skyhunter",
                "author": "Marie Lu",
                "description": "The Karensa Federation has conquered a dozen countries, leaving Mara as one of the last free nations in the world. Refugees flee to its borders to escape a fate worse than death—transformation into mutant war beasts known as Ghosts, creatures the Federation then sends to attack Mara. The legendary Strikers, Mara's elite fighting force, are trained to stop them. But as the number of Ghosts grows and Karensa closes in, defeat seems inevitable. Still, one Striker refuses to give up hope. Robbed of her voice and home, Talin Kanami knows firsthand the brutality of the Federation. Their cruelty forced her and her mother to seek asylum in a country that considers their people repugnant. She finds comfort only with a handful of fellow Strikers who have pledged their lives to one another and who are determined to push Karensa back at all costs. When a mysterious prisoner is brought from the front, Talin senses there’s more to him than meets the eye. Is he a spy from the Federation? Or could he be the weapon that will save them all?"
            },
            {
                "title": "Hench",
                "author": "Natalie Zina Walschots",
                "description": "Anna does boring things for terrible people because even criminals need office help and she needs a job. Working for a monster lurking beneath the surface of the world isn’t glamorous. But is it really worse than working for an oil conglomerate or an insurance company? In this economy? As a temp, she’s just a cog in the machine. But when she finally gets a promising assignment, everything goes very wrong, and an encounter with the so-called “hero” leaves her badly injured.  And, to her horror, compared to the other bodies strewn about, she’s the lucky one. So, of course, then she gets laid off. With no money and no mobility, with only her anger and internet research acumen, she discovers her suffering at the hands of a hero is far from unique. When people start listening to the story that her data tells, she realizes she might not be as powerless as she thinks. Because the key to everything is data: knowing how to collate it, how to manipulate it, and how to weaponize it. By tallying up the human cost these caped forces of nature wreak upon the world, she discovers that the line between good and evil is mostly marketing.  And with social media and viral videos, she can control that appearance. It’s not too long before she’s employed once more, this time by one of the worst villains on earth. As she becomes an increasingly valuable lieutenant, she might just save the world."
            },
            {
                "title": "Early Departures",
                "author": "Justin A Reynolds",
                "description": "Justin A. Reynolds, author of Opposite of Always, delivers another smart, funny, and powerful stand-alone YA contemporary novel, with a speculative twist in which Jamal’s best friend is brought back to life after a freak accident . . . but they only have a short time together before he will die again. Jamal’s best friend, Q, doesn’t know he’s about to die . . . again. He also doesn’t know that Jamal tried to save his life, rescuing him from drowning only to watch Q die later in the hospital. Even more complicated, Jamal and Q haven’t been best friends in two years—not since Jamal’s parents died in a car accident, leaving him and his sister to carry on without them. Grief swallowed Jamal whole, and he blamed Q for causing the accident. But what if Jamal could have a second chance? An impossible chance that would grant him the opportunity to say goodbye to his best friend? A new health-care technology allows Q to be reanimated—brought back to life like the old Q again. But there’s a catch: Q will only reanimate for a short time before he dies . . . forever. Jamal is determined to make things right with Q, but grief is hard to shake. And he can’t tell Q why he’s suddenly trying to be friends with him again. Because Q has no idea that he died, and Q’s mom is not about to let anyone ruin the miracle by telling him. How can Jamal fix his friendship with Q if he can’t tell him the truth?"
            }
            ]    
    }, 
    "Sports": {

        "name": "Sports",
        "description": "Sports : engagement in physical activity intended to create a benefit to the participant. Ranging from Amateur to Professional, from incompetent to proficient, for all levels of ability, all nations, all creeds, all genders. As James Joyce said 'I am, a stride at a time'",

        "books": [
            {
                "title": "Far From Normal",
                "author": "Becky Wallace",
                "description": "Maddie McPherson is sick of Normal—both her hometown of Normal, Illinois and being the ‘normal’ sibling. But when she lands a summer internship with a sports marketing firm, she finally has a chance to crawl out of her genius brother’s shadow. Not to mention, a glowing letter of recommendation could secure her admission to her dream college. But Maddie’s nickname is “CalaMaddie” for a reason, and when the company tasks her with repairing the image of teen soccer phenom Gabriel Fortunato, she wonders if she’s set herself up for embarrassment. Gabriel is a tabloid magnet, who’s best-known for flubbing Italy’s World Cup hopes. As Maddie works with him to develop “pleasant and friendly” content for social media, she also learns he’s thoughtful, multi-talented, and fiercely loyal—maybe even to a fault. Falling for a footballer is exactly how CalaMaddie would botch this internship, but with the firm pressuring her to get the job done, perhaps her heart is worth risking?"
            },
            {
                "title": "Furia",
                "author": "Yamile Saied Mendez",
                "description": "In Rosario, Argentina, Camila Hassan lives a double life.At home, she is a careful daughter, living within her mother’s narrow expectations, in her rising-soccer-star brother’s shadow, and under the abusive rule of her short-tempered father.On the field, she is La Furia, a powerhouse of skill and talent. When her team qualifies for the South American tournament, Camila gets the chance to see just how far those talents can take her. In her wildest dreams, she’d get an athletic scholarship to a North American university.But the path ahead isn’t easy. Her parents don’t know about her passion. They wouldn’t allow a girl to play fútbol—and she needs their permission to go any farther. And the boy she once loved is back in town. Since he left, Diego has become an international star, playing in Italy for the renowned team Juventus. Camila doesn’t have time to be distracted by her feelings for him. Things aren’t the same as when he left: she has her own passions and ambitions now, and La Furia cannot be denied. As her life becomes more complicated, Camila is forced to face her secrets and make her way in a world with no place for the dreams and ambition of a girl like her. "
            },
            {
                "title": "The Insomniacs",
                "author": "Marit Weisenberg",
                "description": "When seventeen-year-old competitive diver Ingrid freezes up and sustains a head injury at a routine meet, her orderly life is turned upside down. Now housebound and sedentary on doctor’s orders, Ingrid can’t sleep and is haunted by the question of what triggered her uncharacteristic stage fright.The only thing she remembers about the moment before the dive is seeing Van, her neighbor, former best friend, and forever crush, on the sidelines. Then one sleepless night, she sees Van outside her window...looking right back at her. They tentatively begin “not sleeping” together every night but still living separate lives by day.Ingrid tells herself this is just temporary, but soon, she and Van are up every night together, increasingly intertwined in helping each other put pieces of memory together. As Van works through his own reasons for not being able to sleep, both of them are pulled into a mystery that threatens to turn their quiet neighborhood into a darker place than they realized. "
            } 
        ] 
 
    }, 
}

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/browse")
def browse(): 
    return render_template("browse.html", categories = content)

@app.route("/category/<name>")
def category(name): 
    return render_template("category.html", category = content[name])

@app.route("/<category>/book/<int:id>")
def book(category, id): 
    book = content[category]["books"][id]
    return render_template("book.html", book = book)
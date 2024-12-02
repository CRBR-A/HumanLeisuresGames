#Fifi's Big Adventure
#by Kay Savetz ChatGPT for NaNoGenMo 2023
#cc0 license https://creativecommons.org/public-domain/cc0/

import random
INVENTORY = True #show inventory at the top of each page
APARTMENT = (5,0) #Fifi's home #verify
(x,y)=APARTMENT #starting locale

# Street names for the 10x10 grid
streets = ['Akita Avenue', 'Beagle Boulevard', 'Collie Crescent', 'Dachshund Drive', 'Elkhound Expressway', 'Foxhound Fairway', 'Greyhound Grove', 'Husky Highway', 'Irish Setter Isle', 'Jack Russell Junction']
avenues = ['1st Ave', '2nd Ave', '3rd Ave', '4th Ave', '5th Ave', '6th Ave', '7th Ave', '8th Ave', '9th Ave', '10th Ave']

def inventory():
    global INVENTORY, i_fifi, i_ticket, i_drycleaning, i_flowers, i_money
    if INVENTORY:
        content = "<i>Inventory: "
        if i_fifi:
            content += "Fifi "
        if i_ticket:
            content += "ticket "
        if i_drycleaning:
            content += "drycleaning "
        if i_money:
            content += "money "
        if i_flowers:
            content += "flowers "
        if not (i_fifi or i_ticket or i_drycleaning or i_money or i_flowers):
            content += "empty-handed "
        
        content += "</i>"
    else:
        content=''
    return content                                   


def city_description(x, y):
    descriptions = [
        # Row 1
        ["Nestled amidst the city's concrete landscape, the skate park emerges as a haven for thrill-seekers and skateboard enthusiasts. Vibrant graffiti art splashes across the ramps, half-pipes, and rails, adding a burst of color and creativity to the scene. The rhythmic clatter of wheels on concrete resonates through the air, punctuated by occasional cheers for a well-executed trick. Skaters of all ages weave in and out, perfecting their moves, while onlookers perch on nearby benches, taking in the dynamic display of skill and camaraderie.",
         "A historic statue stands in a small plaza, drawing a crowd of admirers and photographers.",
         "The bustling entrance to a subway station witnesses a continuous stream of commuters.",
         "A small group of protesters peacefully march, holding signs and chanting for a cause.",
         "A street musician strums a guitar, drawing a small crowd of onlookers.",
         "The aroma of food wafts from a cluster of street food vendors, tempting everyone who walks by.",
         "City workers in bright vests repair a section of the sidewalk, directing pedestrians around their work area.",
         "A crowd gathers around a street magician, gasping and applauding at each trick.",
         "Outdoor tables of a popular café are filled with patrons sipping coffee and chatting.",
         "The grand entrance of the city hall, with steps filled with people reading and enjoying the sun."],

        # Row 2
        ["The busy crosswalk flashes 'Walk,' and a crowd moves across the street in unison.",
         "Tourists with cameras hang around a striking piece of street art, discussing its meaning.",
         "Rush hour traffic buzzes through the intersection, with taxis honking and cyclists weaving.",
         "Outside a major bank, an impressive water feature attracts kids trying to catch the water jets.",
         "A green pocket park offers a quiet respite, with benches occupied by readers and daydreamers.",
         "A mime performs near the corner, drawing both amusement and confusion from passersby.",
         "The scent of fresh flowers fills the air, coming from a street vendor's colorful display.",
         "People wait at a bus stop, some checking watches and others lost in their headphones.",
         "A dog park adjacent to the intersection sees joyful dogs running and playing fetch.",
         "A guided city tour group gathers, with the guide holding up an umbrella for visibility."],

        # Row 3
        ["An intersection marked by a giant colorful balloon sale, attracting families with children.",
         "A local artist paints the cityscape on a large canvas, capturing the day's light.",
         "A popcorn vendor does brisk business, with the smell drawing people from a block away.",
         "A group of cyclists gather for a community bike ride, adjusting helmets and checking maps.",
         "A couple dances to a tune played by a nearby radio, drawing applause from onlookers.",
         "A children's lemonade stand does brisk business, with a sign that reads 'For a Good Cause'.",
         "Residents engage in a lively game of street chess, with a crowd gathering to watch the match.",
         "A small pop-up market sells handmade crafts, with shoppers browsing unique finds.",
         "Street performers juggle and do acrobatics, their hat filling up with appreciative tips.",
         "Runners line up for a community race, stretching and preparing for the start whistle."],

        # Row 4
        ["A group of students sketch the surrounding buildings, deeply engrossed in their art.",
         "Families feed pigeons, watching as the birds flock and flutter around them.",
         "Vendors at a farmer's market offer samples of cheeses, fruits, and other local produce.",
         "Children fly kites in an open area, their colorful creations soaring against the blue sky.",
         "A jazz band plays on the corner, their melodies setting the rhythm of the street.",
         "A flea market attracts treasure hunters, with tables full of antiques and curios.",
         "Streetlights illuminate a late-night food stall, serving hungry patrons under the stars.",
         "A community bulletin board is filled with notices, from lost pets to upcoming events.",
         "A vintage car show takes up the block, with enthusiasts admiring the polished beauties.",
         "Outside a community hall, a poster announces a dance that evening. People enter in festive attire."],

        # Row 5
        ["A group of elders play a spirited game of bocce, while onlookers cheer them on.",
         "A colorful mural decorates a building wall, with local artists adding finishing touches.",
         "A bustling outdoor yoga class stretches in unison, their mats covering the park grass.",
         "A mobile pet adoption van parks by the curb, attracting a crowd of animal lovers.",
         "A lively debate ensues at a pop-up book stall, where readers discuss the latest bestsellers.",
         "A lantern festival lights up the evening, with floating lanterns creating a magical glow.",
         "A community potluck spreads on long tables, with neighbors sharing dishes and stories.",
         "A street basketball game draws a crowd, the rhythmic bouncing of balls echoing in the air.",
         "Local musicians have a jam session, their instruments ranging from flutes to drums.",
         "A weekend craft workshop takes place under a tent, with participants painting and crafting."],

        # Row 6
        ["A small tree-lined park provides shade, with families picnicking and enjoying the outdoors.",
         "A community garage sale attracts bargain hunters, tables filled with second-hand goods.",
         "Children with painted faces play at a small playground, their laughter echoing around.",
         "A weekly farmers market bustles with activity, vendors selling fresh produce and artisan goods.",
         "A community band sets up for an evening concert, testing instruments and tuning up.",
         "An open-air art exhibition showcases local talent, with paintings displayed on easels.",
         "A family-friendly puppet show attracts a crowd, children sitting up front in anticipation.",
         "A group practices Tai Chi in an open plaza, their movements graceful and synchronized.",
         "A pop-up outdoor cinema prepares for a movie night, with residents laying out blankets.",
         "Street dancers captivate an audience, their moves energetic and perfectly choreographed."],

        # Row 7 (Residential & Community-focused)
        ["Children chase an ice cream truck, their joyous laughter filling the air.",
        "Residents tend to a community garden, planting flowers and vegetables.",
        "A neighborhood watch group discusses safety measures over cups of coffee.",
        "A local cafe's outdoor seating area is filled with residents enjoying the sunny day.",
        "Families gather at a playground, the air filled with the sound of children's laughter.",
        "A small chapel stands serenely, with a sign announcing Sunday services.",
        "Houses with picket fences line the street, each uniquely decorated with gardens.",
        "A neighborhood cat lounges on a porch, lazily watching the world go by.",
        "Kids set up a lemonade stand, hoping to make a little extra pocket money.",
        "A mail carrier makes rounds, exchanging greetings with the residents."],

        # Row 8 (Events & Gatherings)
        ["A charity marathon's starting point is abuzz with participants warming up.",
        "A local school hosts a science fair, with students proudly displaying their projects.",
        "A health camp offers free check-ups, with doctors volunteering their time.",
        "A community theater rehearses an upcoming play in an open space.",
        "Residents gather for a local film screening under the stars.",
        "A jazz festival stage is being set up, musicians doing sound checks.",
        "A food festival attracts a crowd, the aroma of various cuisines wafting in the air.",
        "An outdoor pottery class takes place, participants molding clay with concentration.",
        "A local band entertains residents in a park, playing popular tunes.",
        "A book swap event is underway, residents exchanging and discussing their favorite reads."],

        # Row 9 (Residential & Community-focused)
        ["A row of townhouses displays flags from various countries, showcasing diversity.",
        "A community bulletin board displays announcements, lost pet posters, and event flyers.",
        "Elderly residents enjoy a morning walk, exchanging greetings with passersby.",
        "A cozy bed-and-breakfast advertises vacancies with a hand-painted sign.",
        "Children safely ride their bicycles on the sidewalk, racing each other.",
        "A community pool is a hub of activity, with families cooling off on a hot day.",
        "A neighborhood bake sale is in full swing, with an array of delicious treats.",
        "A knitting group meets under a tree, working on colorful projects.",
        "A peaceful pond is home to ducks, with families feeding them breadcrumbs.",
        "A local carpenter offers repair services, working diligently in his open-air workshop."],

        # Row 10 (Events & Gatherings)
        ["A dance troupe practices in an open area, their movements graceful and synchronized.",
        "A photography exhibition displays stunning local landscapes and portraits.",
        "A poetry slam event attracts budding poets, sharing their verses with the community.",
        "A kite-flying competition is underway, the sky dotted with colorful kites.",
        "Residents set up for a flea market, displaying antiques and handcrafted items.",
        "A community choir practices harmonious melodies, their voices blending beautifully.",
        "A local brewery offers tastings of their latest brew, attracting a curious crowd.",
        "An art workshop invites residents to paint, sketch, or sculpt in a communal setting.",
        "A neighborhood talent show is in progress, with kids showcasing their skills.",
        "A pop-up music school offers lessons, with the strumming of guitars in the background."]
        ]
    return descriptions[y][x]


def border_description(x, y):
    descriptions = []
    
    # Northern border (forest)
    if y == 0:
        descriptions.append(random.choice([
            "The dense forest to the north blocks your way, with tall trees and thick underbrush.",
            "You hear the distant sound of birds from the northern forest, but you can't go further in that direction.",
            "The forest to the north looks serene, but there's no path leading into it from here."
        ]))
    # Southern border (train tracks)
    elif y == 9:
        descriptions.append(random.choice([
            "Train tracks to the south bar your way, with occasional trains rumbling by.",
            "The sound of a train horn echoes from the south, reminding you that you can't cross the tracks.",
            "You see a freight train passing by on the tracks to the south, carrying goods to distant places."
        ]))
    # Western border (river)
    if x == 0:
        descriptions.append(random.choice([
            "A wide river flows to the west, its waters shimmering under the sun.",
            "You hear the gentle sound of flowing water from the river to the west.",
            "The river to the west acts as a natural boundary, with boats occasionally passing by."
        ]))
    # Eastern border (hills)
    elif x == 9:
        descriptions.append(random.choice([
            "Steep hills rise to the east, their slopes covered in greenery.",
            "The eastern hills offer a scenic view, but you can't climb them from here.",
            "Birds of prey circle over the eastern hills, their cries echoing in the distance."
        ]))
    if y == 7:
        windy_descriptions = [
            "This street is notoriously gusty, known for its strong westerly wind that whistles between the buildings.",
            "An offshore breeze from the nearby river makes this area particularly windy, pushing gusts from the west.",
            "You brace yourself as a strong gust of wind sweeps from the west, reminding you of this street's reputation for windiness.",
            "The trees lining the street sway vigorously, their leaves rustling loudly in the consistent west-to-east breeze.",
            "Locals often comment about the unique wind tunnel effect on this street, with breezes always rushing from the west.",
            "Wind chimes from nearby homes tinkle melodiously, carried by this street's persistent westerly breeze.",
            "Flags flutter and snap in the brisk wind that always seems to come from the west on this street.",
            "You notice wind vanes on nearby rooftops pointing westward, indicating the prevailing westerly wind.",
            "Pedestrians lean slightly into the wind as they walk, a testament to the strength of the gusts here.",
            "Old tales suggest this street was designed to harness the wind, and with each westerly gust, you can't help but wonder if there's some truth to the legends."
        ]
        descriptions.append(windy_descriptions[x])

    if x==9 and y==9:
        descriptions.append("Sitting on a park bench is a grizzled old man with deep-set eyes and a weathered face. His gray beard flows down like a river of time, and despite his rugged appearance, he seems wise beyond his years.")
        if not (i_ticket or i_drycleaning):
            descriptions.append("He looks at you and whispers 'Feeling shook? Check a book.'")
        elif not i_fifi:
            descriptions.append("He eyes you and says 'Lost a friend? Park's the trend.'")
        elif not (i_money or i_flowers):
            descriptions.append("He intones, 'Money on your mind? Get wet or grind.'")
        elif i_fifi and i_flowers and i_drycleaning:
            descriptions.append("He closes his eyes and whispers 'Success, you've done your best.'")
        else:
            descriptions.append("He smiles enigmatically.")  # Default line if none of the conditions match
        
    return ' '.join(descriptions)
    
def fifi_actions():
    global x,y
    actions = [
        "Fifi sniffs a nearby fire hydrant, her tail wagging.",
        "A leaf blows by and Fifi chases after it playfully.",
        "Fifi barks excitedly at a butterfly fluttering nearby.",
        "Every now and then, Fifi stops to mark her territory.",
        "Fifi's ears perk up as she hears a distant dog barking.",
        "A car horn honks, and Fifi looks around, curious.",
        "Fifi spots a squirrel and tugs on her leash, eager to chase.",
        "You feel a tug as Fifi tries to chase a passing car.",
        "Fifi rolls around in the grass, looking content.",
        "Fifi looks up at you with a joyful expression, clearly enjoying the walk.",
        "You pause as Fifi takes a moment to drink from a puddle.",
        "A child approaches and pets Fifi, making her wag her tail in delight.",
        "Fifi suddenly starts digging a small hole in the ground, curious about something.",
        "The wind blows, and Fifi's ears flutter, making her look even more adorable.",
        "Fifi finds a stick and proudly carries it in her mouth.",
        "A fellow dog walker passes by, and Fifi greets the other dog with a friendly sniff.",
        "Fifi finds a shady spot under a tree and takes a brief rest.",
        "You laugh as Fifi tries to chase her own tail, spinning in circles.",
        "Fifi perks up, sensing something interesting in a nearby bush.",
        "A loud noise startles Fifi, and she hides behind your legs for a moment.",
        "Fifi finds an old tennis ball and excitedly starts playing with it.",
        "A street musician plays a tune, and Fifi tilts her head, intrigued by the sound.",
        "Fifi jumps up, trying to catch a floating soap bubble created by a nearby child.",
        "A bird lands nearby, and Fifi watches it intently, her instincts kicking in.",
        "Fifi finds a patch of flowers and takes a moment to smell them.",
        "A gentle breeze ruffles Fifi's fur, making her look even fluffier.",
        "Fifi playfully barks at her reflection in a shop window.",
        "Fifi looks up at the sky, curious about a passing airplane.",
        "Fifi's nose twitches as she sniffs a new scent in the air.",
        "Fifi playfully nudges a fallen leaf with her nose, pushing it around.",
        "You and Fifi pause as she takes in the sights and sounds of the bustling city.",
        "A nearby cat catches Fifi's attention, but a gentle tug on her leash keeps her on track.",
        "Fifi's curiosity is piqued by a floating balloon and she tries to jump up and catch it.",
        "A gentle stream of water from a fountain becomes Fifi's impromptu drinking spot.",
        "Fifi barks joyfully at the sound of distant church bells ringing.",
        "Fifi gets excited when she hears the jingle of an ice cream truck in the distance.",
        "A child gives Fifi a pat on the head, and she responds with a happy wag.",
        "Fifi's attention is caught by a colorful kite flying high in the sky.",
        "Fifi tries to join a group of pigeons but they take flight, much to her disappointment.",
        "Fifi's ears twitch with curiosity as she hears the distant train horn.",
        "Fifi sits and offers a paw to a group of tourists taking pictures, becoming an instant attraction.",
        "Fifi finds joy in the simple things, like chasing the shadows of birds flying overhead."
        
    ]
    if(x==6 and y==1): #outside vet #verify
        return 'Fifi becomes notably restless on this particular street corner. Her tail tucks slightly, and she pulls on the leash, eager to move away from the area.'
    else:
        return random.choice(actions)
    
def looking_for_fifi():
    messages = [
        "You scan the area, hoping to catch a glimpse of Fifi.",
        "A feeling of worry settles in as you continue searching for Fifi.",
        "You call out for Fifi, listening for any responding bark or whine.",
        "Every rustle and movement catches your attention; could it be Fifi?",
        "You imagine Fifi's excited bark and hope to hear it soon.",
        "Memories of Fifi's playful antics make you more determined to find her.",
        "You remember the first day you met Fifi and how she instantly stole your heart.",
        "The thought of Fifi being lost and scared pushes you to search even more diligently.",
        "You check under benches and behind trees, hoping to find Fifi hiding.",
        "The streets seem so empty without Fifi's joyful presence by your side.",
        "You ask passersby if they've seen a dog matching Fifi's description.",
        "Every dog you see from a distance raises your hopes, only to be dashed when it's not Fifi.",
        "The sound of distant barking makes you rush forward, hoping it's Fifi.",
        "A child's laughter reminds you of Fifi's playful nature, and you hope she's safe.",
        "You imagine the relief you'll feel when you finally spot Fifi and hold her close.",
        "The city noises drown out your calls, but you keep shouting Fifi's name, hoping she'll hear.",
        "A poster of a missing pet makes you even more anxious. You have to find Fifi soon.",
        "The weight of Fifi's absence feels heavy as you continue your search.",
        "You replay the last moments you saw Fifi, wishing you had been more careful.",
        "Every wagging tail in the distance brings a surge of hope.",
        "You clutch Fifi's leash tighter, hoping for a reunion soon.",
        "You pause for a moment, taking a deep breath and whispering a silent plea to find Fifi.",
        "Each corner you turn, you hope to see Fifi's familiar face.",
        "Your heart races each time you think you spot a dog that might be Fifi.",
        "You wish you could communicate with every pet you meet, asking them if they've seen Fifi.",
        "Every park and open space becomes a potential spot where Fifi might be playing.",
        "You picture Fifi's curious eyes and hope she's not too scared.",
        "You try to think like Fifi, wondering where she might go if she were exploring or chasing something.",
        "You remember teaching Fifi tricks and commands, hoping she's using her smarts to stay safe.",
    ]
    return random.choice(messages)

def get_locations():
    locations = {
        APARTMENT: {"name": "Fifi's Person's Apartment", "description": "You recognize the familiar entrance to Fifi's person's apartment building on this street.",\
        "inside": "Stepping into the apartment, you're immediately enveloped by its warmth and familiarity. The walls are adorned with pictures of various dogs, including several of Fifi in her more playful moments. A cozy couch sits in the living area with a few dog toys scattered around. There's a faint scent of a recently cooked meal from the kitchen, making the place feel even more like home."},
        (9,3): {"name": "Gym", "description": "On the corner, there's a modern gym with large glass windows. Inside, people are working out on treadmills and lifting weights.",
        "inside": "Inside the gym, it's energetic with the sounds of weights clinking and treadmills humming. People are in their workout zones, some listening to music, others focused on their routines."},
        (9,8): {"name": "Library", "description": "Standing tall on this block is a grand library with its majestic tall columns. Many people are walking in and out, each engrossed in their chosen books.",
        "inside": "The grandeur of the library's interior matches its exterior. Tall bookshelves, reading nooks, and soft lighting make it a haven for book lovers. You can hear the soft rustling of pages turning."},
        (4,2): {"name": "Fountain", "description": "A majestic fountain stands in this plaza with water cascading down beautifully. You observe people around it, making wishes and tossing coins with hope.",
        "inside": "Taking a leap of spontaneity, you decide to climb into the fountain! The cold water splashes around you, and you can't help but laugh. You notice some change at the bottom."},
        (1,9): {"name": "Dog Park", "description": "As you approach, you see a fenced dog park where dogs are joyfully playing fetch and running around. Nearby, dog owners chat on the benches.",
        "inside": "Inside the dog park's fence, there's a sense of joy and freedom. Dogs of all sizes run around, some chasing balls, others making new friends. A water station is set up for them to drink."},
        (4,8): {"name": "Dry Cleaners", "description": "There's a dry cleaner's shop on this stretch. Through the window, you can see various clothes hanging inside, neatly pressed and waiting for their owners.",
        "inside": "The dry cleaner's interior is organized and clean. Conveyors move with cleaned clothes in protective wraps. A seamstress works on minor repairs at one side."},
        (1,1): {"name": "Flower Shop", "description": "You notice a charming flower shop displaying a colorful array of flowers on this block. The enchanting scent of roses and lilies fills the air.",
        "inside": "Entering the flower shop, you're surrounded by vibrant colors. The florist is arranging a bouquet, and there's a gentle hum from the cooler preserving delicate flowers."},
        (5,9): {"name": "Cafe", "description": "On the corner, you spot a cozy cafe, and you're immediately drawn to the aroma of fresh coffee beans. Inside, people are sipping their drinks and engaged in warm conversations.",
        "inside": "The cafe's interior is intimate and warm. The barista works the espresso machine, and there's a display of freshly baked goods. Some patrons work on their laptops, while others chat."},
        (3,6): {"name": "Bakery", "description": "A delightful bakery stands here with a tempting display of freshly baked bread and pastries. The irresistible scent of baking wafts around, making you feel hungry.",
        "inside": "The inside of the bakery is warm from the ovens. Behind the counter, bakers knead dough and pull out fresh batches of cookies. There's a chalkboard menu detailing today's specials."},
        (6,1): {"name": "Vet", "description": "There's a vet clinic here with a welcoming sign of a cat and dog. From inside, you can faintly hear the meows and barks of pets.",
        "inside": "The vet's reception is calm and welcoming. A cat lounges in its carrier, and a dog wags its tail, waiting for a treat from the receptionist. The walls have posters about pet care."},
        (0,5): {"name": "Sanctuary", "description": "A quaint and unassuming building with a carved dove in flight signifies peace and acceptance. The sign out front reads 'Non-Denominational House of Worship: All are Welcome'. Soft choral music emanates from within, creating a serene ambiance around.",
        "inside": "The interior is serene and filled with soft lighting from stained glass windows. Wooden pews are neatly arranged facing a simple altar. A few individuals sit quietly, lost in reflection or prayer. The air is filled with a gentle scent of incense, and the overall atmosphere is one of peace and contemplation."},
        (4,4): {"name": "Art Gallery", "description": "The Art Gallery, an architectural marvel, stands elegantly on this street. Its modern facade, juxtaposed against classic design elements, boasts large windows that allow passersby a glimpse of the masterpieces within.",
        "inside": "As you step into the art gallery, the hushed atmosphere envelops you. Walls adorned with paintings from various eras tell a visual story of artistic evolution. Paintings, sculptures, and other artworks are meticulously displayed, each piece telling its own story. The soft lighting and quiet murmurs of fellow art enthusiasts create a contemplative atmosphere."},
        (6,6): {"name": "Performance Venue","description": "The grand facade of the Performance Venue stands out with its intricate architectural details and large poster displays of upcoming shows. A red carpet leads to the main entrance, and the faint sound of rehearsing instruments hints at the artistic magic that happens within.",
        "inside": "The opulent interior is adorned with gold leaf details and plush red velvet seats. Crystal chandeliers hang from the ceiling, casting a warm glow over the audience area. The stage is set for the evening's performance, with props and instruments in place, awaiting the artists."},
        (8,0): {"name": "Your Apartment","description": "Your Apartment building stands tall with a familiar red brick facade. The entrance has a small canopy, and potted plants flank either side of the door.",
        "inside": "Your apartment feels warm and welcoming. The living room is adorned with personal mementos and photos. A comfortable couch faces a TV, and nearby, there's a small dining area. The scent of the last meal cooked lingers pleasantly in the air. It's a haven of personal comfort and memories."},
        (0,7): {"name": "Antique Shop","description": "An antique shop looks like it's from another era with its vintage signage and ornate wooden door.",
        "inside": "Every corner of the shop holds treasures from the past. From old clocks to vintage jewelry, the collection is vast and fascinating."},
        (7,2): {"name": "Pizzeria","description": "A pizzeria stands out on the street with its vibrant neon sign. Through the windows, you can see families and friends gathered at tables, enjoying their meals.",
        "inside": "As you step into the pizzeria, the warm ambiance envelops you. Red and white checkered tablecloths adorn the wooden tables. The walls are decorated with vintage Italian posters and the soft hum of conversations blends with the sizzle from the open kitchen. Chefs can be seen expertly tossing dough and assembling pizzas before sliding them into the stone oven."},
        (2,3): {"name": "Retro Arcade","description": "Neon lights and the sound of classic game tunes beckon you to a Retro Arcade. The entrance is guarded by life-sized statues of iconic video game characters.",
        "inside": "Rows of vintage arcade machines line the walls, each game transporting players to different pixelated worlds. The familiar sounds of coin inserts, joystick moves, and victory jingles create an energetic symphony. In one corner, a high-score board boasts the legends of the arcade, and a snack bar offers refreshments and treats for players taking a break."},
        (8,4): {"name": "Karaoke Bar","description": "A Karaoke Bar's entrance is marked by a neon microphone sign, flickering to the beat of the latest pop hit. The faint sounds of enthusiastic (if not always pitch-perfect) singing can be heard from outside, combined with the occasional burst of laughter and applause.",
        "inside": "Karaoke Bar is dimly lit, with colorful stage lights casting a revolving glow on the main stage. Patrons sit at tables, sipping on drinks, while the brave ones take to the stage, belting out their chosen tunes. A large screen displays lyrics, and the walls are adorned with posters of iconic musicians and bands. The atmosphere is light-hearted and jovial, with everyone cheering on the performers, regardless of their singing prowess."},
        (8,9): {"name": "Candle Shop","description": "Nestled between two buildings is a quaint candle shop, its window adorned with candles of all shapes and colors. The gentle glow from within, combined with the soft fragrance wafting out, makes it an inviting location.",
        "inside": "Inside the candle shop is a sensory delight. Shelves upon shelves of candles in every conceivable color and scent line the walls. Gentle music plays in the background, and the subtle intermingling of aromas — from lavender to fresh linen to sandalwood — creates a calming ambiance."},
        (5,5): {"name": "Clock Tower", "description": "Standing majestically in the center of the city is the historic clock tower, its aged stone facade adorned with intricate carvings of time's passage. A spiral staircase visible through an arched doorway suggests that one can climb to the top for a panoramic view of the surroundings.",
        "inside": "From the top of the ancient clock tower, you're enveloped by a slightly musty aroma. The cool, stone walls seem to whisper tales of times gone by as you ascend. As you reach the peak, a dizzying panorama unfolds before you, granting a clear and unparalleled vantage point over the sprawling city. Every corner, every alley, and every street lies beneath you, like a miniature world waiting to be explored. The distant hum of the city life blends with the rhythmic ticking of the tower's grand clock, a testament to the passage of time."}
    }
    return locations

def special(x, y):
    global i_fifi, i_ticket, i_drycleaning, i_flowers, i_money
    locations = get_locations()

    # Check if the given x,y matches any special location
    location = locations.get((x, y))

    if location:
        return 0, location["name"], location["description"], location["inside"]
    else:
        return False
    
def room_actions(location):
    global i_fifi, i_drycleaning, i_flowers, i_ticket, i_money, page_id
    output='ERROR'
    if location=="Vet":
        if i_fifi:
            output = 'The moment you step into the vet\'s office, Fifi seems to sense where she is. Her tail goes between her legs, and she starts to whimper. Before you can comfort her, she suddenly pulls out of her collar and darts out the door. A vet assistant tries to catch her, but she\'s too quick. "She\'s probably just scared," the vet says reassuringly, "Most pets aren\'t fans of this place. You might want to look for her outside."'
            page_id = newpath(0,i_drycleaning,i_flowers,i_ticket,i_money)
        else:            
            output = 'The vet\'s office is filled with the soft mewls of cats and the occasional bark of dogs. You approach the receptionist and show her a picture of Fifi, asking if anyone has brought her in. She shakes her head, "Sorry, we haven\'t seen your dog. But leave your contact information, and we\'ll call if she shows up." You thank her and decide to continue your search outside.'

    elif location == "Dog Park":
        if i_fifi:
            output = "You and Fifi enter the dog park, and her tail wags with excitement. She immediately joins a group of playful dogs, chasing a frisbee and rolling in the grass. After a while, you call her over, and she comes back, looking extremely happy. A fellow dog owner comments, 'She's got a lot of energy! It's great she has a place like this.'"
        else:
            output = "As you approach the dog park, you spot a familiar furry face. It's Fifi! She's playing joyfully with some other dogs. As you call out her name, she looks up and runs towards you, wagging her tail. It seems she's made some new friends while she was away. A nearby dog owner mentions, 'She's been the star of the park today!' You're relieved to have found her."
            page_id = newpath(1,i_drycleaning,i_flowers,i_ticket,i_money)

    elif location == "Dry Cleaners":
        if i_ticket:
            page_id = newpath(i_fifi ,1,i_flowers,0,i_money)
            if i_fifi:
                output = "You and Fifi walk into the dry cleaners. The clerk, recognizing Fifi, chuckles and says, 'Well, hello there. Helping with the chores today, Fifi?' You hand over the ticket and receive your freshly cleaned clothes. They smell wonderful. Fifi sniffs them approvingly. 'No fur this time!' the clerk jokes."
            else:
                output = "You walk into the dry cleaners and hand over your ticket. The clerk quickly retrieves your clothes, freshly cleaned and neatly folded. The scent of fresh laundry fills your nostrils. As you leave, you can't help but think how much Fifi would've enjoyed the outing."
        else:
            if i_fifi:
                output = "You and Fifi enter the dry cleaners. The clerk smiles and greets Fifi warmly, 'Look who's here!' However, without a ticket, there's not much to do. Fifi seems to enjoy the cool air and the chime of the doorbell."
            else:
                output = "You step into the dry cleaners, but without a ticket, you quickly realize there's not much to do here. The hum of the machines and the soft chatter make it a peaceful place, though."

    elif location == "Flower Shop":
        if i_fifi:
            output = "Fifi gets excited at the sight of the flowers and tries to play with them, causing a bit of a mess. The shopkeeper gives you a stern look. "
            if i_money:
                output += "Remembering Fifi's owner's request for flowers, you pick out a lovely bouquet. You hand over the money and take the flowers."
                page_id = newpath(i_fifi, i_drycleaning, 1, i_ticket, 0)
            else:
                output += "You apologize to the shopkeeper and realize you can't buy the requested flowers without money anyway. It's best to leave before causing any more trouble."
        else:
            if i_money:
                output = "The shop is filled with colorful and fragrant flowers. Remembering Fifi's owner's request, you pick out a lovely bouquet. You hand over the money and take the flowers."
                page_id = newpath(i_fifi, i_drycleaning, 1, i_ticket, 0)
            else:
                output = "The shop is filled with colorful and fragrant flowers. You'd love to fulfill the request for a bouquet, but unfortunately, you don't have any money with you."

    elif location == "Gym":
        if i_fifi:
            output = "As soon as you step inside with Fifi, a staff member approaches with a worried expression. 'Sorry, no pets allowed in the gym,' they say. Fifi looks around curiously, probably intrigued by all the moving machines."
        else:
            if not i_money and not i_flowers:
                output = "While looking around, you spot a lost wallet on the floor. After handing it over to the reception, the grateful owner rewards you for your honesty. You feel a bit richer now!"
                page_id = newpath(i_fifi, i_drycleaning, i_flowers, i_ticket, 1) # Adding money for the reward
            else:
                output = "The gym is bustling with activity. You observe people lifting weights, some are on treadmills, and a group is attending a yoga class. You admire their dedication, but then think to yourself, 'Who needs a gym when you're chasing after dogs all day?'"

    elif location == "Library":
        if i_fifi:
            output = "The librarian, a kind elderly lady, spots you at the entrance with Fifi. 'I'm sorry, pets aren't allowed inside.' She does, however, hand Fifi a biscuit, which she happily munches on. You contemplate returning without Fifi to explore the library."
        else:
            if not i_ticket:
                output = "The library is quiet, with a few patrons engrossed in their reading. While you're browsing, something catches your eye: a piece of paper fluttering in an air vent. Curious, you retrieve it and realize it's the dry cleaning ticket!"
                page_id = newpath(i_fifi, i_drycleaning, i_flowers, 1, i_money)
            else:
                output = "You spend some time browsing through the shelves, enjoying the vast collection of books the library offers. However, the weight of guilt for losing Fifi tugs at your heart, urging you to continue your search."

    elif location == "Cafe":
        if i_fifi:
            output = "The barista behind the counter gives Fifi a friendly smile as you enter. 'We're dog-friendly here!' she says, pointing to a corner where there's a bowl of fresh water for canine visitors. Fifi happily laps up some water, wagging her tail."
            if i_money:
                output += " With the money you have, you decide to treat yourself to a hot cup of coffee. As you sip the warm beverage, you note that you still have some money left over for any other needs."
            else:
                output += " The inviting aroma of coffee fills the air, but without money, you decide to just enjoy the atmosphere for a while before moving on."
        else:
            output = "The cafe is warm and inviting. The smell of freshly brewed coffee is irresistible. You take a seat and enjoy the ambiance, occasionally glancing out the window, hoping to spot Fifi."
            if i_money:
                output += " You decide to order a cup of coffee, savoring its warmth and flavor. After paying, you're relieved to find you still have some money left."

    elif location == "Bakery":
        if i_fifi:
            output = "The bakery is filled with the delightful aroma of freshly baked goods. As you're admiring the pastries on display, a customer accidentally drops a cookie. Before you can react, Fifi, ever the opportunist, quickly snatches it up and munches on her unexpected treat. The customer laughs, 'Guess it's hers now!' You apologize, but they assure you it's alright. 'All part of the fun of having a dog,' they chuckle."
        else:
            output = "The bakery buzzes with activity. The display is lined with a variety of bread, pastries, and cakes, making your mouth water. As you admire the baked goods, you wonder if Fifi would have liked something from here. The thought makes you even more eager to find her."

    elif location == "Sanctuary":
        if i_fifi:
            output = "The calm and peaceful ambiance of the sanctuary envelops you as you step in with Fifi. While some attendees give curious glances at the canine visitor, most offer warm smiles, silently acknowledging the sanctuary's all-inclusive welcome. Fifi, sensing the tranquility, calmly trots beside you, occasionally stopping to curiously sniff at the ends of pews. A nearby attendee, observing Fifi, whispers, 'All creatures, great and small, are welcome here.' You nod in appreciation, feeling grateful for such accepting spaces."
        else:
            output = "The serene environment of the sanctuary allows you a moment of stillness amid the chaos of the city and your search for Fifi. You take a seat in one of the pews, allowing the calmness to wash over you. Silently, you say a prayer, hoping for guidance and the safe return of Fifi. The soft glow from the stained glass windows and the scent of incense provide a comforting backdrop to your moment of reflection."

    elif location == "Art Gallery":
        if i_fifi:
            output = "Fifi seems particularly interested in a painting of dogs playing poker, and you wonder if she recognizes the subject."
        else:
            output = "One particular painting, depicting a lively street scene, features a small dog that bears a striking resemblance to Fifi. A pang of longing hits you, and you're reminded of your mission to find her."

    elif location == "Performance Venue":
        if i_fifi:
            output = "Fifi seems captivated by the music emanating from the stage. Her ears perk up and her tail wags rhythmically, as if she's appreciating the melody."
        else:
            output = "The sound of a lone violin strikes a chord, making you miss Fifi even more."

    elif location == "Your Apartment":
        if i_fifi:
            output = "Fifi, recognizing the place from previous visits, immediately finds a comfy spot on the couch. She gives a contented sigh, clearly at ease in the familiar environment."
        else:
            output = "The apartment feels a bit empty without Fifi's lively presence. You spot a chew toy she left behind during her last visit and hope to reunite her with it soon."

    elif location == "Antique Shop":
        if i_fifi:
            output = ("As you meander through the shop, Fifi becomes particularly intrigued by an old gramophone. "
                      "She tilts her head curiously, ears perked, as she inspects the cone-shaped horn. "
                      "Perhaps she's wondering if it might spring to life with a familiar voice.")
        else:
            output = ("As you look around, you can't help but imagine how Fifi might react to some of these oddities.")

    elif location == "Retro Arcade":
        if i_fifi:
            output = "Fifi seems fascinated by a claw machine filled with plush toys. She excitedly barks each time someone tries to grab a prize, cheering them on in her own way."
        else:
            output = "You notice a 'Duck Hunt' arcade machine, with its iconic giggling dog. A wave of nostalgia washes over you, and thoughts of Fifi come rushing in. How you wish she were beside you, much like the faithful hound in the game."

    elif location == "Karaoke Bar":
        if i_fifi:
            output = "As the next singer takes the stage to sing a particularly high note, Fifi joins in with an enthusiastic 'aroooo!' The crowd erupts in laughter and applause, clearly enjoying her impromptu duet. For a moment, Fifi seems to consider a career in music, her tail wagging to the rhythm."
        else:
            output = "You can't help but get swept up in the music and the atmosphere of the Karaoke Bar. As each performer takes the stage, you imagine how much fun it would be to share this experience with Fifi. Maybe she'd even have a favorite song?"

    elif location == "Candle Shop":
        if i_fifi:
            output = "Fifi seems particularly drawn to a section of uniquely scented candles. To your amusement, she sniffs intently at a bacon-scented candle, her tail wagging in approval."
        else:
            output = "While admiring a display of artisan candles, you notice one shaped like a small dog. It reminds you of Fifi, and you imagine her playful curiosity in this fragrant wonderland."

    elif location == "Pizzeria":
        if i_fifi:
            output = ("Fifi's nose twitches, clearly picking up on the delicious scent. As you wait, "
                      "the kid behind the counter winks at you and sneaks a small slice of cheese pizza to Fifi, "
                      "who gobbles it down with glee. 'Dogs love our pizza too!' the kid chuckles.")
        else:
            output = ("The pizzeria bustles with activity, the delicious scent of baking dough and melting cheese pervading the atmosphere. "
                      "You can't help but think how much Fifi would have loved the aroma. "
                      "As you look around, you notice the kid behind the counter playfully interacting with customers.")

    elif location == "Clock Tower":
        tower_x, tower_y = 5, 5 #verify
        output = ""

        locations = get_locations()
    
        for (x, y), loc in list(locations.items())[:7]:
            if x == tower_x and y == tower_y:
                # This is the clock tower itself, so skip it.
                continue

            if x < tower_x:
                if y < tower_y:
                    direction = "northwest"
                elif y == tower_y:
                    direction = "west"
                else:
                    direction = "southwest"
            elif x == tower_x:
                if y < tower_y:
                    direction = "north"
                elif y == tower_y:
                    # This should never happen as we've already skipped the clock tower.
                    pass
                else:
                    direction = "south"
            else:
                if y < tower_y:
                    direction = "northeast"
                elif y == tower_y:
                    direction = "east"
                else:
                    direction = "southeast"

            location_name = loc["name"]
            output += "Off to the {}, you can see {} {}. ".format(direction, 'the' if location_name != "Fifi's Person's Apartment" else '', location_name)

    elif location == "Fountain":
        if i_fifi:
            output = "Fifi, curious as ever, dips her paws in the water too."
            if i_money or i_flowers:
                output += " Although the sight of the coins tempts you, you decide against taking any, feeling guilty about the thought."
            else:
                output += " The moral dilemma strikes you, but the need for money to buy Fifi's flowers overpowers your hesitation. You quickly gather a handful of coins, hoping nobody notices."
                page_id = newpath(i_fifi, i_drycleaning, i_flowers, i_ticket, 1)
        else:
            output = "The fountain's beauty is captivating, with water cascading elegantly into the pool below. You notice people tossing coins and making wishes. The sight makes you ponder about making a wish for Fifi's safe return."
            if i_money or i_flowers:
                output += " You don't need any money, so you decide it's best not to take any coins, even though the temptation is there."
            else:
                output += " Pondering the moral questions it raises, you decide to take some coins, rationalizing it as a necessity to buy flowers."
                page_id = newpath(i_fifi, i_drycleaning, i_flowers, i_ticket, 1)

    elif location == "Fifi's Person's Apartment":
        if i_fifi:
            if i_drycleaning and i_flowers:
                # Winning Scenario
                output = ("Arriving back at the apartment, Fifi's owner greets you both with a warm smile. Seeing the dry cleaning and flowers, "
                          "they express their heartfelt gratitude. 'I couldn't have asked for more. Thank you!' they say. Fifi, excitedly wagging her tail, "
                          "gives you a loving lick, seemingly thanking you for the day's adventure.")
            elif i_ticket and i_flowers:
                # Mild Disappointment Scenario
                output = ("You return with Fifi and a beautiful bouquet of flowers. Fifi's owner is delighted to see their pet and the flowers but "
                          "notices the dry cleaning ticket in your hand. 'Oh, I see. Well, at least you did half the errands,' they say with a slight frown. "
                          "Fifi gently licks your hand, her way of saying goodbye.")
            elif i_ticket:
                # Another Losing Scenario
                output = ("You step into the apartment with Fifi, presenting the dry cleaning ticket. Fifi's owner looks at you, clearly upset. 'Did you even "
                          "try to run my errands? Did you even walk Fifi at all?' they exclaim, visibly frustrated. Despite the tension, Fifi gives you a gentle "
                          "lick, showing her gratitude for the time spent together.")
            else:
                # Middle Scenario
                output = ("You and Fifi enter the apartment, greeted by a relieved but visibly disappointed owner. 'I'm just glad Fifi's safe,' they say, "
                          "while clearly hoping for more. Fifi wags her tail and licks your face, grateful for the journey you shared.")
        else:
            # Losing Scenario
            output = ("You return to the apartment alone, your heart heavy. The owner's face falls as you explain the situation. 'I can't believe Fifi's gone...' "
                      "they say, visibly upset. The disappointment in their eyes makes you realize the gravity of your failure.")

    return output            

def newpath(fifi,drycleaning,flowers,ticket,money):
    global x,y
    special=0
    
    # Convert the inventory to a binary string
    binary_inventory = str(fifi) + str(drycleaning) + str(flowers) + str(ticket) + str(money)

    # Convert the binary string to a decimal number
    decimal_inventory = int(binary_inventory, 2) + 1

    # Convert the decimal number to a two-digit string
    two_digit_inventory = f"{decimal_inventory:02}"

    # Combine everything to get the page_id
    return str(special) + str(x) + str(y) + two_digit_inventory

def newpathnewxy(fifi,drycleaning,flowers,ticket,money):
    global new_x,new_y
    special=0
    
    # Convert the inventory to a binary string
    binary_inventory = str(fifi) + str(drycleaning) + str(flowers) + str(ticket) + str(money)

    # Convert the binary string to a decimal number
    decimal_inventory = int(binary_inventory, 2) + 1

    # Convert the decimal number to a two-digit string
    two_digit_inventory = f"{decimal_inventory:02}"

    # Combine everything to get the page_id
    return str(special) + str(new_x) + str(new_y) + two_digit_inventory


def move(direction, x, y):
    if direction == 'Go West': x -= 1
    if direction == 'Go East': x += 1
    if direction == 'Go North': y -= 1
    if direction == 'Go South': y += 1
    return x, y

def generate_navigation(x, y):
    directions = []
    if x > 0: directions.append('Go West')
    if x < 9: directions.append('Go East')
    if y > 0: directions.append('Go North')
    if y < 9: directions.append('Go South')
    return directions

# 3. Generate pages

i_fifi=1
i_drycleaning=0
i_flowers=0
i_ticket=1
i_money=0
startpage = newpath(i_fifi,i_drycleaning,i_flowers,i_ticket,i_money) #start with Fifi and ticket

page_contents = {}

for i_fifi in [0, 1]:
    for i_drycleaning in [0, 1]:
        for i_flowers in [0, 1]:
            for i_ticket in [0, 1]:
                for i_money in [0, 1]:
                    if (i_drycleaning and i_ticket):
                        continue
                    if (i_flowers and i_money):
                        continue

                    for y in range(10):
                        for x in range(10):
                            specialinfo = special(x,y)

                            # Convert the inventory to a binary string
                            binary_inventory = str(i_fifi) + str(i_drycleaning) + str(i_flowers) + str(i_ticket) + str(i_money)

                            # Convert the binary string to a decimal number
                            decimal_inventory = int(binary_inventory, 2) + 1

                            # Convert the decimal number to a two-digit string
                            two_digit_inventory = f"{decimal_inventory:02}"

                            # Combine everything to get the page_id
                            specialbit = 0
                            page_id = str(specialbit) + str(x) + str(y) + str(two_digit_inventory)
                            
                            content = f"<a name=\"page{page_id}\"></a>"
                            content += f"<p>Page {page_id}"
                            content += f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{inventory()}</p>"
                            content += f"<h2>{streets[y]} & {avenues[x]}</h2>"
                            content += f"<p>{city_description(x, y)} "
                            content += f"{border_description(x, y)} "

                            if specialinfo:
                                content += f"{specialinfo[2]}"
                            content += '</p>'
                            
                            if i_fifi:
                                if x !=0 and y !=0: #no fifi action at skate park
                                    content += f"{fifi_actions()}</p>"
                            else:
                                content += f"{looking_for_fifi()}</p>"

                            if y==7 and i_ticket:
                                content += f"<p>Oh no! A sudden gust sweeps up your dry cleaning ticket, sending it fluttering to the east and quickly out of sight!</p>"                              

                            if x==0 and y==0 and i_fifi:
                                content += f"<p>A skateboarder misjudges his distance and swoops dangerously close to Fifi. Startled, she yelps and darts away in a panic. You sprint after her, but she's too swift, disappearing from sight! The skater comes to a halt, looking genuinely remorseful. 'Sorry 'bout your dog, dude,' he says, scratching the back of his head.</p>"                              

                            for direction in generate_navigation(x, y):
                                new_x, new_y = move(direction, x, y)
                                if y==7 and i_ticket: #special case for ticket blowing away
                                    link_page_id = newpathnewxy(i_fifi,i_drycleaning,i_flowers,0,i_money)
                                elif x==0 and y==0: #skate park, fifi runs away!
                                    link_page_id = newpathnewxy(0,i_drycleaning,i_flowers,i_ticket,i_money)
                                else:
                                    link_page_id = str(specialbit) + str(new_x) + str(new_y) + str(two_digit_inventory)
                                content += f"If you want to {direction.lower()}, turn to <a href='#page{link_page_id}'>page {link_page_id}</a>.<br />"

                            if specialinfo:
                                specialbit = 1
                                link_page_id = str(specialbit) + str(x) + str(y) + str(two_digit_inventory)

                                if y==7 and i_ticket: #special case for ticket blowing away
                                    binary_inventory = str(i_fifi) + str(i_drycleaning) + str(i_flowers) + str('0') + str(i_money)
                                    decimal_inventory = int(binary_inventory, 2) + 1
                                    two_digit_inventory = f"{decimal_inventory:02}"
                                    temp_page_id = str(specialbit) + str(x) + str(y) + str(two_digit_inventory)
                                    content += f"If you want to enter {'the' if (x, y) != APARTMENT else ''} {specialinfo[1]}, turn to <a href='#page{temp_page_id}'>page {temp_page_id}</a>.<br />"
                                else:
                                    content += f"If you want to enter {'the' if (x, y) != APARTMENT else ''} {specialinfo[1]}, turn to <a href='#page{link_page_id}'>page {link_page_id}</a>.<br />"

                            content += "<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><hr>\n"

                            page_contents[page_id] = content


                            #now, is there an enterable place from here?
                            if specialinfo:
                                #specialbit = 1
                                #room_page_id = str(specialbit) + str(x) + str(y) + two_digit_inventory
                                content = f"<a name=\"page{link_page_id}\"></a>"
                                content += f"<p>Page {link_page_id}"
                                content += f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{inventory()}</p>"
                                content += f"<h2>{specialinfo[1]}</h2>"
                                content += f"<p>{specialinfo[3]}</p>"
                                content += f"<p>{room_actions(specialinfo[1])}</p>"

                                if(x,y) != APARTMENT: # 
                                    content += f"<p>If you want to return to {streets[y]} & {avenues[x]}, turn to <a href='#page{page_id}'>page {page_id}</a>.</p>"
                                else:
                                    content += '<p align="center">THE END</p><br /><br /><p>If you want to play again, <a href="#cover">turn back to the beginning.</a></p>'

                                content += "<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><hr>\n"
                                
                                if link_page_id == "14829": #verify, last page before endgame pages at Fifi's Apartment 
                                    content += '<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />'

                                if (x,y) == APARTMENT:
                                    content += '<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />'
                                
                                if link_page_id in page_contents:
                                    print(f"Warning: Overwriting content for page {link_page_id}.")
                                else:
                                    page_contents[link_page_id] = content



# Construct the HTML
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fifi's Big Adventure</title>
    <link href="https://fonts.googleapis.com/css2?family=Goudy+Bookletter+1911&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Goudy Bookletter 1911', serif;
            font-size: 18px;
        }
    </style>
</head>
<body>
<a name="cover"></a>
<center>
<h1>Fifi's Big Adventure</h2>
<h3>by <a href="https://savetz.com">Kay Savetz</a> and ChatGPT</h3>
<h4>for <a href="https://github.com/NaNoGenMo/2023">NaNoGenMo 2023</a></h4>
<img src="cover.png" width="60%" alt="Warm golden hour light illuminates a cityscape in an oil painting. The main focus is a person walking a standard Poodle that has a unique pink tint. The leash in the person's hand connects them to the dog. Towering buildings stand tall on both sides, and distant figures of other people provide a backdrop, with their shadows stretching on the ground."/>
</center>

<a name="preface"></a>
<p>Preface</p>

<h2>Fifi's Person's Apartment</h2>

<p>The door to the apartment opens with a familiar creak, revealing a warmly lit interior that exudes a sense of home. Plush carpeting muffles your footsteps as you step inside. Immediately, the walls grab your attention — they're adorned with framed photographs of various dogs, their playful antics frozen in time. Among them, Fifi, the mischievous poodle, features prominently, capturing moments of her chasing after a ball or cuddling up on the couch.</p>

<p>A few dog toys — a squeaky bone, a chewed-up tennis ball, and a plushie — are scattered around, hinting at Fifi's recent playtime. From the kitchen, a delicious aroma wafts towards you, hinting at a recently prepared meal. It's a comforting scent, one that mingles with the faint floral notes in the air.</p>

<p>Your thoughts are interrupted by a familiar voice. "Oh, you're here!" Fifi's person, dressed in casual attire, emerges from the adjoining room with a bright smile. Holding onto Fifi's leash, they continue, "She's been eagerly waiting for her walk. And, oh! Before I forget..." They hand you a small, crumpled ticket. "Could you pick up my dry cleaning on your way back? And perhaps buy some fresh flowers for the apartment? It would mean a lot."</p>

<p>As you nod in acknowledgment, Fifi's tail starts wagging furiously, her excitement palpable. She barks happily, clearly thrilled at the prospect of spending time with you.</p>

<p>With the leash in one hand and the dry cleaning ticket in the other, you're ready to embark on an adventure with Fifi by your side.</p>

'''


html_content += f'<a href="#page{startpage}">Start your adventure by turning to page {startpage}.</a><hr /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />'
html_content += "\n"

# add pages to HTML in order
for key in sorted(page_contents.keys()):
    html_content += page_contents[key]

html_content += "</body></html>"

# Save
pages = len(page_contents)
print(f'{pages} content pages')

max_key = max(page_contents.keys())
print(f'{max_key} highest page number')

diff = int(max_key) - int(pages)
print(f'{diff} blank pages')

with open('fifi.html', 'w') as file:
    file.write(html_content)

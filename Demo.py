import json
import pandas as pd
with open('gg2013.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)
print(df.head())


# nominees in 2013 Golden Globe Awards from imdb

List_Awards_Nominee = {"Best Motion Picture - Drama" : ['Argo', 'Django Unchained', 'Life of Pi', 'Lincoln', 'Zero Dark Thirty'],
                       "Best Motion Picture - Musical or Comedy" : ['The Best Exotic Marigold Hotel', 'Les Misérables', 'Moonrise Kingdom', 'Salmon Fishing in the Yemen', 'Silver Linings Playbook'],
                       "Best Performance by an Actor in a Motion Picture - Drama" : ['Daniel Day-Lewis', 'Richard Gere', 'John Hawkes', 'Joaquin Phoenix', 'Denzel Washington'],
                        "Best Performance by an Actor in a Motion Picture - Musical or Comedy" : ['Jack Black', 'Bradley Cooper', 'Hugh Jackman', 'Ewan McGregor', 'Bill Murray'],
                        "Best Performance by an Actress in a Motion Picture - Drama" : ['Jessica Chastain', 'Marion Cotillard', 'Helen Mirren', 'Naomi Watts', 'Rachel Weisz'],
                        "Best Performance by an Actress in a Motion Picture - Musical or Comedy" : ['Emily Blunt', 'Judi Dench', 'Jennifer Lawrence', 'Maggie Smith', 'Meryl Streep'],
                        "Best Performance by an Actor in a Supporting Role in a Motion Picture" : ['Alan Arkin', 'Leonardo DiCaprio', 'Philip Seymour Hoffman', 'Tommy Lee Jones', 'Christoph Waltz'],
                        "Best Performance by an Actress in a Supporting Role in a Motion Picture" : ['Amy Adams', 'Sally Field', 'Anne Hathaway', 'Helen Hunt', 'Nicole Kidman'],
                        "Best Director - Motion Picture" : ['Ben Affleck', 'Kathryn Bigelow', 'Ang Lee', 'Steven Spielberg', 'Quentin Tarantino'],
                        "Best Screenplay - Motion Picture" : ['Mark Boal', 'Tony Kushner', 'David O. Russell', 'Quentin Tarantino', 'Chris Terrio'],
                        "Best Original Score - Motion Picture" : ['Mychael Danna', 'Alexandre Desplat', 'Dario Marianelli', 'Tom Tykwer, Johnny Klimek, Reinhold Heil', 'John Williams'],
                        "Best Original Song - Motion Picture" : ['For You', 'Not Running Anymore', 'Safe & Sound', 'Skyfall', 'Suddenly'],
                        "Best Foreign Language Film" : ['Amour', 'A Royal Affair', 'The Intouchables', 'Kon-Tiki', 'Rust and Bone'],
                        "Best Animated Feature Film" : ['Brave', 'Frankenweenie', 'Hotel Transylvania', 'Rise of the Guardians', 'Wreck-It Ralph'],
                        "Best Television Series - Drama" : ['Breaking Bad', 'Boardwalk Empire', 'Downton Abbey', 'Homeland', 'The Newsroom'],
                        "Best Performance by an Actress in a Television Series - Drama": ['Connie Britton', 'Glenn Close', 'Claire Danes', 'Michelle Dockery', 'Julianna Margulies'],
                        "Best Performance by an Actor in a Television Series - Drama" : ['Steve Buscemi', 'Bryan Cranston', 'Jeff Daniels', 'Jon Hamm', 'Damian Lewis'],
                        "Best Television Series - Comedy or Musical": ['The Big Bang Theory', 'Episodes',"Girls","Modern Family","Smash"],
                        "Best Performance by an Actor in a Television Series - Comedy or Musical": ['Alec Baldwin', 'Don Cheadle', 'Louis C.K.', 'Matt LeBlanc', 'Jim Parsons'],
                        "Best Performance by an Actress in a Television Series - Comedy or Musical": ['Zooey Deschanel', 'Julia Louis-Dreyfus', 'Lena Dunham', 'Tina Fey', 'Amy Poehler'],
                        "Best Mini-Series or Motion Picture Made for Television": ["Game Change","Hatfields & McCoys","The Girl","The Hour","Political Animals"],
                        "Best Performance by an Actor in a Mini-Series or Motion Picture Made for Television": ["Kevin Costner","Benedict Cumberbatch","Woody Harrelson","Toby Jones","Clive Owen"],
                        "Best Performance by an Actress in a Mini-Series or Motion Picture Made for Television": ["Nicole Kidman","Jessica Lange","Sienna Miller","Julianne Moore","Sigourney Weaver"],
                        "Best Performance by an Actor in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television": ["Max Greenfield","Ed Harris","Danny Huston","Mandy Patinkin","Eric Stonestreet"],
                        "Best Performance by an Actress in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television": ["Hayden Panettiere","Archie Panjabi","Sarah Paulson","Maggie Smith","Sofía Vergara"]
                        }
# print(List_Awards_Nominee)


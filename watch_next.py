import spacy

nlp = spacy.load("en_core_web_md")

movie_file = "movies.txt"

movies_dict = {}

def read_file(filename):
    """Reads text from external file and stores it in a dictionary
    
    :param text-file filename: Text file containing movie names and their descriptions
    
    :returns: A dictionary of movie names and their descriptions
    
    :rtype: dictionary
    
    """
    
    with open(filename, "r") as f:
        for line in f:
            line_split = line.strip("\n").split(":")
            movies_dict[line_split[0]] = line_split[1]


# read movie file using read_file function
read_file(movie_file)

# create a sample sentence
sample_title = "Planet Hulk"

sample_desc = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

model_desc = nlp(sample_desc)

def next_movie(movies):
    """Returns the title of the next movie whose description similarity to sample description
    is the highest.
    
    :param dict movies: A dictionary containing movie titles and their respective descriptions
    
    :returns: Movie title
    
    :rtype: String
    
    """
    
    # create a temporary similarity value and initialize it to zero
    similarities = {}
    similarity_list = []
    
    # check each movie description and compare their similarity to the model
    for title, desc in movies.items():
        similarity = similarity_func(desc)
        similarities[similarity] = (title, desc)
    
    for key, value in similarities.items():
        similarity_list.append(key)
    
    highest = max(similarity_list)
    
    return similarities[highest][0]
        
def similarity_func(description):
    """Checks the similarity of a given description to the model description.
    
    :param text description: movie description
    
    :returns: similarity between model description and current movie description
    
    :rtype: float
    """
    desc_token = nlp(description)
    
    similarity = desc_token.similarity(model_desc)
    
    return similarity

print(f"Next Movie: {next_movie(movies_dict)}")


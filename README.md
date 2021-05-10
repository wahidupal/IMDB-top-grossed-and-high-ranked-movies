# IMDB-top-grossed-and-high-ranked-movies

There was task on Kaggle regarding IMDB top 1000 movies. I have collected the data and analyzed it according to the task. 
- The dataset contained these collumns 
- PosterLink: Link of the poster that imdb using
- SeriesTitle: Name of the movie
- ReleasedYear: Year at which that movie released
- Certificate: Certificate earned by that movie
- Runtime: Total runtime of the movie
- Genre: Genre of the movie
- IMDB Rating: Rating of the movie at IMDB site
- Overview: mini story/ summary
- Meta_score: Score earned by the movie
- Director: Name of the Director
- Star1,Star2,Star3,Star4: Name of the Stars
- No of votes: Total number of votes
- Gross: Money earned by that movie

### The task was to mention the name of the movies that are getting the good rating and also able to earn good amount of money according to different genre. 
 At first I have cleaned the data according to the task as what I considered necessary. Then I reduced the dataset in terms of vote count as in I kept only those movies that has a higher vote count than 700000. I did the same thing with IMDB rating higher than 8 and movies that grossed higher than 100000000. Afterwards I put them all into bar charts according to the movie titles

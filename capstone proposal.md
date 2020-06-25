
# WH40K Kill Team Squad Builder

This capstone project is to create a web application where someone can write and manage their WH40K Kill Team, switching between different units, sets of gear, and being able to save them to their user profile. I found that there aren't too many user-friendly applications online for this type of problem, and I think this might be a good chance to challange myself to create something that even I can use after this class.

## Functionality

The user will see the main page, containing a list of builds(Kill team squads) that other users have made. Users can log in to the page, and proceed to upvote/downvote builds they like, so they will mainly be sorted by scores from highest to lowest. The build will show a title that the auther had made, the authors name, the image representing what army is being played, comment count, and the point value.

A user can enter a build page, and see what units and gear have been selected for the squad as well as a section where they can speak about how to play by a specific strategy if there is one. The user can also see comments (sorted from most recent) and reply to them. The user can upvote/downvote on this page, as well as leave comments.

Each User will have their own profile, showing the guides they have posted and the number of comments they have made on other guides.

## Data Model

**User**
- Access to Charfield for a personal description

**Guide**
- Access to User (Author) in ForeignKey field
- Access to Army in ForeignKey field
- Access to units in ManyToMany field
- Access to gear in ManyToMany field
- Access to Charfield for Description
- Access to Integerfield for Upvotes
- Access to DateTimeField for created date

**Comment**
- Access to User (Author) in ForeignKey field
- Access to Guide in ForeignKey field
- Access to Charfield for the comment
- Access to DateTimeField for date posted

**Army**
- Access to Charfield for a name
- Access to Charfield for a brief description of the army

**Unit**
- Access to Army in ForeignKey field
- Access to Gear in ManyToMany field
- Has skill attributes for a fixed number of CharFields and IntergerFields as well as BoolFields for gear

**Gear**
- Access to Army in ForeignKey field
- Access to Unit in ManyToMany field
- Has skill attributes for a fixed number of CharFields and IntergerFields as well as BoolFields for units

## Schedule

I'll be taking on these challenges from easiest to hardest.

# Easy Difficulty

- Making a viewable homepage where a user can navigate to different guides, login, as well as view their profile.

- Easy guide making so the user can post a guide, with units the gear they have selected

- Comments so the user can input their own messages on a guide

- 2 Armies that users can make guides for, some have a pretty big number of things they can use so it will be difficult to add all of them.

# Medium Difficulty

- Making the Guide a bit more intuitive, with sections so that users can Have a more organized setup and display for the guide.

- Adding all of the armies.

# Hard Difficulty

- Adding BBcode for Comments and Guides so the user can input some icons, bold print, italicized print, and so on.

- The ability to upload images to your guide.

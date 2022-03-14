# Petstagram
Petstagram, a full-stack application inspired by Instagram, is a photo-sharing platform where pet owners can upload and share photos of their beloved pets with their friends and followers. Users can interact with posts shared by their friends by commenting, liking, and viewing them on their feed.

[Visit the site live here!](https://thepetstagram.herokuapp.com/)

* [MVP Feature List](https://github.com/jstnswn/Instagram-Clone/wiki/Feature-List)
* [User Stories](https://github.com/jstnswn/Instagram-Clone/wiki/User-Stories)
* [Database Schema](https://github.com/jstnswn/Instagram-Clone/wiki/Database-Schema)
* [Frontend Routes](https://github.com/jstnswn/Instagram-Clone/wiki/Frontend-Routes)
* [API Documentation](https://github.com/jstnswn/Instagram-Clone/wiki/API-Routes)

# Technologies Used

<img src="react-app/public/images/AWS.png" width="40" height="40"><img src="react-app/public/images/Python.png" width="40" height="40"><img src="react-app/public/images/Flask.png" width="40" height="40"><img src="react-app/public/images/React.png" width="40" height="40"><img src="react-app/public/images/Redux.png" width="40" height="40"><img src="react-app/public/images/HTML.png" width="40" height="40"><img src="react-app/public/images/CSS.png" width="40" height="40"><img src="react-app/public/images/Node.png" width="40" height="40"><img src="react-app/public/images/PostgresQL.png" width="40" height="40"><img src="react-app/public/images/SQLA.png" width="40" height="40"><img src="react-app/public/images/Javascript.png" width="40" height="40"><img src="react-app/public/images/Docker.png" width="40" height="40">

- Amazon web services
- Python
- Flask
- React
- Redux
- HTML
- CSS
- Node
- Postgres
- Sequel Alchemy
- JavaScript
- Docker
# Getting Started

1. Clone the repository

       git@github.com:jstnswn/Instagram-Clone.git

2. CD into the /app directory and install dependencies

        pipenv install

3. CD into the /react-app directory and install dependencies

        npm install

4. Create a .env file based on the example with proper settings for your development environment

5. Setup your PostgreSQL user, password and database and verify that it matches your .env file

6. Start your shell, migrate your database, seed your database, and run the flask app

        pipenv shell


        flask db upgrade


        flask seed all


        flask run

7. Create your AWS user and bucket:

      -Create a bucket:

        (https://s3.console.aws.amazon.com/s3/home?region=us-east-1)

      -Create a user with `programmatic access` by navigating to:

        (https://console.aws.amazon.com/iam/home?#/users)

      -Set up a security policy for your user: 'Attach existing policies directly' => 'Create Policy'

      -Click the `JSON tab` and set a policy:

          {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Sid": "Stmt1420751757000",
               "Effect": "Allow",
               "Action": ["s3:*"],
               "Resource": "arn:aws:s3:::<NAME OF BUCKET>/*"
             }
           ]
          }

      -Now update your .env with your `S3_BUCKET`, `S3_KEY`, `S3_SECRET`

8. Open another terminal and change directory into /react-app and run the React app

          npm start

# Features

## Splash Page
Users can log in with an existing account or sign up and create a new account. There is also a demo option so users can quickly explore the site.

<img src='react-app/public/read-me-imgs/login-form.png'></img>
 - Login/Signup form placeholders shift when filling out the form.
 - Submit button doesn't allow you to click if the form isn't complete
 - Error handling for invalid email or password.

<img src='react-app/public/read-me-imgs/login-form2.png'></img>
<img src='react-app/public/read-me-imgs/signup-form.png'></img>
<img src='react-app/public/read-me-imgs/signup-form2.png'></img>

## Navbar

Whenever a user is logged in they will be able to see the Navbar on any page. They will be able to navigate to their home feed, post an image, check notifications, or go to their profile page.

- On the navbar the user can navigate to various parts of the site.
  1. User can click on the logo or the house button to navigate to their feed.
  2. User can click here to create a post.
  3. User can click the heart to see notifications. It will be red if the user has notifications.
  4. User can click the profile image for a dropdown that allows you to navigate to their profile page or logout.

<img src='react-app/public/read-me-imgs/navbar.png'></img>

- Opening the notifications dropdown will show any new likes, follows, and comments made on users posts. When closing the notification dropdown, all notifications will be deleted.

<img src='react-app/public/read-me-imgs/notifications.png'></img>
## Dashboard

Once logged in, the dashboard presents the user with a feed of posts shared by those they follow. The user is then able to infinitely scroll down his feed and click on a post they would like to interact with. There is also a nav bar at the top of the dashboard that coveniently allows the user to create a post, go to their profile page, or log out.

- When logging in you will be greeted with dashboard feed that is filled with post from users that you are following.
- This feed will infinitely scroll until you run out of posts.

<img src='react-app/public/read-me-imgs/dashboard.png'></img>

- If you aren't following anyone your dashboard will be empty but you will see a list of suggested people to follow

<img src='react-app/public/read-me-imgs/suggested-follows.png'></img>

- On each dashboard post you can:
  1. Click the ellipsis to open a modal that has an unfollow option. If you unfollow someone their post will stay on your feed until refresh and you will be given the option to follow that person again.
  2. Click on the owner of the post to visit their profile.
  3. Click on the heart to like a post which dynamically changes the color aswell as the like count.
  4. Click the comment bubble to view all comments.
  5. The user can add a comment to the post which updates dynamically. When there are more than 2 comments the rest are hidden.

<img src='react-app/public/read-me-imgs/dashboard-post.png'></img> <img src='react-app/public/read-me-imgs/additional-comments.png'></img>

- When you click on the comment bubble or 'View all comments' it opens the postView modal where you can see all comments
  1. User can click on these ellipsis to unfollow this post's owner
  2. Here you can also leave a comment or like a post and it will update here and the feed dynamically.
  3. If you are the user that created a comment, this ellipsis will be here for you to edit or delete your comment.

<img src='react-app/public/read-me-imgs/dashboard-postview-modal.png'></img>
## Images

Clicking on the upload icon in the nav bar will open up a modal form, where the user is able to create a new post with an image of their favorite pet and caption.

Once a post is created, the user can both edit and delete their post.

- When creating a post, user can click 'Select from computer' button to choose a file from their local machine.

<img src='react-app/public/read-me-imgs/create-post.png'></img>

- User can also just drag and drop an image and it will give you a preview.

<img src='react-app/public/read-me-imgs/create-post-img.png'></img>

- When clicking next, user can then add a caption to their image before posting.

<img src='react-app/public/read-me-imgs/create-post-caption.png'></img>

- After creating a post, it will show up on your feed and you can click the ellipsis to edit or delete that post.
- If you refresh the page the post will disappear because your own posts are not part of your feed.
<img src='react-app/public/read-me-imgs/delete-edit-post.png'></img>
## Comments

Upon clicking on a post, the user is able to read/write comments as well as delete/edit their own individual comment.

## Likes

A user is able to like/dislike any image in their feed, including their own.

## Follows

On the dashboard, a user is able to unfollow any users they are currently following. On any profile page, the logged in user can click and view a list of followers/following specific to the profile page user. There, the logged in user has the option to follow or unfollow anyone on that list.


## User Profile Page

On the profile page, if it is the user's profile they can change their profile image. On any profile page, they can see the profile users followers and who the profile user is following. Here they can also view details of any post and view all of the post's comments.

<img src='react-app/public/read-me-imgs/profile-page.png'></img>

1. If the user is on his own profile page, he/she has the option to update the profile picture by clicking the profile picture. When the profile picture is clicked, it will generate a modal with options to update the profile image, but there will be more features to come in this menu.
2. The profile page also displays a grid view of all posts from that user, with the most recent posts showing at the top. When hovering over a post, the user will be able to see an overlay which will display the amount of likes and comments that post currently has.
3. In the header for the profile page, users can view how many posts this profile has, and the amount of followers and following the profile has as well. If the user clicks on followers or following, a modal will pop up which displays more detailed information such as the username, full name, and the option to follow/unfollow the other related users.

<img src='react-app/public/read-me-imgs/edit-profile-image.png'></img>
<img src='react-app/public/read-me-imgs/post-meta-data.png'></img>
<img src='react-app/public/read-me-imgs/followers.png'></img>

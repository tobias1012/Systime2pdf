# systime2pdf

This is a simple little python webscraper that turns systime IBog into a pdf

## NOTE
you can't use with without access to systime, you shouldn't use it to distribute books either, if any occurs it's the sole responisiblity of the person distributing them.

Furthermore images doesn't work and i don't intend to add them

## How to make it work?
you need to be able to log in on systime and have access to the books, then we "abuse" their cookie auth. and thereby we are able to log in to the service from the script. to do this find the two values "ekeys-userid" and "myaccount-authtoken" and add these as parameters to either the BookWriter class or as argv[3] and argv[4], argv[1] is for the filename and argv[2] is the link to the books toc

## Finding Cookies

For the userid and authtoken you have to get the cookie value for these, these can be found after logged in in developer tools in different browsers.

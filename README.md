# Post-Covid

## Instructions
1. Clone the repo
2. Create vitual environment and add it to .gitignore so that it doesn't get pushed to the repo
3. Install dependencies by the command (pip install -r requiements.txt)
4. If new dependencies are installed, freeze it into requiements.txt file

## Development Cycle
1. Set Debug = False before deployment

## Prerequisites
1. JWT Authentication
2. CORS
3. Git Large File Storage
4. HEROKU_BUILDPACK_GIT_LFS_REPO

## To Do
1. Whitelist only main webapp in CORS

## Reference Sites and Articles
https://www.tfzx.net/article/5782861.html

https://jpadilla.github.io/django-rest-framework-jwt/

https://github.com/adamchainz/django-cors-headers

https://www.pyimagesearch.com/2015/05/11/creating-a-face-detection-api-with-python-and-opencv-in-just-5-minutes/ ( Deploying ML model )

https://dev.to/iamjcoo/opencv-python-on-deploying-heroku-3lb4 ( Deploying opencv )

https://elements.heroku.com/buildpacks/bureauxlocaux/heroku-buildpack-git-lfs ( Heroku lfs buildpack setup )

## API Endpoints
^rest-auth/

^rest-auth/registration/

api-token-auth/

api/auth/

api/user-detail/

api/current-user/

token-auth/

api-token-refresh/

api-token-verify/

api/get-notification/

api/activate-reminder/

api/deactivate-reminder/

api/activate-social/

api/deactivate-social/

api/run-social/

### My Cheatsheet
python manage.py migrate --run-syncdb (After changing user model)

python manage.py collectstatic

git reset HEAD~1 ( Revert commit )

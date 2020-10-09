# Post-Covid

## Instructions
1. Clone the repo
2. Create vitual environment and add it to .gitignore so that it doesn't get pushed to the repo
3. Install dependencies by the command (pip install -r requiements.txt)
4. If new dependencies are installed, freeze it into requiements.txt file

## Development Cycle
1. Set Debug = False before deployment

## Reference Sites and Articles
https://www.tfzx.net/article/5782861.html

## API Endpoints
rest-auth/registration/

rest-auth/login/

## Common superuser
username: batch2
password: iwannab

### My Cheatsheet
python manage.py migrate --run-syncdb (After changing user model)

python manage.py collectstatic

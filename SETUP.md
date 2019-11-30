- Go to the [Heroku Deployment](https://tapsearch-ankur.herokuapp.com/)


### OR


- `git clone https://github.com/chttrjeankr/TapSearch`
- `cd TapSearch`
- `conda env create -f=./requirements.txt -n myenv`
- `gunicorn setup:app`
- Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Test it out!
    - Input text first into the database.
    - Then search for it.

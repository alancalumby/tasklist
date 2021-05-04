# tasklist
## Task list application by Flask

**2021-04-28**


Thanks to freeCodeCamp.org and jimshapedcode.com (@jimdevops19)

Here we have a very interesting tutorial that helped me to develop this app: https://www.youtube.com/watch?v=Qr4QMBUPxWo


### Necessary packages:
  - `python -m pip install email_validator`
  - `python -m pip install flask`
  - `python -m pip install flask_bcrypt`
  - `python -m pip install flask_login`
  - `python -m pip install flask_sqlalchemy`
  - `python -m pip install flask-wtf`
  - `python -m pip install wtforms`


### Features
  - Multi-user
  - Each user can only access his own tasks
  - Password encryptation
  - Cross-site request forgery protection
  - Bootstrap
  - Three status availables for each task (NotStarted, InProgress and Done)
    - It allows only the following status flow: NotStarted > InProgress > Done
  - Tasks deleting

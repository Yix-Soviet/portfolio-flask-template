from databases.conf_db import db, BaseDBModel

# class ProjectsModel(db.Model, BaseDBModel):
#     id = db.Column(db.Integer, primary_key=True)
#     repo_name = db.Column(db.String(), nullable=False)
#     repo_owner = db.Column(db.String(), nullable=False)
#     repo_url = db.Column(db.String(), nullable=False)
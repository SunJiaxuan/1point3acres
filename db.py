from mongoengine import *

connect('1point3acres')

class UserProfile(Document):
    leave_time=StringField()
    wanna_diploma=StringField()
    result=StringField()
    wanna_subject=StringField()
    wanna_university=StringField()
    undergraduate_subject=StringField()
    undergraduate_university=StringField()
    undergraduate_GPA=StringField()
    ms_subject=StringField()
    ms_university=StringField()
    ms_GPA=StringField()
    toefl=StringField()
    GRE=StringField()
    something=StringField()
    Source=StringField()

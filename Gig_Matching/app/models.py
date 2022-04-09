"""
Definition of models.
"""

from django.db import models

class Skill(models.Model):
    SkillID = models.AutoField(primary_key=True)
    SkillName = models.CharField(max_length = 200)
    SkillAttributs = models.CharField(max_length = 1000)

    def __str__(self):
        return str(self.SkillID)

class ProjectType(models.Model):
    ProjectTypeID = models.AutoField(primary_key=True)
    ProjectTypeName = models.CharField(max_length = 100, null = True)
    SkillID = models.ManyToManyField(Skill) # Keeps list of skills for each project type

    def __str__(self):
        return str(self.ProjectTypeID)

class Account(models.Model):
    AccountID = models.AutoField(primary_key=True)
    SkillID = models.ManyToManyField(Skill) # Keeps list of skills held by account
    AccountPhoto = models.CharField(max_length = 500)
    Name = models.CharField(max_length = 100)
    

class Project(models.Model):
    ProjectID = models.AutoField(primary_key=True)
    ProjectTypeID = models.ForeignKey(ProjectType, on_delete= models.SET_NULL, null= True) # Change from char name in form inputs to getting list of ProjectTypeName to select from, each linked with appropriate ProjectTypeID
    ProjectManagerID = models.IntegerField(default=0)
    ProjectName = models.CharField(max_length = 200)
    ProjectDesc = models.CharField(max_length = 1000)
    AccountID = models.ManyToManyField(Account)

    def __str__(self):
        return self.ProjectName

class ProjectManager(models.Model):
    ProjectManagerID = models.AutoField(primary_key=True)
    AccountID = models.ForeignKey(Account, on_delete= models.SET_NULL, null= True)


# Create your models here.



import requests
import pandas as pd
import json
import configparser
import pyodbc
from emailForward import SuccessEmail
from DOBDataAccess import DOBDataAccess
# Getting data from this url and storing it in dobjobs (converting json to text)
# dobjobs is a type list
class Dataload:
    def __init__(self, url):
        self.url = url

    def download(self):
        #url = "https://data.cityofnewyork.us/resource/rvhx-8trz.json?job_type=PA"
        self.resp = requests.get(self.url)
        self.dobjobs = json.loads(self.resp.text)


# taking a few titles from the dobjobs and storing it in list where each element is a dict.
    def createList(self):
        self.li = []
        for i in range(len(self.dobjobs)):
            jobs_dict = {}
            try:
                jobs_dict['Bin'] = self.dobjobs[i]['bin__']
            except:
                jobs_dict['Bin'] = None
            try:
                jobs_dict['Borough'] = self.dobjobs[i]['borough']
            except:
                jobs_dict['Borough'] = None
            try:
                jobs_dict['Latitude'] = self.dobjobs[i]["gis_latitude"]
            except:
                jobs_dict['Latitude'] = None
            try:
                jobs_dict['Longitude'] = self.dobjobs[i]['gis_longitude']
            except:
                jobs_dict['Longitude'] = None
            try:
                jobs_dict['Building Class'] = self.dobjobs[i]['building_class']
            except:
                jobs_dict['Building Class'] = None
            try:
                jobs_dict['Job Status Decsription'] = self.dobjobs[i]["job_status_descrp"]
            except:
                jobs_dict['Job Status Decsription'] = None

            self.li.append(jobs_dict)


# Creating a dataframe out of the list created above
    def createDataframe(self):
        self.df = pd.DataFrame(self.li)


# Making a connection with SQL
# Storing the data from dataframe into already created table in SQL
    def transferToSql(self):
        objdataAccess=DOBDataAccess()
        objdataAccess.SaveData(self.df)

    def ProcessDownload(self):

        nyjobs.download()
        print("Data Downloaded")

        nyjobs.createList()
        print("List created")

        nyjobs.createDataframe()
        print("Dataframe created")

        nyjobs.transferToSql()
        print("Data tranfered to SQL database")

        #successemail = SuccessEmail("xxx@gmail.com", "xx@gmail.com")
        #successemail.sendEmail("Downloaded sucess", 'NYC DOb Data')

try:
    parser = configparser.ConfigParser()
    parser.read("config.txt")

    nyjobs = Dataload(parser.get("config", "DOB_URL"))
    nyjobs.ProcessDownload()


except Exception as e:
    print(e)




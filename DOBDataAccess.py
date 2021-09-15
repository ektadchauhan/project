
import pyodbc

# Getting data from this url and storing it in dobjobs (converting json to text)
# dobjobs is a type list
class DOBDataAccess:


    def SaveData(self,df):
        coxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server}; SERVER=EKTA\EKTASQLEXPRESS; DATABASE=TestStore; Trusted_Connection=yes;')
        cur = coxn.cursor()
        for index, row in df.iterrows():
            cur.execute("INSERT INTO dbo.DobJobs VALUES (?,?,?,?,?,?)", row['Bin'], row['Borough'], row['Latitude'],
                        row['Longitude'], row['Building Class'], row['Job Status Decsription'])
            coxn.commit()
        coxn.close()

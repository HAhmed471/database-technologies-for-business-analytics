import pyodbc 

server = 'tcp:mcruebs04.isad.isadroot.ex.ac.uk' 
database = 'BEM2040_HAHMED'
username = 'HAhmed' 
password = 'JzrL842*Qz'


cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password+';TrustServerCertificate=yes;Encrypt=no;')

cursor = cnxn.cursor()

#Select Query
print ('Reading data from table')
tsql = "SELECT * FROM Energy_consumption;"
with cursor.execute(tsql):
    row = cursor.fetchone()
    while row:
        print (str(row[0]) + " " + str(row[1]))
        row = cursor.fetchone()

#CRUD Functions for Energy_consumption

#Read the table
cursor.execute('SELECT * FROM Energy_Consumption')
row = cursor.fetchall()
for row in row:
    print(row.customer_id, row.consumption_id, row.source_id, row.units)

# Update the table
cursor.execute("UPDATE Energy_Consumption set consumption_id= 'AS' WHERE units= '6'")
cnxn.commit()
print('completed')

#Create new values for table
Energy_Consumption1= (240, 'king1', 'EG', 'agyad multi')
cursor.execute('INSERT INTO Energy_Consumption(units, customer_id, consumption_id, source_id) VALUES (?,?,?,?)', Energy_Consumption1) 
cnxn.commit()
print('created')

# Delete values that were created 
cursor.execute("DELETE FROM Energy_Consumption WHERE customer_id= 'king1'")
cnxn.commit()
print (cursor.rowcount, 'VALUE DELETED') 



# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import sqlite3


# THESE CODES ARE for creating the dataframe and then merging them
#energy_consumption_df = pd.read_sql_query("SELECT * FROM Energy_Consumption", conn)
#customers_df = pd.read_sql_query("SELECT * FROM Customers", conn)
#merged_df = pd.merge(energy_consumption_df, customers_df, on='customer_id')


# THIS IS FOR analysing the total energy consumption by geneder
#energy_by_gender = merged_df.groupby('gender')['units'].sum().reset_index()
#sns.barplot(data=energy_by_gender, x='gender', y='units')
#plt.xlabel('Gender')
#plt.ylabel('Total Energy Consumption')
#plt.title('Energy Consumption by Gender')
#plt.show()

#THIS IS FOR analysing the average consumption per source_ID
#avg_energy_by_source = merged_df.groupby('source_id')['units'].mean().reset_index()
#sns.barplot(data=avg_energy_by_source, x='source_id', y='units')
#plt.xlabel('Source ID')
#plt.ylabel('Average Energy Consumption')
#plt.title('Average Energy Consumption per Source')
#plt.show()


# THIS IS FOR ANALYSING energy consumption distribution
#sns.histplot(data=merged_df, x='units', kde=True)
#plt.xlabel('Energy Consumption')
#plt.ylabel('Frequency')
#plt.title('Energy Consumption Distribution')
#plt.show()
















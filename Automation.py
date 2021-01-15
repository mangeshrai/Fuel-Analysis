import shutil
import os
import pandas as pd
from openpyxl import load_workbook
import schedule
import time

def job():
    #get list of all processed files in the past
    processed_files = [file for file in os.listdir('./Processed') if file.endswith('.csv')]
    processed_path=os.path.join(os.getcwd(),'./Processed',''.join(processed_files))

    #check if any new files have appeared in drop folder
    dropped_files=[file for file in os.listdir('./Drop') if file.endswith('csv')]
    drop_path=os.path.join(os.getcwd(),'./Drop',''.join(dropped_files))

    #if there is a new file then load into a dataframe and prepare to write
    if dropped_files:
        df=pd.read_excel(dropped_files)

        #find the current number of entries in the main file
        dfmain=pd.read_csv('./main/main.csv')
        currentrows=dfmain.shape[0]

        #load into main workbook
        workbook_name='./main/main.csv'
        wb=load_workbook(workbook_name)
        page=wb['sheet1']

        #write new entries into main workbook
        newentry=df.values.tolist()
        for i in newentry:
            page.append(i)
            wb.save(filename=workbook_name)
df_main_new=pd.read_csv('./main/main.csv')
newrows=df_main_new.shape[0]


schedule.every().day.at("16:43").do(job)

while True:
    schedule.run_pending()
    time.sleep(1) #wait one minute



from rest_framework.response import Response
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.firefox.options import Options
from rest_framework import viewsets
from rest_framework.response import Response
import numpy as np
from workadays import workdays as wd
from .models import OptionItem
import datetime
from .serializers import OptionItemSerializer


class UpdateDataView(viewsets.ModelViewSet):
    queryset = OptionItem.objects.all()
    serializer_class = OptionItemSerializer
    
    def list(self, request):
        brazil_holidays = wd.get_holidays(country='BR', state='SP', years=range(2023, 2024))
        

        today = datetime.date.today()

        last_workday = today

        while True:

            if last_workday.weekday() < 5 and last_workday not in brazil_holidays:
                break
            else:
                last_workday -= datetime.timedelta(days=1)

        
        last_workday = last_workday.strftime('%Y-%m-%d')

        geckodriver_path = r'C:\Users\sique\Documents\geckodriver.exe'

        
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(executable_path=geckodriver_path, options=options)
        
        driver.get(f'https://arquivos.b3.com.br/tabelas/InstrumentsConsolidated/{last_workday}')

        

        
        wait = WebDriverWait(driver, 10)
        next_button = wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()="»"]')))
        df_general_info = pd.DataFrame()
        comprimento = 0
        while ((next_button.is_enabled()) & (comprimento<200)):
            
            wait = WebDriverWait(driver, 10)
            table = wait.until(EC.presence_of_element_located((By.XPATH, '//table[@class="responsive"]')))
            df = pd.read_html(table.get_attribute('outerHTML'))[0]
            df = df[df['Market Name']=='EQUITY-DERIVATE']
            df = df[['Date','Symbol','Segment','Underlying','Expiration Date','Exercise Price']]
            df.dropna(inplace=True)
            df_general_info = pd.concat([df_general_info, df], ignore_index=True)
            
            comprimento = len(df_general_info)
            
            next_button.click()

        
        
        OptionItem.objects.all().delete()
        
        for index, row in df_general_info.iterrows():
            item = OptionItem(
                date_insertion=pd.to_datetime(row[0]),
                option_code=row[1],
                option_type=row[2],
                underlying_asset=row[3],
                expiration_date=pd.to_datetime(row[4]),
                strike_price=float(row[5]),
            )
            item.save()
        
        
        driver.quit()

   
        
        return Response(status=200)


class ShowDataView(viewsets.ModelViewSet):
    queryset = OptionItem.objects.all()
    serializer_class = OptionItemSerializer

    
# %%
"""
2. Írj egy osztályt a következő feladatokra:  
2.1 Neve legyen NJCleaner és mentsd el a NJCleaner.py-ba. Ebben a fájlban csak ez az osztály legyen.
2.2 Konsturktorban kapja meg a csv elérési útvonalát és olvassa be pandas segítségével és mentsük el a data (self.data) osztályszintű változóba 
2.3 Írj egy függvényt ami sorbarendezi a dataframe-et 'scheduled_time' szerint növekvőbe és visszatér a sorbarendezett df-el, a függvény neve legyen 'order_by_scheduled_time' és térjen vissza a df-el  
2.4 Dobjuk el a from és a to oszlopokat, illetve azokat a sorokat ahol van nan és adjuk vissza a df-et. A függvény neve legyen 'drop_columns_and_nan' és térjen vissza a df-el  
2.5 A date-et alakítsd át napokra, pl.: 2018-03-01 --> Thursday, ennek az oszlopnak legyen neve a 'day'. Ezután dobd el a 'date' oszlopot és térjen vissza a df-el. A függvény neve legyen 'convert_date_to_day' és térjen vissza a df-el   
2.6 Hozz létre egy új oszlopot 'part_of_the_day' névvel. A 'scheduled_time' oszlopból számítsd ki az alábbi értékeit. A 'scheduled_time'-ot dobd el. A függvény neve legyen 'convert_scheduled_time_to_part_of_the_day' és térjen vissza a df-el  
    4:00-7:59 -- early_morning  
    8:00-11:59 -- morning  
    12:00-15:59 -- afternoon  
    16:00-19:59 -- evening  
    20:00-23:59 -- night  
    0:00-3:59 -- late_night  
2.7 A késéseket jelöld az alábbiak szerint. Az új osztlop neve legyen 'delay'. A függvény neve legyen pedig 'convert_delay' és térjen vissza a df-el
        0min <= x < 5min   --> 0  
        5min <= x          --> 1  
2.8 Dobd el a felesleges oszlopokat 'train_id' 'actual_time' 'delay_minutes'. A függvény neve legyen 'drop_unnecessary_columns' és térjen vissza a df-el
2.9 Írj egy olyan metódust, ami elmenti a dataframe első 60 000 sorát. A függvénynek egy string paramétere legyen, az pedig az, hogy hova mentse el a csv-t (pl.: 'data/NJ.csv'). A függvény neve legyen 'save_first_60k'. 
2.10 Írj egy függvényt ami a fenti függvényeket összefogja és megvalósítja (sorbarendezés --> drop_columns_and_nan --> ... --> save_first_60k), a függvény neve legyen 'prep_df'. Egy paramnétert várjon, az pedig a csv-nek a mentési útvonala legyen. Ha default value-ja legyen 'data/NJ.csv'
"""

# %%
import pandas as pd


# %%
class NJCleaner:

    def __init__(self,path):
        self.data = pd.read_csv(path)

    def order_by_scheduled_time(self):
        self.data = self.data.sort_values(by=['scheduled_time'])
        return self.data
    
    def drop_columns_and_nan(self):
        self.data = self.data.drop(['from', 'to'], axis=1)
        self.data = self.data.dropna()
        return self.data
    
    def convert_date_to_day(self):
        self.data['date'] = pd.to_datetime(self.data['date'])
        self.data['day'] = self.data['date'].dt.day_name()
        self.data = self.data.drop(['date'], axis=1)
        return self.data
    
    def convert_scheduled_time_to_part_of_the_day(self):
        df = pd.DatetimeIndex(self.data['scheduled_time']).hour
        self.data['part_of_the_day'] = pd.cut(df, bins=[-1, 3, 7, 11, 15, 19, 24], 
                                              labels=[ 'late_night', 'early_morning', 'morning', 'afternoon', 'evening', 'night']) 
        self.data.drop(columns=['scheduled_time'], inplace=True) 
        return self.data

    def convert_delay(self):
        max = self.data['delay_minutes'].astype('float').max()
        self.data['delay'] = pd.cut(self.data['delay_minutes'].astype('float'), bins=[-1, 4.999, max], labels=[0, 1])
        return self.data

    
    def drop_unnecessary_columns(self):
        self.data.drop(['train_id', 'actual_time', 'delay_minutes'], axis=1, inplace=True)
        return self.data
    
    def save_first_60k(self, path):
        cutted_df = self.data.head(60000)
        cutted_df.to_csv(path, index=False)

    def prep_df(self, path='data/NJ.csv'):
        self.order_by_scheduled_time()
        self.drop_columns_and_nan()
        self.convert_date_to_day()
        self.convert_scheduled_time_to_part_of_the_day()
        self.convert_delay()
        self.drop_unnecessary_columns()
        self.save_first_60k(path)
    

# %%
#nj = NJCleaner("data/2018_03.csv")

#nj.prep_df()



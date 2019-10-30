import pandas as pd     # tbd: what's wrong here
import numpy as np
import sys

def create_csv_from_dat_file():
    column_names = [
                ('caseid',       1,  12),    # eindeutige Fallkennung
                ('nbrnaliv',    22,  22),    # Gesamtanzahl Lebendgeburten
                ('babysex',     56,  56),    # Geschlecht des Kindes
                ('birthwgt_lb', 57,  58),    # Geburtsgewicht (lbs)
                ('birthwgt_oz', 59,  60),    # Geburtsgewicht (oz)
                ('prglength',  275, 276),    # Schwangerschaftsdauer (Wochen)
                ('outcome',    277, 277),    # Ausgang (1 = Lebendgeburt)
                ('birthord',   278, 279),    # Index in der Geburtsfolge
                ('agepreg',    284, 287),    # Alter bei Schwangerschaftsende
                ('finalwgt',   423, 440),    # Gewicht (bereinigt)
                ]
    column_names_names = list(zip(*column_names))[0]
    preg_names_df = pd.DataFrame.from_records(column_names,columns=['name','start','end'],index=column_names_names)
    #print(preg_names_df.loc['agepreg'])

    #sys.exit()
    preg_dict = dict.fromkeys(preg_names_df.name)


    #preg_df = pd.DataFrame(columns=preg_names_df['name'])

    preg_file = r'C:\Users\Bastorizzel\Desktop\Statistik Workshop\Statistik-Workshop-Codebeispiele\2002FemPreg.dat\2002FemPreg.dat'

    linecount = 1
    preg_file_txt = open(preg_file, "r")

    for line in preg_file_txt:
        for field in preg_names_df.name:
            if linecount == 1:
                preg_dict[field] = [line[((preg_names_df.loc[field][1])-1):preg_names_df.loc[field][2]].strip()]
            else:
                #print(field,preg_dict[field])
                preg_dict[field].append(line[((preg_names_df.loc[field][1])-1):preg_names_df.loc[field][2]].strip())
        linecount = 0

    preg_df = pd.DataFrame(preg_dict)
    print(preg_df.info())

    preg_file_txt.close()

    preg_df.to_csv('2002FemPreg.csv')

preg_df = pd.read_csv('2002FemPreg.csv')
preg_df = preg_df.drop(preg_df.columns[0],axis=1)
pd.set_option('display.max_columns', None)

print(preg_df.head())
ex_1_3_1 = len(preg_df)
print(ex_1_3_1)

ex_1_3_2 = sum(preg_df.outcome == 1)
print(ex_1_3_2)

ex_1_3_3 = [sum(preg_df.birthord == 1), sum(preg_df.birthord > 1)]
print('First borns: ',ex_1_3_3[0])
print('not first borns: ',ex_1_3_3[1])

ex_1_3_4 = [np.mean(preg_df.prglength[preg_df.birthord == 1]), np.mean(preg_df.prglength[preg_df.birthord > 1])]
print('Average duration pregnancy first borns: ',ex_1_3_4[0])
print('Average duration pregnancy not-first borns: ',ex_1_3_4[1])
print('Difference in days: ',ex_1_3_4[0]*7 - ex_1_3_4[1]*7)
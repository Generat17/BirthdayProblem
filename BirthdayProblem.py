import vk_api
import time
import random
import csv
import pandas as pd

# токен
# узнать можно тут - https://vkhost.github.io/
token = 'Вставьте сюда Ваш токен'

# id группы
group_id = 'sokoloff_show'

id = 1

with open('vk_data.csv', 'w') as new_file:
                # csv
                fieldnames = ['id','id_vk', 'bdate', 'bmonth', 'byear']

                csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')

                csv_writer.writeheader()

                newDict = dict()
                vk_session = vk_api.VkApi(token=token)
                vk = vk_session.get_api()
                
                for i in range(0, 20):
                    vk_group = vk.groups.getMembers(group_id = group_id, offset = 1000 * i,  fields = 'bdate')
                    for k in range(0, 1000):
                        try:
                            new_file.write(str(id) + ',' + str(vk_group['items'][k]["id"]) + ',' + str(vk_group['items'][k]["bdate"]).replace('.', ','))
                            new_file.write('\n')
                            id += 1
                        except:
                            pass

counter = 0
df = pd.read_csv('vk_data.csv', index_col=0)
df['d_and_m'] = df['bdate'] + (df['bmonth']*30)
print(df)

fifty = df["d_and_m"].sample(n = 23)
for i in range(0, 1000):
    fifty = df["d_and_m"].sample(n = 23)
    for j in fifty.duplicated():
        if j == True:
            counter = counter + 1
            break
print('Вероятность:', counter / 1000)
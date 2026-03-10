# import pandas as pd
# from faker import Faker
# import random

# fake=Faker('en_IN')

# data=[]

# for i in range(500):
#     data.append({
#                 "student_id_no": i+1,
#                 "student_name": fake.name(),
#                 "father_name":fake.first_name_male(),
#                 "mother_name":fake.first_name_female(),
#                 "class":random.randint(1,12),
#                 "section":random.choice(["A","B","C"])
    
#     })
# df=pd.DataFrame(data)
# print(df)

# df.to_csv("students_data.csv", index=False)
#################################################################################
import pandas as pd
from faker import Faker
import random

fake=Faker('en_IN')

data=[]

for i in range(500):
    data.append({
                "student_id_no": i+1,
                "couses_name": fake.name(),
                "python":random.randint(30,99),
                "sql":random.randint(30,99),
                "c":random.randint(30,99),
                "c++":random.randint(30,99),
                "html_css":random.randint(30,99),
                "java":random.randint(30,99)              
    
    })
df=pd.DataFrame(data)
print(df)

df.to_csv("courses_data.csv", index=False)


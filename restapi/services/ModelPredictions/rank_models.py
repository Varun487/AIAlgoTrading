import os
import pandas as pd

# print(os.listdir("./Storage/Models"))

df = pd.DataFrame(columns=['company', 'model', 'nrmse'])

companies = []
models = []
nrmses = []

for company in os.listdir("./Storage/Models"):
    # print(company, os.listdir(f"./Storage/Models/{company}/"))
    company_models = os.listdir(f"./Storage/Models/{company}/")
    companies.extend([company for i in range(5)])
    # print(company)
    for model in company_models:
        models.append(model)
        # print(model.split('_')[7].split(':')[1])
        nrmses.append(float(model.split('_')[7].split(':')[1]))

# print(len(models))
# print(len(companies))
# print(len(nrmses))
#
# print(sorted(nrmses))

df['company'] = companies
df['model'] = models
df['nrmse'] = nrmses

print(df)

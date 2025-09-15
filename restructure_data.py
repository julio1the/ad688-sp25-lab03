import pandas as pd

# load dataset
data = pd.read_csv('lightcast_data.csv', low_memory=False)

# 1) Job_Postings
job_postings = data[['ID','TITLE_RAW','TITLE_CLEAN','POSTED','EXPIRED',
    'SALARY_FROM','SALARY_TO','MIN_YEARS_EXPERIENCE','MAX_YEARS_EXPERIENCE',
    'SKILLS','SPECIALIZED_SKILLS','SOFTWARE_SKILLS','EMPLOYMENT_TYPE','COMPANY']]
job_postings.to_csv('_output/job_postings.csv', index=False)

# 2) Company
company = data[['COMPANY','COMPANY_NAME','COMPANY_RAW','COMPANY_IS_STAFFING']].drop_duplicates()
company.to_csv('_output/company.csv', index=False)

# 3) Job_Location
job_location = data[['ID','CITY','STATE','COUNTY','LOCATION']]
job_location.to_csv('_output/job_location.csv', index=False)

# 4) SOC_Details
soc = data[['ID','SOC_2','SOC_2_NAME','SOC_3','SOC_3_NAME',
            'SOC_4','SOC_4_NAME','SOC_5','SOC_5_NAME']]
soc.to_csv('_output/soc_details.csv', index=False)

# 5) LOT_Details
lot = data[['ID','LOT_CAREER_AREA','LOT_CAREER_AREA_NAME','LOT_OCCUPATION',
            'LOT_OCCUPATION_NAME','LOT_SPECIALIZED_OCCUPATION','LOT_SPECIALIZED_OCCUPATION_NAME']]
lot.to_csv('_output/lot_details.csv', index=False)

# 6) NAICS_Details
naics = data[['ID','NAICS2','NAICS2_NAME','NAICS3','NAICS3_NAME','NAICS4',
              'NAICS4_NAME','NAICS5','NAICS5_NAME','NAICS6','NAICS6_NAME']]
naics.to_csv('_output/naics_details.csv', index=False)

print("✅ Listo: CSVs creados en _output/")



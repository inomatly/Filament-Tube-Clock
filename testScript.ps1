$get_date = Get-Date -Format "yyyyMMddhhmmssss"
python -m pytest --html=reports/report_$get_date.html --junitxml=reports/report_$get_date.xml --cov=./ --cov-branch --cov-report html:reports/cov.html
python .\analysis.py
python .\analysis_cov.py
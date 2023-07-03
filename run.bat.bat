pytest -v -s  -m "sanity" --html=Reports\report1.htmltestCases/ --browser chrome
@REM pytest -v -s  -m "regression" --html=Reports\report1.html testCases/ --browser chrome
@REM pytest -v -s  -m "sanity or regression" --html=Reports\report1.html testCases/ --browser chrome
@REM pytest -v -s  -m "sanity and regrassion" --html=Reports\report1.html testCases/ --browser chrome

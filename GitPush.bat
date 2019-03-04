git add *
set /p name="ENTER COMMIT NAME: "
git commit -m "%name%"
git push origin master
@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  start "" http://localhost:8000
  py -m http.server 8000
) else (
  start "" index.html
  echo Python was not found, so the site was opened directly.
  echo Browser location access may require local hosting.
  pause
)

@echo off
cd /d "%~dp0"  :: Changes directory to where the batch file is

:: Add new and changed files
git add .

git commit -m "Auto-commit"

:: Push to origin
git push origin main

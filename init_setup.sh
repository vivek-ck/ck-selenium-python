# Create a Python virtual environment for Selenium
python3 -m venv __dependencies__

# Activate the virtual environment
source __dependencies__/bin/activate

# Install SeleniumBase package within the virtual environment
pip install seleniumbase allure-behave

#Info
echo "#### Activate the virtual environment: source selenium_env/bin/activate ####"
echo "#### To deactivate use : deactivate ####"

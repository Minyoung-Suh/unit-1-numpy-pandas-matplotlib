Make sure pip is at least version 24.2

`python -m pip install --upgrade pip`


Install the requirements using:
`python -m venv .unit-1-env`

Windows: `./.unit-1-env/scripts/activate`
Mac: `source .\.unit-1-env\bin\activate`
Linux: `source .\.unit-1-env\bin\activate`

`python -m pip install -r ./requirements.txt`

It is recommended to create an environment for your packages.

Select your environment for your kernel, do this by:
1. Opening the below .ipynb file
2. Run the first python block
3. Select "Python Environment"
4. Select the .unit-1-env environment

The order in which you should read this unit is:
1. numpy-is-fast.ipynb
2. pandas-is-organized.ipynb
3. matplotlib-is-beautiful.ipynb
4. matplotlib-plot.py for a plt.show example


Troubleshooting
1. If the plots appear as white bars, then restart vscode to see if it helps
2. If the line %matplotlib ipympl causes issues, your pip may be out of date and needs to be upgraded
    - Its also possible your pip being upgraded is not on path, so its using an outdated pip
    - In your env uninstall each package with `python3 -m pip uninstall -r ./requirements.txt`
    - Upgrade pip with `python -m pip install --upgrade pip`
    - Then reinstall the packages with ``python3 -m pip install -r ./requirements.txt`
3. If you get the error `WARNING: Failed to activate VS environment: Could not find C:\Program Files (x86)\Microsoft Visual Studio\Installer\vswhere.exe`, please install Microsoft Visual Studios (this is different than VS Code) at https://visualstudio.microsoft.com/
     - This downloads some c++ tools that are used to install pip packages. 
     - Make sure you click the "Desktop Development with C++" box, then hit install.
     - Once installed you do not need to sign in
     - You may need to restart your computer for this to take effect. (my system did not seem to need it)
  
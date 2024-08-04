Make sure pip is at least version 24.2

`python -m pip install --upgrade pip`


Install the requirements using:
`python3 -m venv .unit-1-env`

`./.unit-1-env/scripts/activate`

`python3 -m pip install -r ./requirements.txt`

It is recommended to create an environment for your packages.

Select your environment for your kernel.


The order in which you should read this unit is:
1. numpy-is-fast.ipynb
2. pandas-is-organized.ipynb
3. matplotlib-is-beautiful.ipynb
4. matplotlib-plot.py for a plt.show example


Troubleshooting
- If the plots appear as white bars, then restart vscode to see if it helps
- If the line %matplotlib ipympl causes issues, your pip may be out of date and needs to be upgraded
    - Its also possible your pip being upgraded is not on path, so its using an outdated pip
    - In your env uninstall each package with `python3 -m pip uninstall -r ./requirements.txt`
    - Upgrade pip with `python -m pip install --upgrade pip`
    - Then reinstall the packages with ``python3 -m pip install -r ./requirements.txt`
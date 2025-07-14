# ns-login
python script to autologin nations with github actions workflow file. `nation,password` format and multiple nation lists are supported.

***note that all files in the `/nations` directory will be included in the autologin***

## Usage (github actions)

login.yml has been configured to run every Monday and Thursday at 1 am UTC by default

1. [fork the repository](https://github.com/ducky4life/ns-login/fork) or copy `https://github.com/ducky4life/ns-login.git` and [import it to a private repository](https://github.com/new/import) to avoid leaking passwords in plaintext if using `nation,password` format
2. create new github actions repository secret named PASSWORD with your switcher password by going to
   ```
   https://github.com/[github username]/[repo name]/settings/secrets/actions
   ```
3. enter your main nation as useragent in login.py
4. make one or more lists of switchers with a password optionally in `/nations` folder
(default password in secrets will be overridden for a single switcher if a row is in `nation,password` format)
5. run login.yml by going to
   ```
   https://github.com/[github username]/[repo name]/actions/workflows/login.yml
   ```

## Usage (locally)

make sure you have [python](https://www.python.org/downloads/) installed.

1. clone the repository
   ```
   git clone https://github.com/ducky4life/ns-login.git
   ```
2. move into directory
   ```
   cd ns-login
   ```
3. install dependencies
   ```
   pip install -r requirements.txt
   ```
4. create .env file
   ```
   touch .env
   ```
5. put your secrets in the .env file
   ```
   PASSWORD=[your puppet password]
   ```
6. enter your main nation as useragent in login.py
7. make one or more lists of switchers with a password optionally in `/nations` folder
(default password in secrets will be overridden for a single switcher if a row is in `nation,password` format)
8. create input.csv
   ```
   touch input.csv
   ```
9. fill input.csv (all files inside `/nations` folder will be compiled into input.csv, you can also fill input.csv manually)
   ```
   cat ./nations/* > input.csv
   ```
10. run login.py
      ```
      python login.py
      ```

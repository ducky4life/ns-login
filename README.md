# ns-login
python script to autologin nations with github actions workflow file. `nation,password` format is supported.

## Usage (github actions)

1. [fork the repository](https://github.com/ducky4life/ns-login/fork) or [import it to a private repository](https://github.com/new/import) to avoid leaking passwords in plaintext if using `nation,password` format
2. create new action repository secret named PASSWORD with your switcher password by going to
   ```
   https://github.com/[github username]/[repo name]/settings/secrets/actions
   ```
4. edit input.csv and include a list of switchers with a password optionally (default password in secrets will be overridden for a single switcher if a row is in `nation,password` format)
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
2. install dependencies
   ```
   pip install -r requirements.txt
   ```
3. create .env file
   ```
   touch .env
   ```
4. put your secrets in the .env file
   ```
   PASSWORD=[your puppet password]
   ```
5. edit input.csv and include a list of switchers with a password optionally (default password in secrets will be overridden for a single switcher if a row is in `nation,password` format)
6. run login.py
   ```
   py login.py
   ```

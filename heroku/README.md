# Deploying Regression app with Flask to Heroku from Ubuntu 16.04


* Make sure you have Docker installed
* This app is created in virtual environment pyenv. Python and Flask is installed with 
  command 
   * ```pip install python 2.7.13 or 3.6.14``` depending on your preference.
   * ```pip install flask```
   
* Install Heroku Commandliine Interface https://devcenter.heroku.com/articles/heroku-cli
  -For ubuntu 16.04
   ```sh
   $ curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
   
   ``` 
* Authenticate to heroku by 
  
   ```sh
   $ heroku login 
   ```
   
* Log in to Container Registry for Docker deployment
   
   ```sh
   $ heroku container:login
   ```
   
 * Fetch code from Git repo
 
   ```sh
   $ git clone https://github.com/cloudmesh-community/hid-sp18-415/blob/master/project-code/heroku
 
   ```
 * Go to app directory and run following command. A git repository with the application
   will be created and a name will be asigned to the app. 
 
   ```sh
   $ heroku create
   ```
* Now following command will build the image and push it to Container Registry. It
  takes quite some time to build and push image. 
  
   ```sh
   $ heroku container:push web --app appname
   ```
* Once it is done it is time to open app by following command

   ```sh
   $ heroku open --app appname
   ```
* This will open app in herokuapp.com
  Right now it runs in the folowing link
  
         https://afternoon-brushlands-41642.herokuapp.com/currentDetails

      *** These steps are referred from heroku documentation
           https://devcenter.heroku.com/articles/container-registry-and-runtime

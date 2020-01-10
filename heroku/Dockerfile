From heroku/miniconda

# Grab requirements.txt
ADD ./regapp/requirements.txt /tmp/requirements.txt

#Install dependencies
RUN pip install -qr /tmp/requirements.txt

#add code
ADD ./regapp /opt/regapp/
WORKDIR /opt/regapp

RUN conda install pandas scikit-learn


CMD gunicorn -w 4 -b 0.0.0.0:$PORT regressionAPI:app 

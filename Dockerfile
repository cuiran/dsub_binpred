FROM google/cloud-sdk:slim

RUN git clone https://github.com/cuiran/FI_priors.git /home/pyscripts/
RUN chmod 777 -R /home/pyscripts/

COPY requirements.txt /home/

RUN pip install -r /home/requirements.txt

VOLUME ["/root/.config"]
CMD [ "/bin/bash" ]

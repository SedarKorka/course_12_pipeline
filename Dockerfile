#FROM brodriguesco/r_4.2.2:main-b1950d55ccbd8009de4ee2006a097c3e7ef1c529

#FROM python:latest

#RUN mkdir /home/housing

#RUN mkdir /home/housing/pipeline_output

#RUN mkdir /home/housing/shared_folder
 
#COPY my_script.py /home/housing/my_script.py

#COPY requirements.txt /home/housing/requirements.txt  

#CMD ["my_script.py", "-flag"]

#CMD mv /home/housing/pipeline_output/* /home/housing/shared_folder/

FROM python:3.10.12

WORKDIR /home/housing

COPY requirements.txt /home/housing/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY my_script.py /home/housing/my_script.py

# Set environment variables 
ENV FACEBOOK_URL="https://raw.githubusercontent.com/wang422003/Complex-Networks_exercise/main/Datasets/Group3/Facebook-Ego/348.edges"
ENV TWITTER_URL="https://raw.githubusercontent.com/wang422003/Complex-Networks_exercise/main/Datasets/Group3/Twitter-Ego/789071.edges"


CMD ["python", "-u", "my_script.py"] 


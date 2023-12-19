FROM python:3.10.12

WORKDIR /home/newwork

COPY requirements.txt /home/newwork/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY my_script.py /home/newwork/my_script.py

# Set environment variables 
ENV FACEBOOK_URL="https://raw.githubusercontent.com/wang422003/Complex-Networks_exercise/main/Datasets/Group3/Facebook-Ego/348.edges"
ENV TWITTER_URL="https://raw.githubusercontent.com/wang422003/Complex-Networks_exercise/main/Datasets/Group3/Twitter-Ego/789071.edges"

#COPY output.txt /home/newwork/output.txt
#ENV OUTPUT_FILE="output.txt"

CMD ["python", "-u", "my_script.py"] 


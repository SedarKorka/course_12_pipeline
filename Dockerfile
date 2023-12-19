FROM python:3.10.12

WORKDIR /home/network
RUN mkdir /home/network/output

COPY requirements.txt /home/network/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY my_script.py /home/network/my_script.py

# Set environment variables 
ENV FACEBOOK_URL="https://raw.githubusercontent.com/wang422003/Complex-Networks_exercise/main/Datasets/Group3/Facebook-Ego/348.edges"
ENV TWITTER_URL="https://raw.githubusercontent.com/wang422003/Complex-Networks_exercise/main/Datasets/Group3/Twitter-Ego/789071.edges"

#COPY output.txt /home/network/output.txt
#ENV OUTPUT_FILE="output.txt"

CMD ["python", "-u", "my_script.py"] 


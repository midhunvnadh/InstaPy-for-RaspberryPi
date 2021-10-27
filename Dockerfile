FROM ubuntu:20.04
ENV DEBIAN_FRONTEND "noninteractive"
WORKDIR /bot
ADD ./root/. /


RUN apt-get update && \
	apt-get install -y software-properties-common && \
	add-apt-repository ppa:deadsnakes/ppa && \
	apt-get update && \
	apt install -y python3.8 python3.8-dev python3-pip firefox-geckodriver firefox && \
	pip install instapy && \
	sed -i "s#browser = webdriver.Firefox(#browser = webdriver.Firefox(service_log_path=os.devnull,#g" /usr/local/lib/python3.8/dist-packages/instapy/browser.py && \
	sed -i "s#bitness in name]#bitness in name and name[-3:] != 'asc' ]#g" /usr/local/lib/python3.8/dist-packages/webdriverdownloader/webdriverdownloader.py

CMD ["bash", "./update_and_start.sh"]

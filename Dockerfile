FROM python

RUN apt-get update && apt-get install -y cmake

RUN wget https://github.com/libgit2/libgit2/archive/v0.25.1.tar.gz
RUN tar xzf v0.25.1.tar.gz
RUN cd libgit2-0.25.1 \
    && cmake . \
    && make \
    && make install

RUN pip install pygit2
RUN pip install django

RUN ldconfig

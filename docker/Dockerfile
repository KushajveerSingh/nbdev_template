FROM kushaj/fastai:latest

LABEL author  = "Kushajveer Singh" \
      email   = "kushajreal@gmail.com" \
      website = "https://kushajveersingh.github.io/blog/"

WORKDIR /home/default

# To install library with git
RUN git clone {git_url}  && \
    pip install -e {lib_name}

# To install using pip
RUN pip install {lib_name}
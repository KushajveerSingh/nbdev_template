# {Project Name}
> Summary description here.


**Note**:- If you are reading this message, then it means this is still work in progress. Some things mentioned in README may not work.

[![CI-Badge](https://github.com/KushajveerSingh/{REPO_NAME}/workflows/CI/badge.svg)](https://github.com/KushajveerSingh/{REPO_NAME}/actions?query=workflow%3ACI) [![PyPI](https://img.shields.io/pypi/v/{REPO_NAME}?color=blue&label=pypi%20version)](https://pypi.org/project/{REPO_NAME}/#description) [![Docker](https://raw.githubusercontent.com/KushajveerSingh/nbdev_template/master/docs/images/docker%20image-not%20available-red.svg)](https://hub.docker.com/repository/docker/kushaj/{REPO_NAME})

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [{Project Name}](#project-name)
  - [Installation](#installation)
    - [PyPI](#pypi)
    - [Docker Image](#docker-image)
    - [From Source](#from-source)
  - [Usage details](#usage-details)
  - [Tests](#tests)
  - [Contributing](#contributing)
  - [License](#license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Installation

### PyPI
```
pip install {REPO_NAME}
```

### Docker Image
The docker image builds on [kushaj/fastai](https://hub.docker.com/repository/docker/kushaj/fastai) docker image. I have setup **Ubuntu, sudo, default user, conda, jupyter, cuda, pytorch, fastai** in the base image. Please, check the [README](https://hub.docker.com/repository/docker/kushaj/fastai/) for the complete details of the base image.

To pull the image from [Dockerhub](https://hub.docker.com/repository/docker/kushaj/{REPO_NAME}), use this command
```
docker pull kushaj/{REPO_NAME}:latest
```

Now you can start a container using this command
```
docker run -it --gpus all --name {REPO_NAME} -p 8889:8889 --ipc=host kushaj/{REPO_NAME}
```

* `-it` - opens a terminal connected to the container
* `--gpus all` - which GPUs to use in the container (use `device=0` to only use GPU0)
* `--name {REPO_NAME}` - name of the container (can by anything)
* `-p 8889:8889` - format is {host_port}:{container_port}. This is used to run the jupyter notebook. 
* `--ipc=host` - PyTorch uses shared memory to share data between processes, so if torch multiprocessing is used (e.g. for multithreaded data loaders) the default shared memory segment size that container runs with is not enough and using `--ipc=host` resolves this issue.

If you want to add another terminal to the container, run `docker ps` to get the **id** of the container you want to connect the terminal to. Now use this command to add a terminal `docker exec -it {id} bash`.

### From Source
```
git clone --depth=1 https://github.com/KushajveerSingh/{REPO_NAME}.git
cd {REPO_NAME}
pip install .
```

If you want to browse the notebooks and build the library from them you will need [nbdev](https://nbdev.fast.ai/).

## Usage details

## Tests
To run the tests under `tests` folder, use this command in the home directory ([hypothesis](https://pypi.org/project/hypothesis/) must be installed):
```
python -m unittest discover -s tests -v
```

To run `nbdev` tests i.e. run the jupyter notebooks in `nbs` folder, use this command:
```
nbdev_test_nbs
```

**Note**:- `nbdev_test_nbs` runs the notebooks in parallel. If the notebook contains some training code (in which a model is trained), then that code will also run. You can comment out the code that issues the training of model, or mark those cells as [slow](https://nbdev.fast.ai/test/), so that these cells do not run and the tests can complete is meaningful time.

## Contributing
After you clone this repository, please run `nbdev_install_git_hooks` in your terminal. This sets up git hooks, which clean up the notebooks to remove the extraneous stuff stored in the notebooks (e.g. which cells you ran) which causes unnecessary merge conflicts. Install [nbdev](https://github.com/fastai/nbdev) is not available.

Before submitting a PR, check that the local library and notebooks match. The script `nbdev_diff_nbs` can let you know if there is a difference between the local library and the notebooks.
* If you made a change to the notebooks in one of the exported cells, you can export it to the library with `nbdev_build_lib`.
* If you made a change to the library, you can export it back to the notebooks with `nbdev_update_lib`.

## License
[Apache License 2.0](LICENSE)

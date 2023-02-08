# Machine Learning Docker Template

Baseline docker containers and docker compose files that works on all the platforms (including Apple Silicon).

There are 3 templates in total. Base template is the most general one and includes libraries you might need for machine learning. Like scikit-learn and pandas. Other 2 folders are created for deploying deep learning models (PyTorch and TensorFlow). Since MPS (GPU Acceleration for Apple silicon) is not supported on Docker yet, codes will ran on CPU. So, training large models using these docker containers will not be optimal. However, you could still use them for deployment and production. For a detailed installation, check out my YouTube video.

For testing the docker containers, sample codes are added into main.py files. Remove them before use!

## Run Python files

Put all your code inside the src folder and change `"python main.py"` line inside docker-compose file with your main python folder or script. src folder will directly be copied inside the container.
```
cd template
docker build .
docker-compose build
docker-compose up
```
## Run Jupyter-Notebok

Go to the docker compose folder, change `"python main.py"` with `"jupyter-notebook --ip 0.0.0.0 --port 8000"`. Then, follow the instructions:
```
cd template
docker build .
docker-compse build
docker-compose up
```
After that, you should see a prompt saying that server is online at . Use that link to access your notebook. If you want to use your notebook in your local network, you need to replace your computer's ip address with 127.0.0.1. Then, you should be able to access it in your local network.

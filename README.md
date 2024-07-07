# Medical ChatBot

## Step to run the Project

### Create a new conda environment named 'mchatbot' with Python 3.9
```bash
conda create -p  mchatbot python=3.9 -y
```
### Activate the 'mchatbot' environment
```bash
conda activate mchatbot
```
### Install the Requirement library
```bash
pip install -r requirements.txt
```

### Create a .env file in the root directory and add your pincone credentials as follows:
```ini
PINCONE_API_KEY="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
```
### Download the quantize model from the link provided in model folder & keep the model in the model directory:

```ini
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```
## TechStack Used
## Programming Language used for the project
- ### Programming Language: Python

## Generative AI Framework used for the project
- ### Generative AI Framework: Langchain 

## Frontend Framework used for the project
- ### Frontend Framework: Streamlit

## Large Language Model (LLM) used for the project
- ### LLM: Meta Llama 2

# Vector Database used for the project
- ### Vector Db: Pinecone



























import os
from huggingface_hub import HfApi, login

# Set your Hugging Face token here or use 'huggingface-cli login' in terminal
HF_TOKEN = os.getenv("HF_TOKEN")
DATASET_REPO_ID = 'sharmax-vikas/Elon_Musk'
DATASET_FILE = 'elon_musk_finetunned/data/trainset/merged/merged_trainset.jsonl'

# Login to Hugging Face
login(token=HF_TOKEN)

# Initialize API
api = HfApi()

# Create the dataset repo if it doesn't exist
try:
    api.create_repo(repo_id=DATASET_REPO_ID, repo_type='dataset', exist_ok=True)
except Exception as e:
    print(f"Repo creation error: {e}")

# Upload the file
api.upload_file(
    path_or_fileobj=DATASET_FILE,
    path_in_repo='merged_trainset.jsonl',
    repo_id=DATASET_REPO_ID,
    repo_type='dataset'
)
print('Upload complete!')

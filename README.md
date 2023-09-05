# RAG with Amazon Bedrock using Titan Embeddings and Amazon OpenSearch Vector Engine

This code sample demonstrates using RAG (Retrieval Augmented Generation) with [Amazon Bedrock](https://aws.amazon.com/bedrock/)'s [Titan embeddings](https://aws.amazon.com/bedrock/titan/) and a large language model (LLM). It creates text embeddings stored in [Amazon OpenSearch](https://aws.amazon.com/opensearch-service/) with [vector engine support](https://aws.amazon.com/about-aws/whats-new/2023/07/vector-engine-amazon-opensearch-serverless-preview/). This enables prompt engineering for more accurate LLM responses.

This sample does the following

- Creates embeddings using [Titan embeddings](https://aws.amazon.com/bedrock/titan/) LLM
- Saves embeddings to Amazon OpenSearch
- Using LangChain, input Query from you (user) is queried for retrieval from vectorized data from Amazon OpenSearch
- Retrieval from OpenSearch matching the question is fed to Amazon Titan Text LLM as context
- Amazon Titan Text augments the response based on the User Query

## Prerequisites

1. This was tested on Python 3.11.4
2. It is advise to work on a clean environment, use `virtualenv` or any other virtual environment manager.

    ```bash
    pip install virtualenv
    python -m virtualenv venv
    source ./venv/bin/activate
    ```

3. Run `./download-beta-sdk.sh` to download the beta SDK for using Amazon Bedrock
4. Install requirements `pip install -r requirements.txt`
5. Install [terraform](https://developer.hashicorp.com/terraform/downloads?product_intent=terraform) to create the OpenSearch cluster

    ```bash
    brew tap hashicorp/tap
    brew install hashicorp/tap/terraform
    ```

## Usage

First, deploy an OpenSearch cluster with Terraform:

```bash
cd ./terraform
terraform init
terraform apply -auto-approve
```


Using Sagemaker jupyter notebook rag1.ipynb and then rag2.ipynb

### Cleanup

```bash
cd ./terraform 
terraform destroy # Confirm with yes
```
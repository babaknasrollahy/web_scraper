from flask import Flask 
import requests
import json

app = Flask(__name__)

@app.route('/')
def sender_json():
    text = """Unleashing the Power of Quantized Models: A New Era for Generative AI
Sean Bailey
·
Follow
4 min read
·
4 days ago
2
In the rapidly evolving world of AI, Large Language Models (LLMs) such as LLama 2 have been making waves, offering unprecedented capabilities in natural language understanding and generation. However, as highlighted in recent publications, the use of these models often comes with a significant caveat — the need for high-powered, expensive cloud computing resources to scale effectively.
The Challenge
While the power of LLMs is undeniable, the resource-intensive nature of these models can be a barrier to their widespread adoption, particularly for organizations operating under budget constraints or in environments where high-powered computing resources are not readily available. This has led to a growing interest in finding more cost-effective, scalable solutions for deploying these models.
The Solution: Quantized Models
Enter Quantized LLMs, a promising solution that has been successfully deployed on AWS Lambda. Quantized models use reduced numerical precision, significantly improving inference time and cost-efficiency without a substantial impact on output quality. This makes them an attractive option for businesses looking to leverage the power of LLMs in a more resource-friendly manner.
Introducing Llama-Anywhere
Building on this concept, I’ve developed a new open-source project, Llama-Anywhere, which takes the potential of quantized models a step further. This repository provides a framework for quantizing any model compatible with llama.cpp, allowing for a wide range of models to be optimized for cost and speed.
The Llama-Anywhere repository includes Docker containers that can be directly deployed and used to experiment on standard EC2 instances or as SageMaker Endpoints. This provides a flexible, user-friendly platform for developers to explore the potential of quantized models in their own applications.
Deploying and Using Llama-Anywhere API on an EC2 Instance
The llama-anywhere project offers a seamless way to deploy and experiment with quantized models on standard EC2 instances or as SageMaker Endpoints. Here’s a quick guide to get you started:
Prerequisites
An AWS account with necessary permissions.
AWS CLI, CDK CLI, Python 3, and Node.js installed.
Installation
Clone the repository:
git clone https://github.com/baileytec-labs/llama-anywhere.git
Usage
The stack takes several parameters, such as deployment type, model information, instance type, region, and port. You can supply these using the cdk.json file or via the command line.
cdk deploy --context deployType=f --context model=YourModel --context hftoken=YourToken --context instanceType=t2.micro --context region=us-east-1 --context portval=8080
Interacting with the Endpoints
The llama-anywhere project provides FastAPI endpoints in both the foundational and quantized containers, allowing you to easily interact with the models. Here’s a quick guide on how to use these endpoints:
Each container serves a large language model for text generation. You can configure the model and generate text using the /configure and /invoke endpoints respectively. The foundational container is designed for foundational models hosted on HuggingFace, and the quantized container is designed for llama.cpp compatible quantized models.
To configure the model, make a POST request to /configure with a JSON payload specifying the HuggingFace model name and your HuggingFace API token. Once the model is configured, you can generate text by making a POST request to /invoke with a JSON payload containing your input text.
The Research: Quantized Models in Action
My recent research paper, “From Cloud to Edge: Quantized Models Make Generative AI Universally Scalable,” provides an in-depth analysis of the performance of quantized models. The paper compares the Llama-2 7B foundation model and its quantized version across various EC2 instance types, demonstrating that the quantized model runs about 200% faster and costs around 50% less per inference versus the foundation model when compared 1:1, with only slight changes in output resolution.
Why This Matters
By leveraging the frameworks found in the llama-anywhere project and the power of quantized models, organizations can deploy generative AI solutions using the latest open-source LLMs that are not only more cost-effective, but with improved speed and scalability. This opens up a world of possibilities for applications in areas such as customer service, content generation, and more. The barrier of entry and the cost of experimentation is now lowered!
Conclusion
As we move into a new era of AI, it’s time for organizations to think laterally and explore how they can leverage frameworks like Llama-Anywhere to harness the power of quantized models. Whether you’re a do-er or a decision maker, I encourage you to delve into the Llama-Anywhere repo and the research paper for more details. The future of generative AI is here, and it’s more accessible than ever.Unleashing the Power"""



    url = 'http://localhost:5005/receive_json'  # Replace with the URL of the other Flask application's endpoint
    payload = {
                'content': text,
                'name' : 'test',
                'family' : 'testy'
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    # Process the response if needed
    if response.status_code == 200:
        print('Text sent successfully')
    else:
        print('Error sending text')
        
    return("ok")
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
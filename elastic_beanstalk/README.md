# Deploy a Flask API to Elastic Beanstalk
---
_Why use EB?_   

**Faster Deployment**: Once EB is configured, you can provision, modify, and terminate an EC2 directly from the command line.  

**Automated Environment Setup**: For Python apps, EB will automatically set up your Python environment and install all dependencies listed in `requirements.txt`.

**Automated Infrastructure**: EB creates security groups, a load balancer, an autoscaler, and (for a Flask app) an Nginx web server for you.  

**Domain Name**: EC2's provisioned by EB are given domain names for public access. No more ugly IP addresses or paying for registered domains.

Instructions
---
1. after cloning repo, create a local python environment by running `python3 -m virtualenv env`
2. activate the environment you just created by running `source env/bin/activate`
3. run `pip freeze` and check that no dependencies are returned. This ensures you've successfully activated your new environment.
4. run `pip install -r requirements.txt`.

### Setting up Elastic Beanstalk CLI
1. Follow the instructions for steps 1 (Overview) and 2 (Quick Start) [here](https://github.com/aws/aws-elastic-beanstalk-cli-setup).
2. Run `python ./aws-elastic-beanstalk-cli-setup/scripts/ebcli_installer.py`. This creates a virtual environment containing the EB CLI in a folder called `.ebcli-virtual-env`.
3. Activate this virtual env by running `~/.ebcli-virtual-env/bin/activate`. **The location of the environment may be different on your computer.**
4. From this project's root directory (`hiroshis_flask_api`), run `eb init`. You will have to complete several prompts.
5. Run `eb create`. This creates an Elastic Beanstalk environment and application.
6. If everything is set up correctly, running `eb open` will display your deployed app in a browser.
7. Cleanup by running `eb terminate`.

### Troubleshooting
- Make sure you configure your AWS CLI with the keys for a user with admin priviliges.
- EB needs to create a load balancer. To do so, you need to have at least 2 availability zones with 2 subnets each, one of which has to be a default subnet. (e.g. `us-east-1a` and `us-east-1b` each need two subnets.) See [here](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html#create-default-subnet) on instructions on how to create a default subnet.
- If the app is running but your POST requests are giving you errors, make sure your request looks something like `curl -X POST <your elastic beanstalk url> -H 'Content-Type: application/json' -d '{"name":"chester"}'`
- Remember that the POST request needs to be made to the `/cat` endpoint.
- If all else fails, check the logs by running `eb logs --zip`. This will create a zip containing logs in the `.elasticbeanstalk` directory.
- [Instructions from AWS docs](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html).

# most-watched-repo
Creating Docker Image:
To create image you need to run the following command after cloning the most-watched-repo repository into your local machine.
docker image build --no-cache -f Dockerfile -t ubuntu:18.04 .

Once the above command have been completed successfully, you can run the Container and get details of top contributors in most watched repo.
--org = GitHub Organization Name
--top = Top contributor names in the most watched repo
Example:
docker run ubuntu:18.04 --org ubuntu --top 5

# most-watched-repo

logical steps:

1. Read the arguments, verify whether organization exists and repo contributors count
2. Look for the organization repo's and get the repos list
3. Look for the each repo and its watchers count
4. Create sorted dictionary and get the most watched repo by using its watched count
5. Take the most watched repo and get the contributors of it
6. Sort the contributors using number of commits in the repo
7. Create sorted dictionary and get the top N contributors from the top
8. Print the top N contributors



Creating Docker Image:
To create image you need to run the following command after cloning the most-watched-repo repository into your local machine.

docker image build --no-cache -f Dockerfile -t ubuntu:18.04 .

Once the above command have been completed successfully, you can run the Container and get details of top contributors in most watched repo.

--org = github organization name

--top = top contributor names in the most watched repo

Example:
docker run ubuntu:18.04 --org ubuntu --top 5

# Pipe line to calculale the number of edges and nodes for facebook and twitter network

## How to run this pipeline

- Clone the repository:

```
git @github.com:SedarKorka/course_12_pipeline.git
```

- Build the image (run this command in the same folder where you cloned the repo):

```
docker build -t pipeline .
```

- You can now run the pipeline with the following command (change `/absolute/path/` to the path
on your machine)
- Example 
```
docker run --rm --name housing_container -v  /absolute/path/:/home/network/output:rw  pipeline  
```

When it will work correctly , you should the output folder with `output/` folder.

## Requirements

You need to have Docker installed, and also python 3.10

## Actions
- You can also change the url of the networks in Docker file


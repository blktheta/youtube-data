### Under progress
The goal is to create a robust automated infrastructure system using modern open source tools. The stack is subject to change during the initial phase of setting everything up.

#### Expected tools to be used in the project.
| Stage | Tool |
| :--- | :---: |
| Infrastructure | Terraform/Docker |
| Orchetration | Prefect |
| Extract & Load | Python |
| Transformation | Data Build Tool (DBT) |
| Warehouse | Google BigQuery |
| CI/CD | Github Actions/Google Cloud Run |  

#### Current planning 
- [x] implement Prefect storage with Github version control
- [x] implement Python CI with Github Actions
    - [x] inlcude Critical checks
    - [x] inlcude Linting checks
    - [x] inlcude Python tests
- [x] deploy Prefect flows from Github actions
- [ ] implement Google Cloud Run blocks in Prefect
    - [x] set up credentials
    - [ ] set up container GCP Artifact Registry/Docker
> Note: Currently investing time in AWS instead. The **gcloud** auth config-docker does not support **docker** installed via Snap, as the **docker** snap package does not currently provide an interface for credential helpers. More about it can be read at https://cloud.google.com/sdk/gcloud/reference/auth/configure-docker.
- [ ] store data in BigQuery
    - [ ] design All-in-One database
    - [ ] use hybrid data modeling approach with Star shema and OBT
- [ ] implement DBT CI wih Github actions
    - [ ] clone DBT repo
    - [ ] include tests
    - [ ] run models
- [ ] cost/performance analysis
- [ ] ...
- [ ] extra: create mutliple data image repos
    - [ ] repo: Python Docker image for extraction scripts
    - [ ] repo: Prefect Docker image for deployments
    - [ ] repo: DBT Docker image for transformation 


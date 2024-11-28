# News Aggregator

## About the project
#### What?
A microservice-based application for fetching news based on user-specified preferences. Once news are requested, app it delivers the most relevant news to the provided topic through the email.

#### Why?
The project is designed to practice building microservice architecture and interacting with various APIs.

#### State of the project
Currently, the project has completed the active development stage, the core functuanality is established. But there are lot's of things to polish

#### Used technologies
- [Python/Flask](https://flask.palletsprojects.com/en/stable/quickstart/)
- [Ruby/Rails](https://rubyonrails.org/)
- [Docker](https://www.docker.com/)
- [Dapr](https://docs.dapr.io/)
- RabbitMQ
- [MySQL](https://www.mysql.com/)
- [Google AI Studio](https://aistudio.google.com/prompts/new_chat)
- [Google Gmail API](https://developers.google.com/gmail/api/quickstart/python)
- [The Guardian Open Platform](https://open-platform.theguardian.com/)

## API Documentation
[Check here after you started the project](http://127.0.0.1:8081/api-docs/index.html)

## Aplication overview
### Microservice arcitecture
![screenshot goes here](/docs/project_arcitecture.png)

## Run the application
1. Clone the repository  
```sh
git clone https://github.com/PlaksinAnton/news_aggregator.git
```      

2. Before running the application it is important to get all secret keys for APIs configured.    
- Create .env file in project root directory:
```sh
nano .env
```      
- You will be filling it with next variables:
```
GUARDIAN_API_KEY=
GEMINI_API_KEY=
RAILS_MASTER_KEY=
MYSQL_ROOT_PASSWORD=
```   
- Get your own key for the news API [here](https://open-platform.theguardian.com/access/).    
- Get your own key for the AI API [here](https://aistudio.google.com/apikey).    
- Proper way to set up `RAILS_MASTER_KEY` for user manager service (for development) would be get Ruby on Rails and regeneraite credentials.yaml.enc file.    
Since the project is educational, I am sharing the master key publicly: `ac7ca3b008a4db5d586ddef0ce8970c1`
- `MYSQL_ROOT_PASSWORD` can be set up at your discretion.    

3. To set up Google Gmail API it is important to put your `credentials.json` to `./accessors/message_handler/` directory.    
How to set up your google api watch [here](https://www.youtube.com/watch?v=1Ua0Eplg75M), to generate credentials go [here](https://developers.google.com/gmail/api/quickstart/python).

4. Now you are ready to go! Run:    
```sh
docker compose up -d --build
```    

## Things for future development

- Add an ID to requests to distinguish callback messages.    

- Implement post field verification for news requests on behalf of the user manager. 

- Add a check and notification for email correctness.

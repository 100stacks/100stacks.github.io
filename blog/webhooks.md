# Webhooks 

The article will discuss intergraton with GitHub API Events.

## What are Webhooks?

## Why use Webhooks?

## Steps to Building a Webhook

1. User queries Hubot with a command  
2. Hubot sends command to GitHub
3. GitHub validates it can receive commands from our registered Hubot client
4. GitHub determines if it has a registered webhook for the command sent from our Hubot client
5. If so, GitHub sends the command to our webhook server
6. Webhook server verifies via HMAC hash that it can receive commands from our GitHub client
7. Webhook server sends the command via Maestro API to Jenkins
8. Jenkins queues up container build
9. Success/Failure is returned to Webhook server
10. Webhook server sends build status to our GitHub client
11. GitHub client receives the build status
12. GitHub client sends the build status to Hubot client

## Interaction with GitHub API

Expand on `GitHub` interaction with your servers.  `GitHub` does **not** interact directly with your servers, it acts a third-party client that sends and receives commands.


## Interaction with Carina (Docker)

### Next steps...

https://developer.github.com/v3/
https://developer.github.com/webhooks/

## GitHub Dev Guides

https://developer.github.com/guides/

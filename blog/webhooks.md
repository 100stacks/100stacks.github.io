# Webhooks 

The article will discuss intergraton with GitHub API Events.

## What are Webhooks?

Webhooks are part of any modern Continuous Development/Continuous Integration build process.

Webhooks have grown in popularity as a lightweight real-time API for interacting with mircoservices.  We can also refer to them as a HTTP Push API or web callback.

## Why use Webhooks?

What's so great about webhooks?  It borrows the functional `callback`, or event-loop pattern from JavaScript.  It provides a way to configure APIs asynchronously. 

Some benefits:
* They are used to automate repetitious and/or tedious processes across distributed teams to reduce possible
conflicts in the build process.
* Launching DevOps microservices.

## Steps to Building a Webhook

1. User queries Hubot with a command  
2. Hubot sends command to GitHub
3. GitHub validates it can receive commands from our registered Hubot client
4. GitHub determines if it has a registered webhook for the command sent from our Hubot client
5. If so, GitHub sends the command to our Webhook server
6. Webhook server verifies via HMAC hash that it can receive commands from our GitHub client
7. Webhook server sends the command to Jenkins
8. Jenkins queues up container build
9. Success/Failure is returned to Webhook server
10. Webhook server sends build status to our GitHub client
11. GitHub client receives the build status
12. GitHub client sends the build status to Hubot client
13. Hubot posts the build status to the registered chat channel(s)
14. All registered users see the build status from GitHub


## Interaction with GitHub API

Expand on `GitHub` interaction with your servers.  `GitHub` does **not** interact directly with your servers, it
acts a third-party client that sends and receives commands.


## Interaction with Carina (Docker)

### Next steps...

https://developer.github.com/v3/
https://developer.github.com/webhooks/

## GitHub Dev Guides

https://developer.github.com/guides/

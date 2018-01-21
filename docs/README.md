DisasterTag
===========
Made at SpartaHack 18
Presentation : http://slides.com/connorjones-1/disaster-tag

## Inspiration
We were very motivated to got after the challenges presented to during or immediately following a natural disaster, We came to the conclusion that the most deterministic factor of how well an event was handled was  by effective communication between first responders in the field and medical professionals in the hospital. 

## What it does
Our application works on two fronts. In the field our application is used by first responders to gather information on each person they come across in the area following a natural disaster. The first responder is able to tag the location a person was found as well as a name, level of severity of their injuries as well as any additional information that might be pertantet, ie "individual was found with leg pinned under log, possible fracture"

This information is then stored in our database where it can then be accessed by medical professionals upon patient arrival. Using this information gathered from the field, doctors can streamline the treatment process without the need to waste time gathering background data on each individual. 

## How we built it
We designed our application with scaling and flexibility in mind from the start. We developed locally on our machines using a docker-compose stack we created. Once we had our stack well established we moved our application onto the google compute platform(GPC) as a production environment. Because we had designed our application to be containerized it lends itself very quick and scalable deployments. After we were running in GPC we could setup ssl certificates from lets encrypt to secure our data transactions

## Challenges we ran into
Neither of us had a lot of web development experience so we both spent a lot of time learning the ins, outs, and idiosyncrasies of django which delayed much of our core functionality. Because we decided to integrate so many tooling options, troubleshooting was rather unique for us, particularly getting static files serving through nginx to gunicorn. 
### Barcodes...
Originally we had a big design goal of being able to tag a patient with a code, associate that barcode with that patient, and then be able to scan the code upon their arrival at the hospital. We ran into around 10 hours of issues because all the barcode scanning libraries we could find for we were written in nodejs(neither of us is proficient enough at javascript to develop in node). Ultimately we were unable to integrate a node library with our django application as we ran out of time. 

## Accomplishments that we're proud of
- One of our devs started with **0** MVC, django web development experience
- We have a production site running with proper ssl verification
- Proper use of docker-compose stack and containerization technology
- Having a working product in GCP, having never interacted with it before.

## What we learned
- Time managment
- Django
- GCP
- NGINX

## What's next for DisasterTags
Application features that would be added:
- Supporting barcode scanning and tagging
- Support image uploads to the databse
Technological addions that we would add given more time:
- Kubernetes
- Integrate dynatrace for performance indications
- More robust databse

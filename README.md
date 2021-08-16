## Table of content

- [Introduction](#introduction)
    - [What is Fresh Bites](#what-is-fresh-bites)
    - [Why did we create Fresh Bites](#why-did-we-create-fresh-bites)
- [Getting Started](#getting-started)
    - [Login/Signup](#login-signup)
    - [Additional Information](#additional-information)
- [Features](#features)
    - [Shopping Page](#shopping-page)
    - [Shopping Cart](#shopping-cart)
    - [Confirmation Page](#confirmation-page)
    - [Spoonacular API](#spoonacular-api)
- [Planned Future Features](#planned-future-features)
    - [Water Tracker with Alert](#water-tracker-with-alert)
- [A Bit About the Code](#a-bit-about-the-code)
    - [Technologies Used](#technologies-used)
    - [Things to Note for Potential Contributors](#things-to-note-for-potential-contributors)
- [License](#license)
- [Links](#links)

## Introduction

### What is Fresh Bites

Fresh Bites is an app that we created to help people live their healthiest lives. Fresh Bites makes it easier to plan their meals and diets by allowing people to buy individual foods and the ingredients of said foods. This allows people greater control over what people put in their bodies. 

### Why did we create Fresh Bites

We created Fresh Bites in order to allow people greater control over what people put into their bodies. If you read the ingredients section on the labels on common foods, you will see a number of ingredients you will not be able to pronounce. This is because they are not actual food ingredients but rather man-made chemical additives that often end up being harmful to our bodies over time. 

## Getting Started

Below are some instructions on how to get started on Fresh Bites to begin living a healthier lifestyle. 

### Login/Signup

### Additional Information

## Features

### Shopping Page

### Shopping Cart

### Confirmation Page

### Spoonacular API

## Planned Future Features 

### Water Tracker with Alert

## A Bit about the Code

### Technologies Used

On the Backend, we used Python with Flask to implement the logic of how each of our features work. We store the data using MySQL, which is a type of SQL Database. 

On the Frontend, we have implemented HTML, CSS, JavaScript, and Bootstrap. 

Additionally, we have implemented:
 - CI/CD using GitHub Actions 
 - Nginx
 - SSL Certification for additional security (HTTPS)
 - Monitoring using Graphana 
 - for Login/Signup
 - Docker to containerize different parts of the app (app, Nginx/SSL Certification, MySQL Database)

### Things to Note for Potential Contributors

In order to be able to test your additions locally, you have to install Flask and other necessary python packages. Those packages are specified in requirements.txt, the basic steps for Flask are shown below (for installing packages, recycle Step 3):

- Step 1: python3 -m venv venv
- Step 2: . venv/bin/activate
- Step 3: pip3 install Flask
- Step 4: export FLASK_ENV=development
- Step 5: flask run

## License

## Links
- [Fresh Bites Site](https://fresh-bites.tech/)
- [Site Repository](https://github.com/MLH-Fellowship/fresh-bites/)

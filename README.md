## Table of contents

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
- [About the Founders and Contributors](#about-the-founders-and-contributors)
    -[Avi](#avi)
    -[Gabriel](#gabriel)
    -[Monika](#monika)
    -[Brandon](#brandon)
- [A Bit About the Code](#a-bit-about-the-code)
    - [Technologies Used](#technologies-used)
    - [Things to Note for Potential Contributors](#things-to-note-for-potential-contributors)
- [License](#license)
- [Links](#links)

## Introduction

We are delighted to welcome you to our app [Fresh Bites](https://fresh-bites.tech)! Take your health and wellness into your own hands today!

### What is Fresh Bites

Fresh Bites is an app that we created to help people live their healthiest lives. Fresh Bites makes it easier to plan their diets and cook their meals by allowing people to buy individual foods and the ingredients of said foods. This allows people greater control over what people put in their bodies. 

### Why did we create Fresh Bites

We created Fresh Bites in order to allow people greater control over what people put into their bodies. Alot of times, we just don't know what we are putting into our bodies, especially when so many common foods list ingredients that are not even food items. So we wanted to make it easier for people to plan healthier meals and diets for themselves and their loved ones. Thus, Fresh Bites was born. 

## Getting Started

Below are some instructions on how to get started on Fresh Bites and begin living a healthier lifestyle. 

### Login/Signup

Befor you can shop or place any orders on Fresh Bites, you have to create and/or login to your Fresh Bites account. If you are not logged in, you will be unable to place any orders.

You can create an account by clicking on the Login/Signup tab of our fresh-bites.com Home page. Then, you can either login to your account:


Or you can click on the signup tab at the bottom of the login window to create your account: 

### Additional Information

Something else you might want to know is that you have to create an account to actually browse the items. This is to give early adopters and testers a head start in trying the fresh-bites app.

## Features

Below is an explanation of some of the features we have available so far.

### Shopping Page

Our Shopping Page displays all of the products available for you to purchase. You can add foods and ingredients to your cart from here:



Once you are done shopping, you can click on the little cart icon on the top right to access your shopping cart:

### Shopping Cart

Once you have clicked the shopping cart page, you can review the items on your page. This will allow you to place your order as well as change the quantity of each item in your cart:




Note: You must have items in your cart in order to access this page. If you do not have a cart in session, you will see this instead:




### Confirmation Page

Once you have placed your order, you will see this lovely confirmation page. This confirms that we have received your order and that it will be on its way to your place of residence ASAP. 

### Spoonacular API

We make use of the Spoonacular API, which gives us access to information on a ton of recipes for healthy and delicious foods, to power our app. 

## Planned Future Features 

Below are some features we plan on implementing in the future. 

### Water Tracker with Alert

In order to be our healthiest selves, we humans require at least 80 fl. oz of water every day. However, because of our busy lives, we often lose track of this and often fall short of our water requirement because of it. Thus, we intend to implement a water tracker so that you can count how much water you drink in a day. Additionally, we plan to add an alert system to remind you at specific times throughout the day to drink a cup of water, making it easier to track and successfully attain the necessary water intake for you.

## About the Founders and Contributors

### Avi

### Gabriel

### Monika

### Brandon

## A Bit about the Code

Below is some information about what we used to create this app, which will aid anyone looking to contribute to this project or otherwise interested in what we did here. 

### Technologies Used

On the Backend, we used Python with Flask to implement the logic of how each of our features work. We store the data using MySQL, which is a type of SQL Database. 

On the Frontend, we have implemented HTML, CSS, JavaScript, and Bootstrap. 

Additionally, we have implemented:
 - CI/CD using GitHub Actions 
 - Nginx
 - SSL Certification for additional security (HTTPS)
 - Monitoring using Graphana 
 - AUTH0 for Login/Signup
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
- [Check out Spoonacular!](https://spoonacular.com/)

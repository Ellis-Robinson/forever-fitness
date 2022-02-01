# Contents

- [User Experience](#user-experience)
    - [Strategy](#strategy)
        - [User Stories](#user-stories)
        - [Structure](#structure)
    - [Design](#design)
        - [Database Schema](#database-schema)
        - [Apps/Models](#apps/models)
        - [Wireframes](#wireframes)
    - [Features](#features)
- [Technologies](#technologies)
    - [Languages](#languages)
    - [Libraries, Frameworks and programs](#libraries-frameworks-and-programs)
- [Testing](#testing)
- [Bugs and Fixes](#bugs-and-fixes)
- [Deployment](#deployment)
- [Credits](#credits)

# User Experience

## Strategy

### User goals
- Find fitness related products
- Attened fitness classes

### Site owner goals
- Provide an enjoyable user experience
- Offer a range of relevent products
- Get returning customers

### User Stories

![User Stories 1-13](docs/README-imgs/user_stories_1-13.png)
![User Stories 14-30](docs/README-imgs/user_stories_14-30.png)

### Structure 

- Consistancy and intuitiveness throughout the site.
- Users are able to access the main areas; Products, Profile and Shopping Bag, within 3 clicks from any page.
- Base template containing the navigation section and displaying it across the whole site.
- Each call to action and all links clearly and simply explain their intention.

## Design

### Database Schema

![Database Schema](docs/README-imgs/database_FF.png)

### Apps/Models

- Bag app:
    - Containts context.py which stores logic for the shopping bag and delivery costs usable across the whole site
---
- Checkout app:
    - Order model:
        - Foreign key = Profile
        - Contains information about each order including; customer information, users profile, delivery cost and order total.
        - Generates a unique order number.
        - Updates the total using items from OrderLineItem model.
    - OrderLineItem model:
        - Foreign key = Order, Product
        - Stores if a product has a size and the quantity.
        - Saves the total price if contains multiples of the save product.
---
- Products app:
    - Category model:
        - Contains category name.
    - Product model:
        - Foreign key = Category
        - Contains information on each product including if it has sizes.
---
- Profile app:
    - Profile model:
        - One to One connection relationship User model
        - Contains delivery information about the user
---
- Wishlist app:
    - Wishlist model:
        - foreign key = Profile
        - Contains items from WishlistLineItem model
    - WishlistLineItem model:
        - foreign key = Wishlist, Product
---
- Workouts app:
    - TypeOfWorkout model:
        - Contains a name and image
    - Workout model:
        - foreign key = TypeOfWorkout
        - Many to Many relationship with Profile model
        - Contains information about the workout i.e date, location
---

### Wireframes

- [Checkout Page desktop-tablet-phone](docs/README-imgs/checkout.png)
- [Home Page desktop-tablet-phone](docs/README-imgs/home_page.png)
- [Item Details Page desktop-tablet-phone](docs/README-imgs/item_details.png)
- [Products Page desktop-tablet-phone](docs/README-imgs/products.png)
- [Shopping basket Page desktop-tablet-phone](docs/README-imgs/shopping_basket.png)

## Features

### Nav Section
The Navigation section is constant across the whole of the site and has:
- **Logo and brand name**: Links to the home page
- **Search bar**: Filters products by name and description
- **'My account'**: Dropdown menu
    
    *if user is Anonymous*
    - **'Register'**: Links to signup page
    - **'Login'**: Links to login page

    *If user is Authorised*
    - **'My Profile'**: Links to user profile
    - **'Logout'**: Links to logout page   
    
    *If user is Super User*
    - **'Product Management'**: Links to add product page
    - **'Class Management'**: Links to add workout page
- **Shopping basket**: Displays price and links to shopping bag page
- *Sort/Filter selection*
    - **'All Products'**: Dropdown menu
        -**'By Price'**: Links to products page and sorts all products by price
        -**'By Rating'**: Links to products page and Sorts all products by rating
        -**'By Category'**: Links to products page and Sorts all products by category
        -**'All Products'**: Links to products page
    - **'Clothing'**: Dropdown menu
        - **Shorts**: Links to products page and filters by category 'shorts'
        - **Tops**: Links to products page and filters by category 'tops'
        - **All Clothing**: Links to products page and filters by category 'tops' & 'shorts'
    - **'Accessories'**: Dropdown menu
        - **Yoga**: Links to products page and filters by category 'yoga'
        - **Boxing**: Links to products page and filters by category 'boxing'
        - **All Accessories**: Links to products page and filters by category 'yoga' & 'boxing'
    - **'Consumables'**: Dropdown menu
        - **Powders**: Links to products page and filters by category 'Powders'
        - **Bars**: Links to products page and filters by category 'Bars'
        - **All Consumables**: Links to products page and filters by category 'Powders' & 'Bars'


# Technologies

## Languages

## Frameworks, Libraries and Programs Used

# Testing

# Bugs and Fixes

# Deployment

# Credits
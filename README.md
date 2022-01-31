# Contents

- [User Experience](#user-experience)
    - [Strategy](#strategy)
        - [User Stories](#user-stories)
        - [Structure](#structure)
    - [Design](#design)
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
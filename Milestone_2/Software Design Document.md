# Software Design Document

## Project Name: Nutritional Food Comparison
## Group Number: 015

## Team members

| Student No. | Full Name         |
|-------------|-------------------|
| s5387195    | Ethan Davis       |
| s5347877    | Tristan Martins   |
| s5294045    | Ethan Baker       |


<div style="page-break-after: always;"></div>



# Table of Contents

<!-- TOC -->
* [Table of Contents](#table-of-contents)
  * [1. System Vision](#1-system-vision)
    * [1.1 Problem Background](#11-problem-background)
    * [1.2 System capabilities/overview](#12-system-capabilitiesoverview)
    * [1.3	Potential Benefits](#13potential-benefits)
  * [2. Requirements](#2-requirements)
    * [2.1 User Requirements](#21-user-requirements)
    * [2.2	Software Requirements](#22software-requirements)
    * [2.3 Use Case Diagrams](#23-use-case-diagrams)
    * [2.4 Use Cases](#24-use-cases)
  * [3.	Software Design and System Components](#3-software-design-and-system-components-)
    * [3.1	Software Design](#31software-design)
    * [3.2	System Components](#32system-components)
      * [3.2.1 Functions](#321-functions)
      * [3.2.2 Data Structures / Data Sources](#322-data-structures--data-sources)
      * [3.2.3 Detailed Design](#323-detailed-design)
  * [4. User Interface Design](#4-user-interface-design)
    * [4.1 Structural Design](#41-structural-design)
    * [4.2	Visual Design](#42visual-design)
<!-- TOC -->


<div style="page-break-after: always;"></div>



## 1. System Vision

### 1.1 Problem Background

#### 1.1.1 Problem Identification: What problem does this system solve?

The 'Nutritional Food Comparison' system, including its features like Food Search, Nutrition Breakdown, Nutrition Range Filter, Nutrition Level Filter, and the additional Meal Planner feature, aims to solve the following problems:

- **1) Complexity in Nutritional Data Analysis:** Nutritional information can be overwhelming and difficult to interpret manually. The system simplifies this process by providing tools that enable users to search for foods, analyse their nutritional content, and create personalised labels.

- **2) Inaccessible Visualisation:** The system makes nutritional data more accessible by incorporating simple visual elements like pie charts, bar graphs, and detailed nutritional breakdowns.

- **3) Efficient Decision-Making:** Tools such as the system's filtering and range selection allow users to quickly make informed food choices based on nutritional content and dietary requirements. 

- 4) Personalised Meal Planning: The Meal Planner feature, a unique and valuable component of the 'Nutritional Food Comparison' system, encourages users to create balanced meals by combining foods and analysing their nutritional value. This aids in achieving dietary goals such as weight management or nutrient intake optimisation. 

- **5) Time and Effort Reduction:** The system automates analysing and comparing nutritional data, reducing the time and effort required to plan meals and make healthy food choices.



#### 1.1.2 Dataset: What is the dataset used?
  
The Nutritional Food Database provides a comprehensive dataset showing detailed nutritional information for various food items. Each food item in the dataset is analyzed based on various nutritional parameters, making it a valuable resource for dietary and health inquiries.

The Column descriptions that are used in the dataset are listed below:
| Dataset                               | Description                                                                                                  |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Food                                  | The name or type of the food item.                                                                           |
| Caloric Value (in kcal)               | Total energy provided by the food, typically measured in kilocalories per 100 grams.                         |
| Fat (in g)                            | Total amount of fats in grams per 100 grams, including the breakdowns that follow.                           |
| Saturated Fats (in g)                 | Amount of saturated fats (which can raise cholesterol levels) in grams per 100 grams.                        |
| Monounsaturated Fats (in g)           | Amount of monounsaturated fats (considered heart-healthy fats) in grams per 100 grams.                       |
| Polyunsaturated Fats (in g)           | Amount of polyunsaturated fats (essential fats needed by the body) in grams per 100 grams.                   |
| Carbohydrates (in g)                  | Total carbohydrates in grams per 100 grams, including sugars.                                                |
| Sugars (in g)                         | Total sugars in grams per 100 grams, a subset of carbohydrates.                                              |
| Protein (in g)                        | Total proteins in grams per 100 grams, essential for body repair and growth.                                 |
| Dietary Fiber (in g)                  | Fiber content in grams per 100 grams, important for digestive health.                                        |
| Cholesterol (in mg)                   | Cholesterol content in milligrams per 100 grams, pertinent for cardiovascular health.                        |
| Sodium (in g)                         | Sodium content in milligrams per 100 grams, crucial for fluid balance and nerve function.                    |
| Water (in g)                          | Water content in grams per 100 grams, which affects the food’s energy density.                               |
| Vitamin A (in µg)                     | Amount of Vitamin A in micrograms per 100 grams, important for vision and immune functioning.                |
| Vitamin B1 (Thiamine) (in mg)         | Essential for glucose metabolism.                                                                            |
| Vitamin B11 (Folic Acid) (in mg)      | Crucial for cell function and tissue growth, particularly important in pregnancy.                            |
| Vitamin B12 (in µg)                   | Important for brain function and blood formation.                                                            |
| Vitamin B2 (Riboflavin) (in mg)       | Necessary for energy production, cell function, and fat metabolism.                                          |
| Vitamin B3 (Niacin) (in mg)           | Supports digestive system, skin, and nerve health.                                                           |
| Vitamin B5 (Pantothenic Acid) (in mg) | Necessary for making blood cells and helps convert food into energy.                                         |
| Vitamin B6 (in mg)                    | Important for normal brain development and maintaining the nervous and immune systems.                       |
| Vitamin C (in mg)                     | Important for the repair of all body tissues.                                                                |
| Vitamin D (in µg)                     | Crucial for the absorption of calcium, promoting bone growth and health.                                     |
| Vitamin E (in mg)                     | Acts as an antioxidant, helping to protect cells from damage caused by free radicals.                        |
| Vitamin K (in µg)                     | Necessary for blood clotting and bone health.                                                                |
| Calcium (in mg)                       | Vital for building and maintaining strong bones and teeth.                                                   |
| Copper (in mg)                        | Helps with the formation of collagen, increases iron absorption, and plays a role in energy production.      |
| Iron (in mg)                          | Essential for the creation of red blood cells.                                                               |
| Magnesium (in mg)                     | Important for regulating muscle and nerve function, blood sugar levels, and blood pressure.                  |
| Manganese (in mg)                     | Involved in bone formation, blood clotting, and metabolism of fats and carbohydrates.                        |
| Phosphorus (in mg)                    | Helps with the formation of bones and teeth and is necessary for cell growth and repair.                     |
| Potassium (in mg)                     | Helps regulate fluid balance, muscle contractions, and nerve signals.                                        |
| Selenium (in µg)                      | Important for reproduction, thyroid function, DNA production, and protecting the body from free radicals.    |
| Zinc (in mg)                          | Necessary for immune function, cell division, growth, wound healing, and carbohydrate breakdown.             |
| Nutrition Density                     | A metric indicating the nutrient richness of the food per calorie.                                           |

#### 1.1.3 Data Input/Output: What kind of data input and output is required?

Ensuring that both input and output mechanisms are intuitive and robust will enhance the user experience and accuracy of the 'Nutritional Food Comparison' project. The data input and output requirements are essential for the functionality and usability of the application. Below is a detailed breakdown:

**Data Input**
 - User Input for Food Search:
   Search Queries: This is text-based input where users can search for food items by name. This might include partial names or exact matches.
   - Filters: Criteria for filtering data, such as:
     Nutritional Langes: Users can select one of the nutrition and input minimum and maximum values, and the tool will display a list of foods that fall within those ranges.
     Nutritional Levels: Users can filter foods by their nutritional content levels—low, mid, and high—including fat, protein, carbohydrates, sugar, and nutritional density.
       - Low: Less than 33% of the highest value.
       - Mid: Between 33% and 66% of the highest value.
       - High: Greater than 66% of the highest value.     
 - Upload and Intergration:
   CSV File Upload: This option allows administrators to upload a CSV file containing nutritional data, which the system must parse and integrate into the database.
   - Image Upload: Allows administrators to upload images to integrate into the correct food items.

**Data Output**
 - Search Results:
   - List of Food Items: Display search results based on the user's query, including relevant nutritional information.
   Detailed Information: Provide detailed nutritional data for each food item, such as calories, fat content, vitamins, etc.
 - Nutritional Breakdown:
   - Tables: Detailed tables showing the nutritional breakdown of selected food items.
   - Graphs and Charts: Visual representations like bar charts. Pie charts or line graphs to illustrate comparisons between different foods or nutrient levels.
   - Comparison Tables: Allow users to compare nutritional values of multiple food items side by side.
   - Summary Statistics: Provide summary statistics or insights based on user queries, such as average calories, highest protein content, etc.
 - User Interface (UI):
   - Interactive Elements: Input fields for searching, filtering, and uploading, as well as buttons for generating reports or viewing detailed comparisons.
 - Export Options:
   Downloadable Reports: Users can export search results or comparison reports in formats like CSV, PDF, or Excel for offline analysis.

#### 1.1.4 Target Users: Who will use the system, and why?
The 'Nutritional Food Comparison' system is designed to cater to a range of users who have different needs related to dietary management, health, and nutrition. Below is a detailed breakdown of the projected Proto-Personas.

| **Proto Persona 1**                                                             |
|---------------------------------------------------------------------------------|
| Fitness Enthusiast "Alex"                                                       |
| **Age:** 28                                                                     |
| **Goal:** Balanced meal planning                                                |
| **User Needs:** Quick access to nutritional data for planning meals             |

---

| **Proto Persona 2**                                                             |
|---------------------------------------------------------------------------------|
| Professional Nutritionist "Dr. Emma"                                            |
| **Age:** 45                                                                     |
| **Goal:** Personalized client meal plans                                        |
| **User Needs:** Detailed nutritional info and tools for creating meal plans     |

---

| **Proto Persona 3**                                                             |
|---------------------------------------------------------------------------------|
| Health-Conscious Parent "Sarah"                                                 |
| **Age:** 35                                                                     |
| **Goal:** Planning meals for family                                             |
| **User Needs:** Focus on Vegan options for family meals                         |

---

| **Proto Persona 4**                                                             |
|---------------------------------------------------------------------------------|
| Elderly Individual "John"                                                       |
| **Age:** 70                                                                     |
| **Goal:** Maintain a balanced diet for healthy aging                            |
| **User Needs:** Low-sodium/sugar and heart-healthy meal options                 |

---

| **Proto Persona 5**                                                             |
|---------------------------------------------------------------------------------|
| College Student "Emily"                                                         |
| **Age:** 21                                                                     |
| **Goal:** Affordable and nutritious meals                                       |
| **User Needs:** Quick and easy meal planning with budget-friendly ingredients   |

---

| **Proto Persona 6**                                                             |
|---------------------------------------------------------------------------------|
| Busy Professional "David"                                                       |
| **Age:** 34                                                                     |
| **Goal:** Efficient meal planning amidst a busy schedule                        |
| **User Needs:** Quick, grab-and-go meal options with high nutritional value     |

---

| **Proto Persona 7**                                                             |
|---------------------------------------------------------------------------------|
| Young Athlete "Mia"                                                             |
| **Age:** 18                                                                     |
| **Goal:** Optimized nutrition for peak athletic performance                     |
| **User Needs:** High-protein and energy-rich meal options                       |

The 'Nutritional Food Comparison' system aims to cater to diverse users, including fitness enthusiasts, health-conscious parents, professional nutritionists, food manufacturers, elderly individuals, busy professionals, young athletes and the general populous. These users share a common need for reliable and accessible nutritional information to support their unique health and dietary goals. The system provides personalized tools and resources for meal planning, nutritional analysis, and decision-making, empowering users to make informed choices that align with their lifestyles and dietary requirements. Whether seeking to maintain a balanced diet, optimize athletic performance, or ensure product compliance, the system offers tailored solutions to these diverse needs.

### 1.2 System capabilities/overview

**System Functionality:** The 'Nutritional Food Comparison' desktop application is designed with a user-friendly interface to simplify the management and analysis of nutritional information. It addresses challenges like the complexity of data interpretation and the need for accessible visualisation. The system allows users to search for food items and analyse their nutritional content quickly. It also enables users to apply filters based on nutritional ranges and levels, tailoring search results to meet specific dietary needs, such as finding low-sodium or high-protein foods. Additionally, the system provides detailed nutritional breakdowns that are easy to understand, incorporating visual aids like pie charts and bar graphs. The application supports meal planning by allowing users to combine different foods and assess their nutritional values, helping them achieve dietary goals such as weight management or optimised nutrition for athletic performance.

**Features and Functionalities:** The 'Nutritional Food Comparison' system offers several key features to enhance the user's experience. The Food Search tools let users locate food items and quickly retrieve detailed nutritional data. Nutrition Range and Level Filters enable customised searches based on specific criteria, like calorie content or nutrient levels. The Meal Planner feature is a standout component, helping users create balanced meals by analysing the combined nutritional content of selected foods. The system allows the administration to use CSV and image uploads for data input, allowing easy integration of new informational data. On the output side, users can export their search results, nutritional breakdowns, and meal plans in various formats, such as CSV, PDF, or Excel, making offline analysis and sharing convenient. Designed for a wide range of users - from fitness enthusiasts to professional nutritionists - the system ensures personalised, informed decisions and dietary management, empowering users to take control of their health.

### 1.3	Benefit Analysis

The 'Nutritional Food Comparison' system provides significant value by streamlining the complex process of nutritional data analysis and meal planning, making it more accessible and actionable for users. Intuitive tools like the Food Search, Nutrition Filters, and Meal Planner benefit users by saving time and reducing the effort required to make informed dietary choices. By offering personalized insights and visual representations of nutritional information, the system helps users meet their health goals, whether managing weight, optimizing athletic performance, or ensuring a balanced diet. The ability to easily compare foods, create customized meal plans, and export detailed reports empowers users to take control of their nutrition with confidence and precision. Additionally, the system's user-friendly interface and comprehensive data integration capabilities ensure that users of all backgrounds, from busy professionals to health-conscious parents, can efficiently achieve their dietary objectives.

## 2. Requirements

### 2.1 User Requirements

The 'Nutritional Food Comparison' system is designed with a diverse range of users in mind, including fitness enthusiasts, nutritionists, busy professionals, and health-conscious individuals. These users are expected to interact with the program to achieve their dietary and nutritional goals efficiently. The system must provide the following functionalities from the end-user perspective:

**Narrative Descriptions**

**1) Fitness Enthusiast "Alex":** Alex, a 28-year-old fitness enthusiast, uses the system to plan meals that support his workout routines. He needs quick access to nutritional data to ensure his meals are balanced and aligned with his fitness goals. Alex frequently searches for high-protein foods, filters results based on specific nutrient levels and uses the Meal Planner to create meals that optimise his performance and recovery.

---

**2) Nutritionist "Dr Emma":** Dr Emma, a 45-year-old professional nutritionist, relies on the system to develop personalised meal plans for her clients. She needs detailed nutritional information and the ability to compare various food items to meet her clients' dietary needs. The system's export feature allows her to generate reports that can be shared with her clients, ensuring they have clear guidelines to follow.

---

**3) Busy Professional "David":** David, a 34-year-old professional, interacts with the system to quickly plan nutritious meals that fit his hectic schedule. He uses the system's filters to find grab-and-go meal options that are high in nutrients and low in unhealthy fats. The ability to save and export meal plans allows him to stay organised and maintain a balanced diet despite his busy lifestyle.

**Search and Filter Functionality:**
- Users need the ability to search for specific food items using text-based queries.
- The system must provide filters for nutritional content, allowing users to search based on calories, protein, fats, vitamins, and other nutrients.
- Filters should include ranges (e.g., low, medium, high) to help users find foods that match their dietary requirements.

**Detailed Nutritional Breakdown:**
- Users need access to comprehensive nutritional information for each food item, presented in an easy-to-understand format.
- Visual tools such as pie charts, bar graphs, and comparison tables should be available to help users interpret the data.

**Data Integration and Export:**
- Users must be able to upload their data, such as CSV files with nutritional information, to customise the database.
- The system should allow users to export their search results, nutritional breakdowns, and meal plans in multiple formats, such as CSV, PDF, or Excel, for offline analysis and sharing.

**Meal Planning Tools:**
- The system must provide a Meal Planner feature that allows users to combine various foods and evaluate the overall nutritional content of the planned meal.
- Users should be able to save and revisit their meal plans, adjusting them as needed to meet their goals.

**User-Friendly Interface:**
- The system must have an intuitive interface that allows users of varying technical skill levels to navigate and efficiently utilise all features.
- Interactive elements, such as clickable buttons and easy-to-use filters, should enhance the user experience and efficiency.

### 2.2	Software Requirements

- **R1.0 Food Search and Filtering:**
  - R1.1) The system shall allow users to search for food items using a text-based query.
  - R1.2) The system shall provide filters for users to narrow down search results based on nutritional ranges (e.g., calories, fats, proteins).
  - R1.3) The system shall enable users to apply nutritional level filters (low, medium, high) for specific nutrients such as sodium, sugar, and cholesterol.
  - R1.4) The system shall display a list of food items that match the search criteria, including relevant nutritional information.

---

- **R2.0 Nutritional Data Presentation:**
  - R2.1) The system shall provide a detailed nutritional breakdown for each food item, including metrics such as caloric value, fats, carbohydrates, proteins, vitamins, and minerals.
  - R2.2) The system shall present nutritional data in tables to compare multiple food items easily.
  - R2.3) To aid data interpretation, The system shall include visual representations of nutritional data, such as pie charts, bar graphs, and line graphs.
  - R2.4) The system shall allow users to compare the nutritional values of multiple food items side by side.

---
 
- **R3.0 Meal Planning:**
  - R3.1) The system shall provide a Meal Planner feature that allows users to create and save meal plans by selecting multiple food items.
  - R3.2) The system shall calculate and display the total nutritional content of the selected foods within a meal plan.
  - R3.3) The system shall enable users to modify meal plans by adding or removing food items and automatically updating the nutritional content.

---

- **R4.0 Data Integration and Export:**
  - R4.1) The system shall allow administrators to upload CSV files containing nutritional data, which will be parsed and integrated into the system's database.
  - R4.2) The system shall allow administrators to upload images associated with specific food items.
  - R4.3) The system shall enable users to export search results, nutritional breakdowns, and meal plans in multiple formats, including CSV, PDF, and Excel.
  - R4.4) The system shall allow users to download detailed reports of their meal plans and food comparisons.

---

- **R5.0 User Interface (UI) and Interaction:**
  - R5.1) The system shall provide an intuitive user interface that supports easy navigation and use of all features.
  - R5.2) The system shall include interactive elements like buttons, dropdown menus, and input fields to facilitate user interaction.
  - R5.3) The system shall offer real-time feedback and updates as users search for foods, apply filters, or create meal plans.
  - R5.4) The system shall allow users to save their settings and preferences for a personalised experience.

---

- **R6.0 Security and User Management:**
  - R6.1) The system shall require user authentication (e.g., login credentials) to access personalised meal plans and saved settings.
  - R6.2) The system shall ensure that valid data (e.g., CSV files) is uploaded for accuracy and completeness before integration.
  - R6.3) The system shall provide role-based access controls, allowing administrators to manage data and user permissions.

These requirements define the essential functionalities of the 'Nutritional Food Comparison' system, ensuring a comprehensive and user-friendly experience for all intended users.

### 2.3 Use Case Diagram
 
![System Use Case Diagram](./UC-05.png)

### 2.4 Use Cases

---

| Use Case ID    | UC-01 |
|----------------|-------|
| Use Case Name  | Nutritional Database |
| Actors         | Administrator |
| Description    | The administrator uploads nutritional data via CSV files and integrates it into the system's database. |
| Flow of Events | 1) The administrator selects uploading a CSV file. 2) The system prompts the administrator to select a file from the local system. 3) The system validates and parses the data, integrating it into the database. 4) The administrator receives confirmation of a successful upload.|
| Alternate Flow | If the CSV file contains errors, the system prompts the administrator to correct and re-upload the file. |

![UC-01, Nutritional Database](./UC-01.png)

---

| Use Case ID    | UC-02 |
|----------------|-------|
| Use Case Name  | Search Filters |
| Actors         | User |
| Description    |The user applies filters to narrow down food search results based on specific nutritional criteria. |
| Flow of Events | 1) The user selects a mineral filter option (e.g., calories, protein, fat). 2) The user sets a range or level (low, medium, high) for the selected nutrient. 3) The system filters and displays the food items that meet the criteria. |
| Alternate Flow | The user can view the nutritional breakdown in different formats (e.g., pie chart, bar graph).|

![UC-02, Search Filter](./UC-02.png)

---

| Use Case ID    | UC-03 |
|----------------|-------|
| Use Case Name  | Nutritional Breakdown |
| Actors         | User |
| Description    |The user views a detailed report of nutritional information for selected food items. |
| Flow of Events | 1) The user selects a food item from the search results. 2) The system displays a detailed nutritional breakdown in tabular and graphical formats. 3) The user can compare the breakdown with other food items. |
| Alternate Flow | The user can view the nutritional breakdown in different formats (e.g., pie chart, bar graph). |

![UC-03, Nutritional Breakdown](./UC-03.png)

---

| Use Case ID    | UC-04 |
|----------------|-------|
| Use Case Name  | Account Management |
| Actors         | User |
| Description    | Users can manage accounts, including registration, login, and account updates. |
| Flow of Events | Create Account: 1) The user selects "Register" and provides required details like email and password. 2) The system stores the user's details in the user database and sends a verification email. Verification: 1) The user clicks on the verification link sent via email. 2) The system verifies the account and activates it. Account Login: 1) The user enters their email and password on the login page. 2) The system authenticates the user and grants access to the account. |
| Alternate Flow | Reset (Passowrd: 1) The user selects "Forgot Password" and enters their registered email. 2) The system sends a password reset link. 3) The user resets the password via the link, and the system updates the user database. |

![UC-01, Account Management](./UC-04.png)

## 3.	Software Design and System Components 

### 3.1	Software Design

![Software Design Flowchart](./Flowchart.png)

### 3.2	System Components

#### 3.2.1 Functions

**Start Program:** The software starts, prompting users to log in or register.

- **Login:** Users enter credentials, which are validated. If incorrect, the user is prompted to re-enter the data.
- Register: Users create an account, verify via email, and log in.

**Dashboard:** Once logged in, users can select from key functionalities:
- **Food Search:** Users enter a food search query, and the system displays the nutritional details for each item.
- **Apply Filters:** Users can filter food items based on nutritional ranges (e.g., calories, protein, fat). Filtered results are displayed, and the user can adjust filters as needed.
- **Meal Planner:** Users add food items to a meal plan, and the system calculates the total nutritional value of the meal.

**Exporting and Saving:** Users can export their search results, filtered items, or meal plans as CSV, PDF, or Excel files for offline use.

**End Program:** After completing tasks, the user logs out or closes the software, ending the session.

#### 3.2.2 Data Structures / Data Sources

#### 3.2.2.1 Food Database

**Type**: **Dictionary** (or Database Table)  
**Usage**: Stores detailed nutritional information for each food item, where each food item is a key, and its corresponding nutritional data (calories, fats, proteins, etc.) is the value.

**Functions**:
- `search_food(query)`: Searches the food database for food items matching the search query.
- `get_nutritional_data(food_item)`: Retrieves the detailed nutritional breakdown of a specific food item.

---

#### 3.2.2.2 User Accounts

**Type**: **Dictionary** (or Database Table)  
**Usage**: Stores user account information, such as email, hashed passwords, and preferences. Each user is identified by a key (user ID or email), and their details are stored as values.

**Functions**:
- `register_user(user_data)`: Registers a new user and stores their information.
- `login_user(email, password)`: Authenticates the user by verifying their email and password.
- `update_user_account(user_id, new_data)`: Updates the user’s account details (e.g., email, password).
- `reset_password(email)`: Sends a password reset link to the user's email for password recovery.

---

#### 3.2.2.3 Meal Plan

**Type**: **List** (of dictionaries)  
**Usage**: Stores a list of food items selected by the user for a meal plan. Each food item is represented as a dictionary containing nutritional information.

**Functions**:
- `add_to_meal_plan(food_item)`: Adds a food item to the current meal plan.
- `calculate_meal_plan_nutrition(meal_plan)`: Calculates the total nutritional value (calories, proteins, etc.) of all food items in the meal plan.
- `remove_from_meal_plan(food_item)`: Removes a selected food item from the meal plan.
- `save_meal_plan(user_id, meal_plan)`: Saves the current meal plan for the user.

---

#### 3.2.2.4 Search Results

**Type**: **List** (of dictionaries)  
**Usage**: Temporarily stores search results after the user enters a query. Each result is a dictionary containing the food item and its basic nutritional information.

**Functions**:
- `sort_results(criteria)`: Sorts search results by selected criteria (e.g., calories, protein).
- `apply_filters(filters)`: Applies nutritional filters (e.g., calories range, low fat) to narrow down search results.

---

#### 3.2.2.5 Nutritional Filters

**Type**: **Dictionary**  
**Usage**: Stores the filters applied to search results. The dictionary keys represent the nutrient type (e.g., calories, protein), and the values represent the range or level.

**Functions**:
- `apply_filters(filters, search_results)`: Filters the food items in the search results based on the selected ranges provided in the filter dictionary.
- `clear_filters()`: Resets the filters to display all food items again.

---

#### 3.2.2.6 Nutritional Breakdown

**Type**: **Dictionary**  
**Usage**: Stores detailed nutritional information for a selected food item. The dictionary contains key-value pairs representing nutrients (e.g., calories, fats) and their corresponding amounts.

**Functions**:
- `get_nutritional_data(food_item)`: Fetches detailed nutritional data for a food item.
- `compare_foods(food_items)`: Compares the nutritional breakdown of multiple food items.

---

#### 3.2.2.7 CSV Data Source

**Type**: **CSV File (External Source)**  
**Usage**: Administrators upload CSV files containing nutritional data to be integrated into the system.

**Functions**:
- `upload_csv(file)`: Allows administrators to upload and import CSV files with nutritional data.
- `parse_csv(file)`: Parses the uploaded CSV file and integrates it into the food database.
- `validate_csv(file)`: Ensures that the CSV data is valid (correct format, complete data) before processing.

---

#### 3.2.2.8 User Preferences

**Type**: **Dictionary**  
**Usage**: Stores individual user preferences such as dietary restrictions, preferred units of measurement, and previously saved meal plans.

**Functions**:
- `save_user_preferences(user_id, preferences)`: Saves the user's preferences to their account.
- `load_user_preferences(user_id)`: Loads the user's saved preferences during login or session start.

---

#### 3.2.2.9 Export Data

**Type**: **Dictionary** (formatted for export)  
**Usage**: Temporarily stores data such as search results, nutritional comparisons, or meal plans for export. The data is structured for conversion into various file formats (CSV, PDF, Excel).

**Functions**:
- `export_to_csv(data)`: Converts the stored data into a CSV file.
- `export_to_pdf(data)`: Converts the stored data into a PDF report.
- `export_to_excel(data)`: Converts the stored data into an Excel file.

---

#### 3.2.2.10 Session Data

**Type**: **Dictionary**  
**Usage**: Temporarily stores session-specific information, such as the current user's ID, active meal plans, and applied filters. This data is used during the user’s active session.

**Functions**:
- `start_session(user_id)`: Initializes a session for the user, storing their ID and session-specific data.
- `end_session()`: Clears all session data when the user logs out or the session ends.

#### 3.2.3 Detailed Design

---

#### 3.2.3.1 Start Program
**Pseudocode**:
```
function start_program():
    display("Welcome to the Nutrition App")
    display("1. Login")
    display("2. Register")
    user_choice = get_user_input()
    
    if user_choice == "1":
        login()
    elif user_choice == "2":
        register()
    else:
        display("Invalid choice, please try again")
        start_program()
```

---

#### 3.2.3.2 Login
**Pseudocode**:
```
function login():
    email = get_user_input("Enter email: ")
    password = get_user_input("Enter password: ")
    
    if authenticate_user(email, password):
        dashboard()
    else:
        display("Invalid credentials, please try again")
        login()
```

---

#### 3.2.3.3 Register
**Pseudocode**:
```
function register():
    email = get_user_input("Enter email: ")
    password = get_user_input("Enter password: ")
    
    if email_already_registered(email):
        display("Email already in use, please log in or use a different email")
        start_program()
    else:
        save_user(email, hash_password(password))
        send_verification_email(email)
        display("A verification email has been sent. Please verify to log in.")
        login()
```

---

#### 3.2.3.4 Dashboard
**Pseudocode**:
```
function dashboard():
    display("Welcome to the Dashboard")
    display("1. Food Search")
    display("2. Apply Filters")
    display("3. Meal Planner")
    display("4. Export Data")
    display("5. Logout")
    
    user_choice = get_user_input()
    
    if user_choice == "1":
        food_search()
    elif user_choice == "2":
        apply_filters()
    elif user_choice == "3":
        meal_planner()
    elif user_choice == "4":
        export_data()
    elif user_choice == "5":
        end_program()
    else:
        display("Invalid choice, please try again")
        dashboard()
```

---

#### 3.2.3.5 Food Search
**Pseudocode**:
```
function food_search():
    query = get_user_input("Enter food name or keyword: ")
    results = search_food(query)
    
    if results:
        display_food_results(results)
    else:
        display("No results found. Try again.")
        food_search()
    
    dashboard()
```

---

#### 3.2.3.6 Apply Filters
**Pseudocode**:
```
function apply_filters():
    display("Filter by:")
    display("1. Calories")
    display("2. Protein")
    display("3. Fats")
    
    filter_choice = get_user_input()
    range_min = get_user_input("Enter minimum value: ")
    range_max = get_user_input("Enter maximum value: ")
    
    filters = set_filter(filter_choice, range_min, range_max)
    filtered_results = apply_filters(filters, search_results)
    
    if filtered_results:
        display_food_results(filtered_results)
    else:
        display("No results found within filter range")
    
    dashboard()
```

---

#### 3.2.3.7 Meal Planner
**Pseudocode**:
```
function meal_planner():
    display("Add food items to your meal plan")
    while True:
        food_item = get_user_input("Enter food name to add (or type 'done' to finish): ")
        
        if food_item == "done":
            break
        
        item_data = get_nutritional_data(food_item)
        if item_data:
            add_to_meal_plan(item_data)
            display(f"{food_item} added to meal plan")
        else:
            display("Food item not found. Try again.")
    
    total_nutrition = calculate_meal_plan_nutrition(meal_plan)
    display("Total Nutrition for Meal Plan:", total_nutrition)
    
    dashboard()
```

---

#### 3.2.3.8 Exporting & Saving
**Pseudocode**:
```
function export_data():
    display("Choose export format:")
    display("1. CSV")
    display("2. PDF")
    display("3. Excel")
    
    format_choice = get_user_input()
    
    if format_choice == "1":
        export_to_csv(data)
    elif format_choice == "2":
        export_to_pdf(data)
    elif format_choice == "3":
        export_to_excel(data)
    else:
        display("Invalid format, please try again")
        export_data()
    
    display("Data successfully exported")
    dashboard()
```

---

#### 3.2.3.9 End Program
**Pseudocode**:
```
function end_program():
    display("Thank you for using the Nutrition App. Goodbye!")
    logout_user()
    exit_program()
```

## 4. User Interface Design

### 4.1 Structural Design

![Structural_Hierarchy Design](./Hierarchy.png)

#### 4.1.1 Functions

**Start Program**: This is where the user begins their interaction with the app. It opens with a login or registration screen to ensure only authenticated users access the system. This prevents unauthorized access to personalized data like saved meal plans or preferences.

---

**Login/Register**:
- Login: Validates users' credentials, enabling them to access their dashboard.
- Register: Allows new users to create an account, verified via email, ensuring security and authentication.

These design choices ensure each user has a personalized experience based on their preferences and nutritional data.

---

**Dashboard**: Once logged in, users are presented with the central navigation hub. From here, they can easily access various modules like food search, filtering options, meal planning, and export tools. The dashboard serves as the command centre for the app, streamlining the user experience and making all features accessible from a single location.

---

**Food Search Module**: One of the core features allows users to search for food items to retrieve detailed nutritional information. The system uses a database of food items with nutritional data like calories, fats, proteins, etc. The search function is built to be fast and efficient, allowing users to find specific foods quickly.

---

**Filter Options Module**: Users can apply filters to search results based on their nutritional needs. This is important for those following specific diets or who need to monitor macronutrients like fats or proteins. The app allows customization and flexibility in searching for foods that meet the user's requirements.

---

**Meal Planner Module**: Users can add food items to a meal plan, and the system calculates the total nutritional value of the meal. This module helps users plan balanced meals by providing immediate feedback on the nutritional content, which is essential for those monitoring their intake.

---

**Export/Import Modules**: This feature allows users to export their search results, meal plans, or nutritional data into various formats like CSV, PDF, and Excel. It is helpful for offline access, sharing, or further analysis. The import function allows administrators to upload new nutritional data via CSV files.

---

**User and Nutritional Database**: These databases store information like user credentials, preferences, and the nutritional breakdown of food items. The user database handles account management, including registering new users, managing passwords, and editing account details. The nutritional database provides data for search results and meal planning.

---

**Search and Filtered Foods**: This step allows users to see their search results with applied filters. The filtered results give them more control over their choices, allowing for targeted meal planning and dietary management.

---

**Account Management Module**: This module allows users to manage their account details, such as email and password. Users can update their information and preferences to reflect dietary needs or personal data changes.

---

**Summary of Nutritional Data**: After using the filters or meal planner, users are shown a summary of the total nutritional content. This step is designed to provide clarity and assist users in making informed decisions about their food intake.


#### 4.1.2 Navigation & Design Choices

**Simplicity**: The design focuses on a user-friendly interface, allowing users to navigate easily through the app. Each module is clearly defined and accessible from the dashboard, ensuring users can quickly find what they need.

---

**Mobile & Desktop Compatibility**: The app is designed to work seamlessly on mobile devices and desktop computers, making it accessible to a broad audience. Its simplicity ensures that all users, regardless of their device, can navigate through the app without confusion.

---

**Data Visualization**: The information is presented through graphs, charts, and tables, allowing users to choose the format that works best for them. This flexibility in visualization improves user engagement and understanding of nutritional data.

### 4.2	Visual Design

![Visual Design](./Visual_Design_App.png)




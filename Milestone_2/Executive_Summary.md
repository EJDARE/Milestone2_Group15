# Executive Summary

Please provide your GitHub repository link.
### GitHub Repository URL: https://github.com/EJDARE/Milestone2_Group15.git

---

You should use your software to prepare an executive summary as outlined below for the five required features.

## 1. Food Name
### Description  
The "Food Name" feature allows users to quickly search for specific food items by entering their name in a search field. This feature supports searching for various types of food, such as snacks, meals, beverages, and more. Users can enter full or partial names, and the system will display results matching their query, making it easier to find information or products related to specific food items (e.g., Apple Pastry, Cream Cheese, Meat Pie).

**This feature is useful for:**

1. Browsing through a large database of foods quickly.
2. Finding specific nutritional information for a given food.
3. Locating food products in online stores or restaurants.

### Steps
1. Locate the search box: Find the text box next to the label "Food Name" at the top of the page or in the designated search section.
2. Input the food name: Type in the full name or part of the name of the food you want to search for. For example, if you're looking for "Apple Pastry," you can type either 
   "Apple" or "Apple Pastry" to get relevant results.
3. Auto-suggestions: As you type, a list of suggested food items may appear, allowing you to select from common or popular food options.
4. Click the Search icon: Once you've entered the food name, click on the magnifying glass (Search icon) next to the text box to initiate the search. Alternatively, 
   pressing the "Enter" key on your keyboard will also perform the search.
5. View the search results: The system will display a list of results matching your search query, including food items, related nutritional information, or available 
   products. You can then browse, select, or refine your search based on the results shown.

**Additional Features**
1. Auto-correction: If a food name is misspelled, the system may suggest the correct spelling or the closest match.
2. Filter options: After viewing search results, users may have the option to apply filters such as categories (e.g., snacks, desserts), dietary preferences (e.g., gluten-free, vegan), or specific brands.
3. History: Some versions of the system may save your recent searches for easy reference.

### Screenshots
Include screenshots for each step demonstrating the use of this feature.  
![Food Name 1.png](Food%20Name%201.png)

![Food Name 2.png](Food%20Name%202.png)

---

## 2. Select Carbs/Fats Or Vitamins
### Description  
The "Select Carbs/Fats or Vitamins" feature allows users to filter their search results based on specific nutritional categories. This dropdown menu includes options for Carbohydrates (Carbs), Fats, or Vitamins, enabling users to focus their search on food items with specific caloric or nutritional values.

**This feature is particularly useful for users who want to:**

1. Find foods based on macronutrient composition (e.g., high in fats or carbs).
2. Search for food items rich in certain vitamins (e.g., Vitamin C, Vitamin D).
3. Adjust their diet based on nutritional goals, such as lowering fat intake or increasing vitamin-rich food consumption.

### Steps
1. Locate the dropdown box: Find the dropdown box next to the label "Select Carbs/Fats or Vitamins" on the page.
2. Click on the dropdown box: Clicking on the box will open a list of available filtering options.
3. Choose an option: From the dropdown menu, select one of the following options:
   1. Carbs: Filters the search results by food items high in carbohydrates.
   2. Fats: Filters the search results to display foods high in fat content.
   3. Vitamins: Displays food items rich in various vitamins.
4. Apply the filter: Once an option is selected, the system will filter the available food items according to your selection, showing relevant results.

**Additional Features**
1. Dynamic Filtering: Once you select a filter option (Carbs, Fats, or Vitamins), the list of food items will update dynamically, allowing users to see the filtered results    immediately.
2. Multi-filtering: Some implementations of this feature may allow multiple selections, such as filtering for both Carbs and Fats simultaneously.
3. Nutritional Breakdown: After applying a filter, the system may also display a detailed nutritional breakdown of the food items that match your criteria.

### Screenshots
Include screenshots for each step demonstrating the use of this feature.  
![Filter 1.png](Filter%201.png)

![Filter 2.png](Filter%202.png)

---

## 3. Min
### Description  
The "Min" field allows users to set a minimum threshold value for their search, which relates to the previously selected category from the "Select Carbs/Fats or Vitamins" dropdown. For example, if the user selects "Carbs," the "Min" field specifies the minimum number of carbohydrates they want to query in the database. This feature is helpful for narrowing down search results to food items that meet a specific nutritional criterion, such as caloric value or nutrient content.

### Steps
1. Locate the "Min" text box: Find the text box labeled "Min" near the dropdown for "Select Carbs/Fats or Vitamins."

2. Enter a minimum value: Click inside the text box and type the minimum value you'd like to query. This could be a caloric value, amount of carbohydrates, fats, or            vitamins. For example:

   1. Carbs: Enter "10" to search for foods with at least 10 grams of carbohydrates.
   2. Fats: Enter "5" to search for foods with a minimum of 5 grams of fat.
   3. Vitamins: Enter "100" to search for foods with at least 100 mg of a specific vitamin.
      
3. Submit or proceed with the search: After entering the minimum value, either click the Search button (if available) or continue with the next filter/step if the system       supports further refinement.

**Example Scenarios**
1. If a user is looking for foods high in fats, they could select "Fats" from the dropdown and input "20" in the "Min" field. The search results will then show only foods      with 20 grams or more of fats.
2. If searching for vitamin-rich foods, the user could select "Vitamins" from the dropdown, enter a specific value (e.g., "50" mg) in the "Min" field, and the system will      display foods with at least that amount of vitamins.

**Additional Features**
1. Error Handling: If a user enters an invalid value (e.g., negative numbers or non-numeric characters), the system may prompt the user to correct the input.
2. Range Queries: In some systems, a "Max" field may also be available, allowing the user to specify both minimum and maximum values for a more precise search.

### Screenshots
Include screenshots for each step demonstrating the use of this feature.    
![Min 1.png](Min%201.png)

![Min 2.png](Min%202.png)


---

## 4. Max
### Description  
Max is short for maximum value, which is in relation to the prior step of "Select Carbs/Fats Or Vitamins". Max for example is the maximum number you want to query the database by such as Caloric Value.

### Steps
1. Click the textbox next to the word "Max"
2. Type in a Maximum value you want to query the database by.

### Screenshots
Include screenshots for each step demonstrating the use of this feature.    
![Max 1.png](Max%201.png)

![Max 2.png](Max%202.png)


---

## 5. Sort Order
### Description
Sort order is a function allowing the user to sort by either a ascending or descending fashion.

### Steps
1. Click the drop down box next to Sort Order text
2. Select either Ascending or Descending

### Screenshots
![Sort 1.png](Sort%201.png)

![Sort 2.png](Sort%202.png)



---

## 6. Search
### Description  
The search feature encompassses all four prior steps after completeing each step, the user can click the search button and all queries will be executed and the databse will show the information.

### Steps
1. Make sure you completed step 1 to 4
2. Click the search button to display the query

### Screenshots
Include screenshots for each step demonstrating the use of this feature.    
![Search 1.png](Search%201.png)

![Search 2.png](Search%202.png)

![Search 3.png](Search%203.png)

---

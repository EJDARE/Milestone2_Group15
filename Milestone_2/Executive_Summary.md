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

## 3. Min and Max (Range Query)
### Description
The "Min" and "Max" fields word together to allow users to set a specific range of values for their search, based on a chosen nutirional category (e.g. Carbs, Fats, Vitatmins). These fields provide a more granular search by letting users define both the minimum and maximum thresholds. This is particularly useful when users want to narrow down results to food items that fall within a certain nutrional range.

This feature is helpful for users who are managing their diet, monitoring specific nutrient intake, or looking for food items within a defined caloric or nutrient range.

### Steps
1. Locate the "Min" and "Max" text boxes: Find the text boxes labeled "Min" and "Max" near the dropdown for "Select Carbs/Fats or Vitamins."
2. Select a category from the dropdown: Choose the nutrient type you want to search for, such as "Carbs," "Fats," or "Vitamins."
3. Enter a minimum value: Click inside the text box and type the minimum value you'd like to query. This could be a caloric value, amount of carbohydrates, fats, or vitamins. For example:

   1. Carbs: Enter "10" to search for foods with at least 10 grams of carbohydrates.
   2. Fats: Enter "5" to search for foods with a minimum of 5 grams of fat.
   3. Vitamins: Enter "100" to search for foods with at least 100 mg of a specific vitamin.

4. Enter a maximum value in the Max field: Type the maximum value you'd like to query (e.g., "50" for carbs or "20" for fats).
5. Submit or proceed with the search: After entering the Min and Max values, click the "Search" button (if available) or continue to the next step if adding more filters.

### Example Scenarios
1. If a user wants to find foods with a moderate amount of carbohydrates, they can set "Carbs" as the category, "10" in the Min field, and "50" in the Max field. The results will show foods containing between 10 and 50 grams of carbs.
2. If searching for low-fat options, the user might select "Fats" from the dropdown and set the range between "5" and "20" grams.

### Additional Features
1. Error Handling: If a user enters an invalid value (e.g., negative numbers or non-numeric characters), the system may prompt the user to correct the input.
2. Range Queries: In some systems, a "Max" field may also be available, allowing the user to specify both minimum and maximum values for a more precise search.
3. Validation: The system should validate the user input to ensure that the "Max" value is greater than the "Min" value, and that no invalid characters are entered.
4. Dynamic Updates: Once the user enters the "Max" value, the search results could automatically update to reflect the refined search based on the new parameters.
   
### Min Screenshots
Include screenshots for each step demonstrating the use of this feature.    
![Min 1.png](Min%201.png)

![Min 2.png](Min%202.png)

### Max Screenshots
Include screenshots for each step demonstrating the use of this feature.    
![Max 1.png](Max%201.png)

![Max 2.png](Max%202.png)

---
## 4. Sort Order
### Description
The "Sort Order" feature allows users to organize their search results either in ascending or descending order, based on the selected nutritional category (e.g., Carbs, Fats, Vitamins, or Caloric Value). This function helps users quickly view food items in their preferred order, such as from lowest to highest carb content or from highest to lowest caloric value.

**This feature is particularly useful for:**
1. Users who want to find foods with the least or most of a specific nutrient.
2. Easily comparing food items by ordering them in a logical sequence.

### Steps
1. Locate the dropdown box: Find the dropdown menu next to the "Sort Order" label.
2. Click on the dropdown box: Click the dropdown menu to reveal the sorting options.
3. Select either Ascending or Descending:
   1. Ascending (A to Z / Low to High): This option sorts the results in an upward order, showing the lowest values first (e.g., from the least carbs to the most carbs).
   2. Descending (Z to A / High to Low): This option sorts the results in a downward order, showing the highest values first (e.g., from the highest calorie count to the          lowest).
4. View sorted results: Once a sort order is selected, the search results will automatically rearrange themselves according to your preference, either showing the highest      values first (Descending) or the lowest values first (Ascending).

**Example Use Case**
1. If a user is searching for foods with fats, they may want to find the food with the least fat content first. In this case, they would select "Ascending" to display          results from the lowest to highest fat content.
2. Conversely, a user looking for the most calorie-dense foods could select "Descending" to show the items with the highest caloric values first.

**Additional Features**
1. Default Sorting: The system may have a default sort order (usually ascending), which users can override by selecting their preferred option.
2. Dynamic Sorting: Some systems automatically re-sort results in real-time as the user switches between ascending and descending options, providing immediate feedback.
3. Multi-level Sorting: Advanced versions of this feature may allow users to sort by multiple criteria (e.g., sort by carbs first and then by vitamins) for more customized     searches.

### Screenshots
![Sort 1.png](Sort%201.png)

![Sort 2.png](Sort%202.png)


---

## 5. Search
### Description  
The "Search" feature is the final step that executes all the previous selections and inputs (from steps 1 to 4). Once the user has specified their search criteria—such as selecting a nutritional category, entering minimum and maximum values, and choosing a sort order—they can click the "Search" button to initiate the query. The system will then process the inputs and return the filtered and sorted results from the database, showing the relevant food items that match the user’s specifications.

This feature serves as the gateway to retrieving tailored results based on the user's preferences for Carbs, Fats, Vitamins, or other nutritional elements.

### Steps
1. Verify that steps 1 to 4 are complete:
   1. Ensure that you have selected a nutritional category (Carbs, Fats, or Vitamins).
   2. Specify a minimum and maximum value, if applicable.
   3. Choose a sort order (Ascending or Descending) to organize the results.
2. Click the "Search" button: Once all necessary fields are completed, locate and click the "Search" button to execute the query.
3. View the results: The system will process the inputs and display the filtered and sorted results. The displayed items will meet the criteria based on the user’s input       (e.g., a list of foods high in fats sorted from lowest to highest fat content).

**Example Scenario**
If a user selects "Carbs" from the dropdown, enters a minimum value of "10" and a maximum value of "50," and chooses "Ascending" as the sort order, clicking the "Search" button will return a list of foods with carbohydrates between 10 and 50 grams, sorted from the lowest to highest amount of carbs.

**Additional Features**
1. Error Handling: If any required fields are missing (e.g., no "Min" or "Max" value is entered), the system may prompt the user to complete the necessary fields before        performing the search.
2. Search Reset: After performing a search, the system may provide an option to reset the search fields, allowing users to start a new search with fresh criteria.

### Screenshots
Include screenshots for each step demonstrating the use of this feature.    
![Search 1.png](Search%201.png)

![Search 2.png](Search%202.png)

![Search 3.png](Search%203.png)


---

# Video-Games-Sales-Analysis
Overview:

The tool loads cleaned video game sales data from a CSV file and presents a dropdown menu of video game titles to the user. Upon selection of a game title, a bar graph dynamically updates to display the sales data of the selected game across different regions (NA_Sales, EU_Sales, JP_Sales, Other_Sales).

How it works:

1.	The program reads the cleaned CSV file using pandas, which contains information about video game sales.
2.	A plotly FigureWidget is created, which will contain a bar graph. This graph displays the regional sales data for the selected video game. Initially, the graph is empty.
3.	A dropdown menu is created using ipywidgets, and it is populated with the unique names of the video games from the DataFrame.
4.	An update function is defined, which is triggered when a new game title is selected from the dropdown. This function fetches the sales data for the selected game and updates the y-values of the bar graph with this data. The plot's title is also updated to reflect the name of the selected game. If no data is found for a game, a message is printed out indicating this.
5.	The dropdown and the figure are displayed, presenting an interactive interface to the user.

Libraries Used:

•	pandas: Used for efficient data manipulation and analysis.
•	plotly.graph_objects: Used for creating interactive plots.
•	ipywidgets: Used for creating interactive widgets like the dropdown menu.

Usage:

1.	Make sure the cleaned CSV file (cleaned_video_game_sales_withname.csv) is in the correct path as specified in the code.
2.	Run the script in a Python environment that supports widgets, such as Jupyter notebooks.
3.	A dropdown menu will be displayed, containing the names of the video games. Select a game.
4.	Upon selection, the bar graph below will update to reflect the sales data for the chosen game across different regions.
5.	To analyze another game, simply select another game from the dropdown menu.

With this tool, users can easily explore and analyze video game sales data, making it an invaluable resource for video game analysts, marketers, and enthusiasts alike. Enjoy exploring the fascinating world of video game sales data!
![image](https://github.com/mourtashi/Video-Games-Sales-Analysis/assets/109982496/b2a60254-9be6-40fc-ad32-168847387742)

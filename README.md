# Grazioso Salvare Dashboard
<img width="685" height="683" alt="Grazioso Salvare Logo" src="https://github.com/user-attachments/assets/f63bb083-2cc8-4f18-b9dd-09137eb09c95" />

## About the Project
This project features a data dashboard for the Austin Animal Center Outcomes dataset, built to provide interactive visualization and dynamic filtering for animal rescue and adoption information.

The dashboard enables users to do the following:

- Filter animals by rescue type:
  - **Water**
  - **Mountain/Wilderness**
  - **Disaster**
  - **Reset All**
- View an interactive data table that updates dynamically based on filters.
- Explore a geolocation map showing selected animal locations.
- View a breed distribution pie chart that updates with filtered data.


You can view a screencast demonstration at the link below. Supplemental screenshots are provided in the “How to Run the Dashboard” section.
[**Screencast Demonstration** ](https://drive.google.com/file/d/1ZYiJ7AAtfA_RAqt56Gg-c-pCSEHg5CBT/view?usp=sharing)

---

## Tools and Rationale

### **MongoDB**
Used as the model component to store and retrieve the Austin Animal Center dataset.  
MongoDB’s flexible JSON-like document structure and PyMongo’s support for field queries, regex searches, and range queries make it ideal for filtering by breed, sex, and age.

### **Dash Framework**
Provides the view and controller structure, supporting:
- Interactive UI components (RadioItems, DataTable, graphs)
- Callback functions linking filters → table → map → charts  
- Plotly integration for high-quality charts  
- Dash Leaflet for interactive mapping

### **Additional Python Libraries**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Plotly**
- **Dash**
- **Dash Leaflet**

Documentation links:
- [Dash Documentation](https://dash.plotly.com/)
- [Plotly Express Documentation](https://plotly.com/python/plotly-express/)
- [PyMongo Documentation](https://pymongo.readthedocs.io/en/stable/)

---

## Project Steps

### **1. Setup Database Access**
- Imported `AnimalShelter` CRUD module  
- Connected using username: **aacuser**  
- Password: **sUchStr0ngP4S$w0rD**

### **2. Data Cleaning and Transformation**
- Loaded documents into a Pandas DataFrame  
- Removed `_id` to prevent dashboard issues  
- Added `species` column  
- Rounded `age_upon_outcome_in_weeks` to nearest integer  

### **3. Dashboard Layout**
Created using **JupyterDash**, including:
- Header  
- Logo  
- Identifier  
- Filter panel  
- Data table  
- Pie chart  
- Geolocation map  

### **4. Interactive Filtering**
- Built `build_rescue_query()` to match selected filters with MongoDB queries  
- Used `update_dashboard()` to refresh table data via callbacks  

### **5. Dynamic Widgets**
- `update_graphs()` → updates pie chart  
- `update_map()` → updates map markers, popups, tooltips  

### **6. Selection Management**
- Table row selection resets automatically when filters change  

---

## Challenges and Solutions

### **Dynamic Selection Reset**
**Challenge:** Table selection persisted incorrectly across filter changes  
**Solution:** Returned `selected_rows=[]` in the callback when filters update table data  

### **Column Name Variations**
**Challenge:** Latitude, longitude, breed, and name fields varied in dataset  
**Solution:** Added dynamic column detection and fallbacks  

### **Geolocation Map Rendering**
**Challenge:** Missing/invalid coordinates caused errors  
**Solution:** Added validation checks before rendering markers  

---

## How to Run the Dashboard

### **1. Install Dependencies**
```bash
pip install jupyter-dash dash dash-leaflet plotly pandas numpy matplotlib
```
### 2. Ensure the Python CRUD Module is Present
Make sure `CRUD_Python_Module.py` is located in the same folder as the dashboard code.

### 3. Open the Dashboard Notebook
Open `ProjectTwoDashboard.ipynb` in **Jupyter Notebook** or **JupyterLab**.

### 4. Run All Cells
Use **Run All** from the toolbar to execute the notebook.

### 5. Open the Dashboard in Your Browser
By default, the dashboard will run on:  
- [http://127.0.0.1:8050/](http://127.0.0.1:8050/)  
- [http://localhost:8050/](http://localhost:8050/)

> *Note: JupyterDash may automatically open a separate browser tab.*

### 6. Interact with the Dashboard
- Use the **filter radio buttons** to explore the dataset.  
- Click on **table rows** to update the map.  
- View the **breed distribution pie chart**, which updates dynamically based on filtered data.


## Additional Screenshots:
<img width="512" height="260" alt="image1" src="https://github.com/user-attachments/assets/c02b5172-04c3-4dea-b7b0-09918d84916c" />
<img width="512" height="222" alt="image2" src="https://github.com/user-attachments/assets/ce0892bb-5590-4ea2-9f52-e3d6ef1988da" />
<img width="512" height="222" alt="image3" src="https://github.com/user-attachments/assets/d93540f1-829f-45d1-8fa1-a0f8dd49ee66" />

## Contact Information:
We’re always open to suggestions! Feel free to reach out to the Global Rain team at the [Global Rain Contact Page](https://globalrain.com/contact-us)
 or open an issue on our GitHub repository. Pull requests are also welcome!

## 8-2 Journal: Reflection
When writing applications, I focus on separating all responsibilities into clear modules to ensure that they are both maintainable and adaptable. Other key coding practices include using meaningful variable and function names, and only adding comments where logic isn't immediately obvious to achieve high readability. This approach was especially important in Project One as it ensured the database logic could be reused in Project Two, preventing redundant query logic from being embedded directly in the dashboard code. A notable advantage of working in this manner is that modifications to database queries or filters could be made in one place without affecting the dashboard layout or callbacks. Furthermore, this CRUD module can now be reused for other dashboards, reports, or backend services that require access to the Austin Animal Center data. 

Approaching a problem from the vantage point of a computer scientist begins by analyzing the client's requirements and breaking them down into smaller, more manageable components. For instance, one might divide this project into smaller scopes like data storage, filtering logic, and visualization. As opposed to my previous approach that often begins with tackling a single, isolated problem, this project required coordinating multiple technologies in concert like MongoDB, Python, and Dash to ensure that database queries returned accurate data prior to integrating them into widgets. In the future, I would apply the same strategy of requirement analysis, modular design, and iterative testing when creating databases and applications for other clients. 

Solutions designed by computer scientists involve transforming raw data into usable information; this process is paramount in helping organizations make informed decisions. As such, the project dashboard enables Grazioso Salvare to quickly identify suitable animals for rescue operations, which in turn improves efficiency and supports their company mission.


# Library Management System

A comprehensive Library Management System built with modern tools and technologies to efficiently manage books, users, and book issuance records.

## Overview
This project is a complete solution for managing library operations. It includes a frontend built with **Streamlit**, a backend implemented using **Python (Flask)**, and a database powered by **MySQL**. The system allows for the addition of new users, books, and tracking issued books, along with their history.

---

## Features
- **Frontend**: Interactive and user-friendly UI built with **Streamlit**.
- **Backend**: Robust backend powered by **Python** and **Flask**.
- **Database**: Persistent data storage using **MySQL**.
- **Functionalities**:
  - Add new users and books.
  - View issued books history.
  - Manage library records seamlessly.

---

## Technologies Used
- **Frontend**: Streamlit
- **Backend**: Python (Flask)
- **Database**: MySQL

---

## Installation and Setup

Follow these steps to get the project up and running:

### Prerequisites
- Python 3.x installed
- MySQL installed and running
- Git installed (optional)

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/amanbhati/Library-Management-Sysytem.git
   cd Library-Management-Sysytem
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up MySQL Database**
   - Open MySQL and create a database:
     ```sql
     CREATE DATABASE library;
     ```
   - Configure the database in your Flask app by updating the connection string in the code:
     ```python
     conn = mysql.connector.connect(
         host="localhost",
         user="your_username",
         password="your_password",
         database="library"
     )
     ```

5. **Run the Flask Backend**
   ```bash
   python library_management.py
   ```

6. **Run the Streamlit Frontend**
   ```bash
   streamlit run libstream.py
   ```

7. **Access the Application**
   - Open your browser and navigate to:
     - Streamlit Frontend: [http://localhost:8502](http://localhost:8502)
     - Flask Backend (if required): [http://localhost:5000](http://localhost:5000)

---

## **Screenshots**
![**Home Page**](https://github.com/amanbhati/Library-Management-Sysytem/blob/main/Screenshot%202025-01-16%20224537.png)
---

## Future Enhancements
- Add user authentication and roles.
- Implement book return functionality.
- Enhance UI with advanced visualization.

---

## Contributing
Contributions are welcome! Feel free to fork the repository and create a pull request with your changes.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
For any inquiries or feedback, reach out to [Aman Kumar Bhati](mailto:amanbhati@example.com).

---

Happy Coding! 🚀

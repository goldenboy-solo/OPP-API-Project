Limkokwing Library Management API

INTRODUCTION
The Limkokwing Library Management API is a modern web-based application developed using FastAPI, PostgreSQL, and SQLAlchemy ORM to automate and improve library management processes. Traditional library systems often rely on manual record keeping, which can result in inefficiencies, data duplication, difficulties in tracking borrowed books, and limited access to information. This project addresses these challenges by providing a secure, scalable, and centralized digital platform for managing library resources.
The system enables administrators, librarians, and members to interact with library services based on their assigned roles. Administrators have full control over the system, including managing users, books, authors, and reviews. Librarians are responsible for managing books and authors as well as handling borrowing and returning operations. Members can browse available books and authors and submit reviews on books they have read.
The application was developed following modern software engineering principles and RESTful API standards. FastAPI was selected as the primary framework because of its high performance, automatic API documentation, and support for asynchronous programming. PostgreSQL serves as the backend database for storing and managing system data, while SQLAlchemy ORM provides efficient database interaction through Python objects.
Security is a major component of the system. The project implements OAuth2 authentication, JSON Web Tokens (JWT), password hashing using bcrypt, and Role-Based Access Control (RBAC) to ensure that users can only perform actions permitted by their assigned roles. Dependency Injection is used throughout the project to improve code maintainability, modularity, and scalability.
Additionally, the project aligns with Sustainable Development Goal (SDG) 4: Quality Education. By providing an organized platform for managing educational resources such as books and learning materials, the system contributes to improved access to knowledge and supports educational development.
Overall, the Limkokwing Library Management API demonstrates practical application of modern backend development techniques, database management, authentication mechanisms, software architecture principles, and open-source development practices. The project serves as a reliable foundation for future enhancements and real-world library management solutions. 
Project Structure

 
PROJECT OBJECTIVES
The main objective of this project is to develop a secure and efficient Library Management System using FastAPI and PostgreSQL.
Specific objectives include:
•	To provide a centralized platform for managing books, authors, reviews, and borrowing activities.
•	To implement secure user authentication using OAuth2 and JWT tokens.
•	To enforce Role-Based Access Control (RBAC) for Admin, Librarian, and Member users.
•	To demonstrate CRUD operations using SQLAlchemy ORM and PostgreSQL.
•	To implement dependency injection using FastAPI's Depends() feature.
•	To demonstrate asynchronous programming through a book search endpoint.
•	To provide automatic API documentation using Swagger UI and ReDoc.
•	To support Sustainable Development Goal 4 (Quality Education) by improving access to educational resources.
•	To apply modern software engineering principles and RESTful API standards.
•	To create a scalable backend system suitable for future enhancements.
 
CONCLUSION
The Limkokwing Library Management API was successfully designed and implemented using FastAPI, PostgreSQL, SQLAlchemy ORM, and JWT Authentication. The system provides a secure, efficient, and scalable solution for managing library operations, including user management, author management, book management, reviews, and borrowing activities.
Through the implementation of Role-Based Access Control, the system ensures that users can only access functionalities appropriate to their roles, thereby improving security and maintaining data integrity. The use of dependency injection and asynchronous programming demonstrates adherence to modern backend development practices and enhances the maintainability and performance of the application.
The project also supports Sustainable Development Goal 4 (Quality Education) by promoting effective management of educational resources and improving access to learning materials. Automatic API documentation through Swagger UI and ReDoc further improves usability and developer experience.
Overall, this project successfully demonstrates the practical application of software engineering principles, database management, RESTful API development, authentication and authorization mechanisms, and open-source development practices. The system provides a strong foundation for future enhancements such as reservation systems, overdue notifications, reporting dashboards, and frontend integration.

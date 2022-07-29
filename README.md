# anima_lib_team-91
A library that allows beginners perform basic web animation using normal language

## The UML Database Model
![alt text](./out/db_schema/uml_database_model.png)

### User Model
From the UML Diagram above; the `User` model represents a user registered on our website. The `User` has a `id` field which is the Primary Key; it also has a `firstName`, `lastName`, `username` and an `email` field which store String values. There are also `profile_pic` and `password` which store an Image and Hash characters respectively.

### CustomAnimation
From the UML Diagram above; the `CustomAnimation` model represents a custom animation created by each user on our website. The `CustomAnimation` has a `id` field which is the Primary Key; it also has a `title` field which store String values. There are also `date_last_created` and `src_code` which store a Date and CSS snippet respectively. It also has a `author` field which is a Foreign Key and stores the Primary Key of the `User` that created the `CustomAnimation`.
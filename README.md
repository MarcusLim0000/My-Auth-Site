# My-Auth-Site

**My Auth Site** is a simple user authentication and authorization app that utilizes groups to support multiple user accounts. It is built using Django version 5.0.7 and Python version 3.12.3. This application allows users to be divided into three main groups, with permissions managed on the Django admin dashboard by a registered superuser. The three main groups are Head Office, District Office, and Branch Office. This project is styled using crispy-forms with Bootstrap 4. The authentication and authorization of users are implemented by the Django framework itself. This project is intended to run on localhost.

## Features
- User accounts are divided into three main groups: Head Office, District Office, and Branch Office.
- Permissions for each group are managed through the Django admin dashboard by a superuser.
- The project uses crispy-forms with Bootstrap 4 for styling.

## User Groups and Permissions
1. **Head Office**: 
    - Head office accounts are created by registering first.
    - Once logged in, Head Office users can create multiple accounts using the “Create new user” link on the side navbar.
    - They can also view a list of the users they have created using the “View” link.
2. **District Office**:
    - District Office accounts can create Branch Office accounts but cannot create other Head Office or District Office accounts.
    - They have the ability to view users they have created.
3. **Branch Office**:
    - Branch Office accounts cannot create any accounts.
    - They can only view company content.

## Steps to Use This Website
1. **Setup**:
    - Clone or download this Git repository into a Python + Django enabled environment.
    - Navigate to the repository using a shell such as Git Bash or CLI.
    - Run the following commands:
      ```
      python manage.py makemigrations
      python manage.py migrate
      python manage.py runserver
      ```
    - Copy the host URL and paste it into a browser (ideally Google Chrome).

2. **Creating Accounts**:
    - First a super user has to be made to create the groups in Django Admin dashboard. Create the superuser by using a shell/CLI such as windows CMD or git bash. Navigate to the repo address and use this command: "python manage.py createsuperuser". Follow the instructions to create the superuser.
    - Access the admin dashboard by adding "/admin" to your server localhost port url which has been opened on the browser.
    - Create the following groups: Head Office, District Office, Branch Office.
    - Adjust permissions for each group.
    - A Head Office user is created using the website. Since multiple companies might use this website, the initial user registering on the site has the option to choose Head Office as their group.
    - Once an account is created, another user can log in using those credentials.

3. **Managing Users**:
    - **Head Office Accounts**:
        - Can create District Office and Branch Office accounts but cannot create other Head Office accounts.
    - **District Office Accounts**:
        - Can create Branch Office accounts but cannot create Head Office or other District Office accounts.
    - **Branch Office Accounts**:
        - Can only view content and cannot create any accounts.

4. **User and Group Management**:
    - A superuser for the Django framework must be created using the CLI.
    - The superuser logs into the admin dashboard to manage all users, groups, and their permissions.

